import os
import inspect 
from shutil import copyfile

# Se especifica el directorio o carpeta donde se guardarán los resultados
GIFT_DIR = "./gift"

from .ejercicio import Ejercicio, EjercicioXML
import xml.etree.ElementTree as ET

#%%%%%%%%%%%%%%%%%
class Administrador(object):
    '''
    Clase para administrar la información de las preguntas
    '''
    
    def __init__(self, formato='xml', preguntas=True,
        posibilidades=True, categorias=True ,media=False):
        '''
        preguntas: indica si se muestra el total de preguntas que se 
            van generando
        posibilidades: indica si se muestra el total de preguntas que es 
            posible generar en todas sus categorías
        categorias : indica si se imprimen las categorías
        media: indica si se agregarán recursos multimedia como imágenes,
            sonido, u otros recursos externos que se pueden agregar 
            dentro de las preguntas.
        '''
        if formato not in ('gift', 'xml'):
            raise Exception("Formato no válido")
        self.formato = formato
        self.preguntas = preguntas
        self.posibilidades = posibilidades #imprime el número de posibles preguntas
        self.categorias = categorias #indica si se muestran las categorías
        
        # Lista que almacena los tipos de las categorías o tipos
        # con sus respectivas preguntas que se pueden generar
        self.ltCategorias = []
        # número de preguntas generadas
        self.nPreguntas = 0
        # número de preguntas máximas que se pueden generar
        self.nPosibles = 0
        # Cadena del resultado que se va generando
        self.s=""
        
        if formato == "xml":
            self.s = '<?xml version="1.0" ?><quiz>'
            # Agrega el formato por defecto
            info = ET.Element('info')
            info.set('format', "moodle_auto_format")
            text = ET.SubElement(info,'text')
            self.s +='\n'+ET.tostring( info, encoding="unicode")
        
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Obtiene el nombre del archivo desde el que 
        # se invoca al Administrador
        
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        
        myPyName = os.path.basename(filename)
        myName = myPyName.replace('.py','')
        print('Nombre del proyecto:',myName)
        print('**Formato:',formato)
        self.nombre =  myName


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def CreaCategoria(self,categoria):
        '''
        Crea una categoría
        '''
        if len(self.ltCategorias)>0 :
            # Si existe una categoría anterior, se utiliza para 
            # actualizar el número total de preguntas, y el 
            # número total de posibles preguntas
            categoriaOld , total, posibilidades = self.ltCategorias[-1]
            self.nPreguntas += total
            self.nPosibles += posibilidades
            if self.categorias:
                # Muestra el total de preguntas en la categoría anterior
                print('  Total de preguntas en la categoría "%s":'%categoriaOld, total)
        
        if self.formato == 'gift':
            self.s+="\n$CATEGORY: %s\n"%categoria
        elif self.formato == 'xml':
            nd = ET.Element('question')
            nd.set("type","category")
            ndCategory = ET.SubElement(nd,'category')
            txtCategory = ET.SubElement(ndCategory,'text')
            txtCategory.text = "$course$/top/"+categoria
            self.s+= ET.tostring(nd,encoding="unicode")
            
            
        # Almacena en la lista la categoría en la forma nombre, número de preguntas
        # generadas, y número máximo de preguntas diferentes que se pueden generar
        # al inicio se crean la categoría nada mas
        self.ltCategorias.append([categoria,0,0])
        
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def Add(self, ejercicio, opciones=6, total=-1 ):
        '''
        Agrega preguntas teniendo en cuenta el 
        ejercicio creado, del cual se generan 
        el número de preguntas dado por total 
        utilizando el número de opciones dado por 
        su respectivo parámetro.
        
        total: númeor de preguntas generadas, si es -1 indica que se toma 
            el valor máximo
        opciones: número de opciones si el tipo es de selección múltiple
        
        '''
        if len(self.ltCategorias) < 1:
            raise Exception("Se debe crear una categoría antes de agregar preguntas")
        
        # Se lee la categoría actual, el número de preguntas que se han
        # generado efectivamente y las posibles preguntas
        categoria , totalPrevias, posibilidades = self.ltCategorias[-1]
        offsetIndice = self.nPreguntas + totalPrevias
        
        if self.formato != ejercicio.formato:
            if self.formato == 'gift':
                ejercicio = Ejercicio(ejercicio=ejercicio)
                print("  Warning: Considere tener los ejercicios en el formato gift")
            elif self.formato == 'xml':
                ejercicio = EjercicioXML(ejercicio=ejercicio)
                print("  Warning: Considere tener los ejercicios en el formato xml")
        self.s += ejercicio(opciones, total, offsetIndice)
        
        maxNumPreguntas = len(ejercicio.preguntas)
        if total == -1 or total > maxNumPreguntas:
            total = maxNumPreguntas
        
        # actualiza el número de preguntas en la categoría actual
        self.ltCategorias[-1][1] += total
        self.ltCategorias[-1][2] += maxNumPreguntas
        if self.posibilidades:
            print('    Posibles preguntas "%s" :'%ejercicio.grupo, maxNumPreguntas)
        
    #%%%%%%%%%%%%    
    def Fin(self):
        '''
        Finaliza la creación de las preguntas, se utiliza para mostrar
        la información de la última categoría generada, así como también
        el total de preguntas si estas opciones se habilitaron
        
        Y se guarda los resultados en la carpeta gift
        '''
        if len(self.ltCategorias) > 0 :
            # Muestra el total de preguntas en la categoría anterior
            categoria , total, posibilidades = self.ltCategorias[-1]
            self.nPreguntas += total
            self.nPosibles += posibilidades
            if self.categorias:
                print('    Total de preguntas en la categoría "%s":'%categoria, total)
                print('  Máximo número de preguntas:',self.nPosibles)
        
        if self.preguntas:
            print('  ** Total de preguntas generadas:',self.nPreguntas)
        
        # Cierra el tag si está en formato xml
        if self.formato == 'xml':
            self.s+= "</quiz>"
        
        
        # Si no existe la carpeta para almacenar el resultado se
        # crea automáticamente
        if not os.path.exists(GIFT_DIR):
            os.mkdir(GIFT_DIR)
        
        dirSave = os.path.join(GIFT_DIR, self.nombre+'.'+self.formato)
        with open(dirSave,'w') as f:
            f.write(self.s)
    
    
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        
    def AgregarRecursoMultimedia(self, archivo , imagen = False, audio = False ):
            '''
            No válido, se mantiene por posibilidad de utilizarse luego
            
            Registra un archivo que se utilizará dentro de las preguntas, verifica su 
            tipo y genera el código del mismo para que se pueda agregar a las 
            preguntas.
            
            Las imágenes válidas pueden ser jpg, png y gif
            '''
            if not self.media :
                raise Exception("Para utilizar recursos multimedia "
                                +"debe declararlo al crear el administrador."
                                +"  Ej: admin = Administrador(media = True)")
            if not os.path.exists(archivo):
                raise Exception(f'El archivo "{archivo}" no se pudo hallar')
            
            
            basename = os.path.basename(archivo)
            # Verifica si ya se agregó el recurso antes
            if basename in self.dicRecursos:
                print("Ya se había agregado el recurso {basename} ")
                print("Recuerde que lo puede utilizar como admin.dicRecursos[{basename}]")
                return self.dicRecursos[basename]
            
            destino = os.path.join(self.projectDir,basename)
            copyfile(archivo, destino)
            
            # Genera la cadea de como se utiliza el recurso en una 
            # pregunta
            name , ext = os.path.splitext(basename)
            dicTipos = {'.jpg': 0, '.jpeg':0 , '.png':0, '.gif':0, '.mp3': 1}
            if ext.lower() not in dicTipos:
                raise Exception(f"El tipo de extension '{ext}' no es válido")
            s=''
            if dicTipos[ext] == 0:
                # Imagen
                s='<img style\="vertical-align: middle; margin: 10px;" '
                s+=' src\="@@PLUGINFILE@@/%s" alt\="%s" />'%(basename,name)
            elif dicTipos[ext] == 1:
                # Audio
                s= '<a href\="@@PLUGINFILE@@/%s">:</a>'%basename
            self.dicRecursos[basename] = s
            return s
