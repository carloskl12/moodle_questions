
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
            self.tipo = ejercicio. tipo
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
        if  self.tipo in (0,1,2,4) and isinstance(s, (list, tuple)):
            return [self.CorrigeFormato(v) for v in s]
            
        if not isinstance(s,str):
            return str(s)
        sn = s.replace('{','\{')
        sn = sn.replace('}','\}')
        if self.formato == 'gift':
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
        elif self.tipo in (1,2,3,4): #completar
            for i in range(np):
                variante = self.preguntas[i]['variante']
                enunciado = self.Enunciado(variante)
                respuestas = self.preguntas[i]['respuesta'] # lista de opciones
                s += self.Respuesta(enunciado, respuestas,i)+'\n'

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
    def Respuesta(self,enunciado, respuestas, iPregunta):
        '''
        Ajusta el enunciado con las respuestas,
        donde la primera es la respuesta correcta,
        retorna un nodo de respuesta
        '''
        # Ajustes de texto
        #enunciado = self.AjusteFormatoParaTextoXML(enunciado)
        #respuestas = self.AjusteRespuestas(respuestas)
        
        TIPOS_XML = {
            0: "multichoice", 
            1: "shortanswer", 
            2: "matching", 
            3: "truefalse",
            4: "multichoice", 
        }
        
        nd = ET.Element('question')
        # Se asigna el tipo de pregunta
        nd.set('type',TIPOS_XML[self.tipo])
        
        # Crear el nombre basado en la categoría y el número de indice y offset
        nombre = ET.SubElement(nd, 'name')
        txtNombre = ET.SubElement(nombre,'text')
        txtNombre.text = '%s_%i'%(self.grupo,iPregunta+self.offsetIndice+1)
        
        if self.tipo in (0,4):
            
            # Se indica el enunciado
            qtext = ET.SubElement(nd, 'questiontext')
            qtext.set('format',"moodle_auto_format")
            self.AppendElement(qtext, 'text', enunciado)
            
            
            # Se agregan las opciones
            # la primera siempre es la correcta
            rOk = ET.SubElement(nd, 'answer')
            rOk.set('fraction',  "100")
            self.AppendElement(rOk, 'text',  respuestas[0])
            
            for rta in respuestas[1:]:
                ri = ET.SubElement(nd, 'answer')
                ri.set('fraction',  "0")
                self.AppendElement(ri, 'text',  rta)

            # Indica que se barajan las respuestas
            self.AppendElement(nd, "shuffleanswers", value = "1")

            # Indica que hay una sola respuesta
            self.AppendElement(nd, "single", value = "true")
            
            # Tipo de numeración
            self.AppendElement(nd, "answernumbering", value = "abc")
            
            # Indica que no se muestre la instrucción por defecto "seleccione una:"
            self.AppendElement(nd, "showstandardinstruction", value = "0")
            
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
            
        ## Transforma el elemento en texto
        return ET.tostring( nd, encoding = "unicode")
    
    

    

