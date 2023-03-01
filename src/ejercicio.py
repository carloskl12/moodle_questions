
TIPOS= { 'selección múltiple': 0, 
    'completar': 1, 
    'emparejar': 2, 
    'verdadero falso': 3,
    'opciones específicas': 4,
}

class Ejercicio (object):
    """
    Se debe tener cuidado con los parámetros a variar con @v#, pues solo 
    se puede tomar hasta 9 variantes, con dos dígitos puede haber problemas
    debido a que el patron @v1 se puede confundir con cualquier @v1#,
    algo similar ocurre con @c#.
    """
    def __init__(self, enunciado,preguntas, grupo,tipo=-1,offsetIndice=0):
        
        '''
        enunciado: enunciado de la pregunta
        preguntas: lista de un diccionario con 
            campos variante (lista de opciones que cambian en el enunciado)
            y respuesta (string con la respuesta)
        grupo:  identifica una categoría para la pregunta
        tipo: el tipo de pregunta, -1 indica múltiples tipos
        offsetIndice: indica el offset para asignar el número de pregunta
        '''
        
        self.grupo = grupo
        self.tipo = tipo
        self.offsetIndice = offsetIndice
        self.preguntas = preguntas
        for i in range(len(preguntas)):
            var = preguntas[i]['variante']
            var = [self.CorrigeFormato(str(v)) for v in var]
            preguntas[i]['variante'] = var
            rta = preguntas[i]['respuesta']
            preguntas[i]['respuesta'] = self.CorrigeFormato(rta)
          
        self.enunciado = self.CorrigeFormato(enunciado)
        # Obtiene el número de argumentos del enunciado
        # Argumentos para las variantes
        self.nArgsV = enunciado.count('@v')
        # Argumentos o espacios a completar
        self.nArgsC = 0
        if tipo == 1:
            self.nArgsC = enunciado.count('@c')

    def CorrigeFormato(self, s):
        '''
        Ajusta el formato latex para que funcione sin problemas en moodle
        '''
        #sn=s.replace('\\{','\\\\')
        if  self.tipo in (1,2,4) and isinstance(s, (list, tuple)):
            return [self.CorrigeFormato(v) for v in s]
            
        if not isinstance(s,str):
            return str(s)
        sn = s.replace('{','\{')
        sn = sn.replace('}','\}')
        sn = sn.replace('=','\=')
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
        s = self.enunciado
        #if self.tipo == 2: # emparejar
        #    return s
        for i, v in enumerate(variante):
            s = s.replace('@v%i'%(i+1), v )#Se quitó la finalización con espacio
        return s

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def Respuesta(self,enunciado, respuestas, iPregunta):
        '''
        Ajusta el enunciado con las respuestas,
        donde la primera es la respuesta correcta
        '''
        s = '::%s_%i::\n'%(self.grupo,iPregunta+self.offsetIndice+1)

        if self.tipo in (0,4):
            # Selección múltiple con única respuesta
            s += enunciado+'\n'
            s += '{\n'
            s += '  =%s\n'%respuestas[0]
            for rta in respuestas[1:]:
                s += '  ~%s\n'%rta
            s += '}\n'
        elif self.tipo == 1: #completar
            # Completar
            if len(respuestas) != self.nArgsC:
                se="El número de valores a completar no coincide:"
                se+=" se esperaban %i campos y se tienen %i."%(self.nArgsC, len(respuestas))
                print(respuestas, len(respuestas))
                raise Exception(se)
            en = enunciado
            for i, rta in enumerate(respuestas):
                sc = "" #campo de la respuesta 
                if isinstance( rta, (list, tuple)):
                    for v in rta:
                        sc+="=%s "%str(v)
                else:
                    sc = "=%s "%str(rta)
                en = en.replace('@c%i'%(i+1), '{ %s }'%sc )
            s += en+"\n"
        
        elif self.tipo == 2: #emparejar
            s += enunciado+'\n'
            s += '{\n'
            for a,b in respuestas:
                s += '  =%s  ->  %s\n'%(a,b)
            s += '}\n'
            
        elif self.tipo == 3: #verdadero falso
            if respuestas[0] not in 'TF':
                raise Exception('La respuesta debe ser True o False')
            s += enunciado + "{%s}\n"%respuestas[0] 
        
        

        return s

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def __call__(self,o = 6, total = -1, offsetIndice = -1):
        '''
        Genera un string de las preguntas según los parámetros:
        o: número de opciones si es una pregunta de seleeción múltiple
        total: cantidad de preguntas, si es -1 se toma la cantidad máxima
        offsetIndice: indica un offset para numerar las preguntas
        '''
        s = '\n'
        if offsetIndice >=0 :
            self.offsetIndice = offsetIndice
        
        #número de preguntas
        np = len(self.preguntas)
        if 0 < total < np:
            np = total
        if self.tipo == 0:
            # Selección múltiple con única respuesta
            # Se arman los grupos para las opciones de respuestas
            if len(self.preguntas) < o:
                raise Exception('El número de preguntas es inferior a las opciones solicitadas')
            #Se guardarán como tuplas de variantes y lista de opciones
            preguntas = self.preguntas[:]
            #print('  *dim preg:',len(preguntas))
            
            
            #n= np-o #Cantidad de preguntas a anexar al final
            preguntas += self.preguntas[:o]
            #print('  *dim preg:',len(preguntas))
            for i in range(np):
                variante = preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = [ preg['respuesta'] for preg in preguntas[i:i+o] ]
                s += self.Respuesta(enunciado, respuestas,i)+'\n'
        elif self.tipo == 1: #completar
            for i in range(np):
                variante = self.preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = self.preguntas[i]['respuesta'] # lista de opciones
                s += self.Respuesta(enunciado, respuestas,i)+'\n'
                
        elif self.tipo == 2: #emparejar
            for i in range(np):
                variante = self.preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = self.preguntas[i]['respuesta'] # lista de opciones
                s += self.Respuesta(enunciado, respuestas,i)+'\n'
        elif self.tipo == 3: #verdadero falso
            for i in range(np):
                variante = self.preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = self.preguntas[i]['respuesta'] # lista de opciones
                s += self.Respuesta(enunciado, respuestas,i)+'\n'
        elif self.tipo == 4: #opciones específicas
            for i in range(np):
                variante = self.preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = self.preguntas[i]['respuesta']
                s += self.Respuesta(enunciado, respuestas,i)+'\n'
        return s
