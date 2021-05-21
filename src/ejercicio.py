

TIPOS= { 'selección múltiple':0, 'completar':1, 'emparejar':2}

class Ejercicio (object):
    '''
    grupo:  identifica una categoría para la pregunta
    tipo: el tipo de pregunta, -1 indica múltiples tipos
    n: el número de preguntas a generar, si se especifica -1
    será el máximo
    preguntas: lista con las respectivas variantes

    offsetIndice: indica el offset para asignar el número de pregunta
    '''
    def __init__(self, enunciado,preguntas, grupo,tipo=-1,offsetIndice=0):
        self.grupo=grupo
        self.tipo=tipo
        self.offsetIndice=offsetIndice
        self.preguntas= preguntas
        for i in range(len(preguntas)):
            var=preguntas[i]['variante']
            var=[self.CorrigeFormato(str(v)) for v in var]
            preguntas[i]['variante']=var
            rta=preguntas[i]['respuesta']
            preguntas[i]['respuesta']=self.CorrigeFormato(rta)
          
        self.enunciado=self.CorrigeFormato(enunciado)
        # Obtiene el número de argumentos del enunciado
        # Argumentos para las variantes
        self.nArgsV=enunciado.count('@v')
        # Argumentos o espacios a completar
        self.nArgsC=0
        if tipo == 1:
            self.nArgsC=enunciado.count('@c')

    def CorrigeFormato(self, s):
        '''
        Ajusta el formato latex para que funcione sin problemas en moodle
        '''
        #sn=s.replace('\\{','\\\\')
        if not isinstance(s,str):
            return str(s)
        sn=s.replace('{','\{')
        sn=sn.replace('}','\}')
        sn=sn.replace('=','\=')
        return sn
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def Enunciado(self, variante):
        '''
        Se define un enunciado dada la variante que 
        corresponde a un diccionario con los 
        parámetros a cambiar en el argumento
        '''
        if not isinstance( variante,(list,tuple)):
            raise Exception(' El formato de variante es inadecuado, debe ser una lista o tupla')
        if len(variante) > self.nArgsV:
            raise Exception('La cantidad de argumentos es incorrecta para generar el enunciado')
        s=self.enunciado
        for i, v in enumerate(variante):
            s=s.replace('@v%i'%(i+1), v )#Se quitó la finalización con espacio
        return s

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def Respuesta(self,enunciado, respuestas, iPregunta):
        '''
        Ajusta el enunciado con las respuestas,
        donde la primera es la respuesta correcta
        '''
        s='::%s_%i::\n'%(self.grupo,iPregunta+self.offsetIndice+1)

        if self.tipo==0:
            # Selección múltiple con única respuesta
            s+=enunciado+'\n'
            s+='{\n'
            s+='  =%s\n'%respuestas[0]
            for rta in respuestas[1:]:
                s+='  ~%s\n'%rta
                s+='}\n'
        elif self.tipo==1:
            # Completar
            en=enunciado
            for i, rta in enumerate(respuestas):
                en=en.replace('@c%i '%(i+1), str(v)+' ' )
            s+=en
        return s
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def __call__(self,o=6, total=-1, offsetIndice=-1):
        '''
        p: cantidad de preguntas
        o: número de opciones si es una pregunta de seleeción múltiple
        '''
        s='\n'
        if offsetIndice >=0:
            self.offsetIndice= offsetIndice
        if self.tipo==0:
            # Selección múltiple con única respuesta
            # Se arman los grupos para las opciones de respuestas
            if len(self.preguntas)< o:
                raise Exception('El número de preguntas es inferior a las opciones solicitadas')
            #Se guardarán como tuplas de variantes y lista de opciones
            preguntas=self.preguntas[:]
            #print('  *dim preg:',len(preguntas))
            np=len(self.preguntas)
            if 0< total < np:
                np=total
            #n= np-o #Cantidad de preguntas a anexar al final
            preguntas+=self.preguntas[:o]
            #print('  *dim preg:',len(preguntas))
            for i in range(np):
                variante=preguntas[i]['variante']
                enunciado=self.Enunciado(variante)
                respuestas= [ preg['respuesta'] for preg in preguntas[i:i+o] ]
                s+=self.Respuesta(enunciado, respuestas,i)+'\n'
            
        return s
