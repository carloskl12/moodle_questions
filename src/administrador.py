

class Administrador(object):
    '''
    Clase para administrar la información de las preguntas
    '''
    
    def __init__(self,preguntas=True,posibilidades=True, categorias=True):
        '''
        preguntas: indica si se muestra el total de preguntas que se 
        van generando
        posibilidades: indica si se muestra el total de preguntas que es 
        posible generar en todas sus categorías
        '''
        self.preguntas=preguntas
        self.posibilidades=posibilidades
        self.categorias=categorias
        
        # Lista que almacena los tipos de las categorías o tipos
        # con sus respectivas preguntas que se pueden generar
        self.ltCategorias=[]
        # número de preguntas generadas
        self.nPreguntas=0
        # número de preguntas máximas que se pueden generar
        self.nPosibles=0
        # Cadena del resultado que se va generando
        self.s=""
        


    def CreaCategoria(self,categoria):
        '''
        Crea una categoría
        '''
        if len(self.ltCategorias)>0 :
            # Muestra el total de preguntas en la categoría anterior
            categoria , total, posibilidades = self.ltCategorias[-1]
            self.nPreguntas+=total
            self.nPosibles+=posibilidades
            if self.categorias:
                print('  Total de preguntas en la categoría "%s":'%categoria, total)
        
        
        self.s+="\n$CATEGORY: %s\n"%categoria
        # Almacena en la lista la categoría en la forma nombre, número de preguntas
        # generadas, y número máximo de preguntas diferentes que se pueden generar
        self.ltCategorias.append([categoria,0,0])
        
    
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
        
        categoria , totalPrevias, posibilidades = self.ltCategorias[-1]
        offsetIndice=self.nPreguntas+totalPrevias
        
        self.s+=ejercicio(opciones, total,offsetIndice)
        
        maxNumPreguntas=len( ejercicio.preguntas)
        if total == -1:
            total= maxNumPreguntas
        
        self.ltCategorias[-1][1]+=total
        self.ltCategorias[-1][2]+=maxNumPreguntas
        if self.posibilidades:
            print('    Posibles preguntas "%s" :'%ejercicio.grupo, maxNumPreguntas)
        
        
    def Fin(self):
        '''
        Finaliza la creación de las preguntas, se utiliza para mostrar
        la información de la última categoría generada, así como también
        el total de preguntas si estas opciones se habilitaron
        '''
        if len(self.ltCategorias)>0 :
            # Muestra el total de preguntas en la categoría anterior
            categoria , total, posibilidades = self.ltCategorias[-1]
            self.nPreguntas+=total
            self.nPosibles+=posibilidades
            if self.categorias:
                print('    Total de preguntas en la categoría "%s":'%categoria, total)
                print('  Máximo número de preguntas:',self.nPosibles)
        
        if self.preguntas:
            print('  ** Total de preguntas generadas:',self.nPreguntas)
            
