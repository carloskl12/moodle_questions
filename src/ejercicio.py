
TIPOS= { 'selección múltiple': 0, 
    'completar': 1, 
    'emparejar': 2, 
    'verdadero falso': 3,
    'opciones específicas': 4,
    'múltiples respuestas':5,
    'preguntas anidadas':6,
}


class Ejercicio (object):
    """
    Se debe tener cuidado con los parámetros a variar con @v#, pues solo 
    se puede tomar hasta 9 variantes, con dos dígitos puede haber problemas
    debido a que el patron @v1 se puede confundir con cualquier @v1#,
    algo similar ocurre con @c#.
    """
    def __init__(self, enunciado=None, preguntas=None, grupo=None, 
        tipo=-1,offsetIndice=0, ejercicio=None):
        
        '''
        enunciado: enunciado de la pregunta
        preguntas: lista de un diccionario con 
            campos variante (lista de opciones que cambian en el enunciado)
            y respuesta (string con la respuesta)
        grupo:  identifica una categoría para la pregunta
        tipo: el tipo de pregunta, -1 indica múltiples tipos
        offsetIndice: indica el offset para asignar el número de pregunta
        '''
        if ejercicio != None:
            if not isinstance(ejercicio, Ejercicio):
                raise Exception("ejercicio debe ser una instancia de la clase Ejercicio")
            self.enunciado = ejercicio.enunciado
            self.preguntas = ejercicio.preguntas
            self.grupo = ejercicio.grupo 
            self.tipo = ejercicio.tipo
            self.nArgsV = ejercicio.nArgsV
            self.nArgsC = ejercicio.nArgsC
            self.offsetIndice = ejercicio.offsetIndice
        else:
            self.grupo = grupo
            self.tipo = tipo
            self.offsetIndice = offsetIndice
            self.preguntas = preguntas
            for i in range(len(preguntas)):
                var = preguntas[i]['variante']
                var = [self.CorrigeFormato(str(v)) for v in var]
                preguntas[i]['variante'] = var
                if tipo != 6: # en cloze no hay parámetro de respuestas
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
                if self.nArgsC > 1:
                    raise Exception("Solo se puede indicar un valor para completar")

    def CorrigeFormato(self, s):
        '''
        Ajusta el formato latex para que funcione sin problemas en moodle
        '''
        #sn=s.replace('\\{','\\\\')
        if  self.tipo in (0,1,2,4,5) and isinstance(s, (list, tuple)):
            return [self.CorrigeFormato(v) for v in s]
            
        if not isinstance(s,str):
            return str(s)
        sn = s
        if self.formato == 'gift':
            sn = s.replace('{','\{')
            sn = sn.replace('}','\}')
        
            sn = sn.replace('=','\=')
        return sn
    @property
    def formato(self):
        """Formato de las preguntas"""
        return 'gift'

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
            raise Exception(f'La cantidad de argumentos es incorrecta para generar el enunciado: se esperaban {self.nArgsV} variantes, pero se tienen {len(variante)}')
        s = self.enunciado
        #if self.tipo == 2: # emparejar
        #    return s
        for i, v in enumerate(variante):
            s = s.replace('@v%i'%(i+1), v )#Se quitó la finalización con espacio
        return s

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def Respuesta(self,enunciado, respuestas, iPregunta, feedback = None):
        '''
        Ajusta el enunciado con las respuestas,
        donde la primera es la respuesta correcta
        '''
        numPregunta = iPregunta+self.offsetIndice+1
        numPregunta = str(numPregunta).zfill(self.numdigitos)
        s = '::%s_%s::\n'%(self.grupo,numPregunta)

        if self.tipo in (0,4):
            
            
            # Selección múltiple con única respuesta
            s += enunciado+'\n'
            s += '{\n'
            s += '  =%s\n'%respuestas[0]
            for rta in respuestas[1:]:
                s += '  ~%s\n'%rta
            s += '}\n'
            
            # valida que no hayan respuestas repetidas
            unicos = []
            for i, r in enumerate(respuestas):
                if r not in unicos:
                    unicos.append(r)
                else:
                    se = "La opción %i repetida:\n    %s"%(i+1,str(r))
                    se += "\n    en: "+s
                    raise Exception(se)
            
        elif self.tipo == 1: #completar
            # Completar
            if  self.nArgsC != 1:
                raise Exception("No se halló la ubicación a completar")
            en = enunciado
            sc = "" #campo de la respuesta 
            for i, rta in enumerate(respuestas):
                sc+="=%s "%str(rta)
            en = en.replace('@c1', '{ %s }'%sc )
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
        else:
            raise Exception(f'El tipo especificado "{self.tipo}" no está implementado')
        

        return s

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def __call__(self,o = 6, total = -1, offsetIndice = -1):
        '''
        Genera un string de las preguntas según los parámetros:
        o: número de opciones si es una pregunta de selección múltiple
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
        # Calcula el número de digitos para esta categoría
        self.numdigitos = len(str(offsetIndice+np))
        
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
        elif self.tipo in (1,2,3,4,5,6): #completar
            for i in range(np):
                variante = self.preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = self.preguntas[i].get('respuesta',None) # lista de opciones
                puntos = self.preguntas[i].get( 'puntos', None)
                feedback = self.preguntas[i].get('feedback',None)
                s += self.Respuesta(enunciado, respuestas,i,feedback, puntos)+'\n'
        else:
            raise Exception(f'El tipo especificado "{self.tipo}" no está implementado')
        return s

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import xml.etree.ElementTree as ET
class EjercicioXML(Ejercicio):
    """
    Encapsula un conjunto de ejercicios para crear un nodo XML
    """
    
    @property
    def formato(self):
        """Formato de las preguntas"""
        return 'xml'
    
    def AppendElement(self, element, tag, value="", attribute=None):
        """
        Anida un nuevo elemento al elemento
        
        element: elemento en el que se anida el nuevo elemento.
        tag: nombre del tag
        value: valor de texto que se incluye en el nuevo elemento
        attribute: un diccionario con diferentes atributos que se agregan al 
            nuevo elemento
        """
        newElement = ET.SubElement( element, tag)
        if value != "":
            if isinstance(value, str):
                newElement.text = value
            else:
                print(value)
                raise Exception("Se esperaba una cadena de caracteres para textValue")
        if attribute != None:
            if isinstance(attribute, dict):
                for k,v in attribute.items():
                    if isinstance(k,str) and isinstance(v,str):
                        newElement.set(k,v)
                    else:
                        raise Exception(
                          "Los atributos deben tener nombre y valor como un string")
                    
            else:
                raise Exception(
                    "Los atributos se deben especificar como un diccionario")
                
                
        return newElement
    
    
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def Respuesta(self,enunciado, respuestas, iPregunta, feedback = None, puntos=None):
        '''
        Ajusta el enunciado con las respuestas,
        donde la primera es la respuesta correcta,
        retorna un nodo de respuesta
        
        puntos: indica los puntos que tiene cada respuesta en los casos que 
        lo requiere
        '''
        
        if feedback != None and len(feedback) == len(respuestas):
            pass
        else:
            feedback = None
        
        TIPOS_XML = {
            0: "multichoice", 
            1: "shortanswer", 
            2: "matching", 
            3: "truefalse",
            4: "multichoice",
            5: "multichoice",
            6: "cloze",
        }
        
        nd = ET.Element('question')
        # Se asigna el tipo de pregunta
        nd.set('type',TIPOS_XML[self.tipo])
        
        # Crear el nombre basado en la categoría y el número de indice y offset
        nombre = ET.SubElement(nd, 'name')
        txtNombre = ET.SubElement(nombre,'text')
        numPregunta = iPregunta+self.offsetIndice+1
        numPregunta = str(numPregunta).zfill(self.numdigitos)
        txtNombre.text = '%s_%s'%(self.grupo,numPregunta)
        if self.tipo in (0,4,5):
            #print("*pregunta tipo:", self.tipo)
            # Se indica el enunciado
            qtext = ET.SubElement(nd, 'questiontext')
            qtext.set('format',"moodle_auto_format")
            self.AppendElement(qtext, 'text', enunciado)
            
            if self.tipo == 5:
                self.AppendElement(nd,'defaultgrade', value = "1.0")
                self.AppendElement(nd,'penalty', value = "1.0")
            
            # Indica que se barajan las respuestas
            self.AppendElement(nd, "shuffleanswers", value = "1")

            # Indica si hay una sola respuesta o varias
            if self.tipo == 5:
                self.AppendElement(nd, "single", value = "false")
            else:
                self.AppendElement(nd, "single", value = "true")
            
            # Tipo de numeración
            self.AppendElement(nd, "answernumbering", value = "abc")
            
            # Indica que no se muestre la instrucción por defecto "seleccione una:"
            self.AppendElement(nd, "showstandardinstruction", value = "0")
            
            # Se agregan las opciones
            
            # Se obtienen los puntos asociados a cada respuesta
            if puntos == None:
                if self.tipo == 5:
                    raise Exception('Para múltiples respuestas se debe dar '+
                    'la puntuación de cada respuesta')
                puntos = [ 0 ]* len(respuestas)
                # La primera opción siempre es la correcta
                puntos[0] = 100
            
            if len(puntos) != len(respuestas):
                raise Exception("Los puntos no coinciden con las respuestas:"+
                f'\n  puntos:{len(puntos)}\n'+
                f'\n  respuestas:{len(respuestas)}\n'
                )
            
            
            if self.tipo == 5:
                total = sum([v for v in puntos if v>0])
                if abs( total - 100) > 0.00015 :
                    raise Exception(f'Los puntos no suman 100, suman: {total}')
                for vr in puntos:
                    v = abs(vr)
                    if isinstance(v,int):
                        venteros = (0,5,10,20,25,30,40, 50, 60, 70, 75,80,90,100)
                        if v not in venteros:
                            raise Exception(" La puntuacion debe ser un entero"+
                            " válido de:"+str(venteros))
                    if isinstance(v,float):
                        vfloats = (11.11111, 12.5, 14.28571, 
                        16.66667, 33.33333, 66.66667, 83.33333 )
                        existe = False
                        for vv in vfloats:
                            if abs(v - vv)<0.0001:
                                existe = True
                                break
                        if not existe:
                            raise Exception(" La puntuacion flotante estar"+
                            " en:"+str(vfloats))
            
            
            for i, rta in enumerate(respuestas):
                ri = ET.SubElement(nd, 'answer')
                ri.set('fraction',  str(puntos[i]))
                self.AppendElement(ri, 'text',  rta)
                if feedback:
                    f = ET.SubElement(ri, 'feedback')
                    self.AppendElement(f, 'text',  feedback[i])

            
            
            # valida que no hayan respuestas repetidas
            unicos = []
            for i, r in enumerate(respuestas):
                if r not in unicos:
                    unicos.append(r)
                else:
                    se = "La opción %i repetida:\n    %s"%(i+1, enunciado)
                    se += "\n    en: "+str(respuestas)
                    raise Exception(se)
            
        elif self.tipo == 1: #completar
            # Completar
            if  self.nArgsC != 1:
                raise Exception("No se halló la ubicación a completar")
            
            # parte el enunciado según la respuesta corta
            
            enA, enB = enunciado.split("@c1")
            enA = enA.strip()
            enB = enB.strip()
            
            enA += " _____ "+enB
                
                
            qtext = self.AppendElement(nd, "questiontext", 
                attribute = {"format":"moodle_auto_format"} )
            self.AppendElement(qtext,'text', value=enA)
            
            # Especifica no distinguir de mayúsculas y minúsculas en la respuesta
            self.AppendElement(nd,'usecase',value="0")
            for rta in respuestas:
                rtaElement = self.AppendElement(nd, "answer", 
                    attribute={"fraction":"100", "format":"moodle_auto_format"})
                self.AppendElement(rtaElement, "text", value = rta)
            
            
        
        elif self.tipo == 2: #emparejar
            # Se indica el enunciado
            qtext = ET.SubElement(nd, 'questiontext')
            qtext.set('format',"moodle_auto_format")
            self.AppendElement(qtext, 'text', enunciado)
            
            # Indica que se barajan las respuestas
            self.AppendElement(nd, "shuffleanswers", value = "1")
            
            for a,b in respuestas:
                subquestion = self.AppendElement(nd, "subquestion", 
                    attribute={'format': 'moodle_auto_format'})
                self.AppendElement(subquestion,'text', a)
                answ = self.AppendElement(subquestion,'answer')
                self.AppendElement(answ, 'text', b)
                
            
        elif self.tipo == 3: #verdadero falso
            if respuestas[0] not in 'TF':
                raise Exception('La respuesta debe ser True o False')
            qtext = self.AppendElement(nd, "questiontext", 
                attribute = {"format":"moodle_auto_format"} )
            self.AppendElement(qtext,'text', value=enunciado)
            
            rtas =[]
            if respuestas[0] == 'T':
                rtas.append( ('100','true') )
                rtas.append( ('0','false') )
            else:
                rtas.append( ('0','true') )
                rtas.append( ('100','false') )
            for f , v in rtas:
                rtaElement = self.AppendElement(nd, "answer", 
                    attribute={"fraction":f, "format":"moodle_auto_format"})
                self.AppendElement(rtaElement, "text", value =  v)
        elif self.tipo == 6: # Cloze
            qtext = self.AppendElement(nd, "questiontext", 
                attribute = {"format":"html"} )
            #self.AppendElement(qtext,'text', value=self.clozeContent(enunciado))
            self.AppendElement(qtext,'text', value=enunciado)
        ## Transforma el elemento en texto
        return ET.tostring( nd, encoding = "unicode")
    
    def clozeContent(self, enunciado):
        '''
        Ajusta el enunciado de las preguntas tipo cloze para agregar al 
        formato html
        '''
        return "<![CDATA[ "+enunciado+" ]]"

    

