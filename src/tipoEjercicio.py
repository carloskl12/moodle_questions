from src import EjercicioXML, TIPOS, Administrador
#from sympy import symbols, factor, cancel, latex
#from math import sin, cos, pi, tan

from random import choice, randint, shuffle
from itertools import product, combinations, permutations
from fractions import Fraction
from jkpyUtils.math import Polinomio, linspace

from src.html import Plot, Function

def multiplesRespuestasUnEnunciado( enunciado , respuestas, nombre_preg , genEjercicio=True):
    """
    Función que permite generar preguntas de múltiple selección dado un 
    enunciado y varias oraciones que se agrupan en falsas y verdaderas.
    
    enunciado: enunciado del problema.
    respuestas: lista o tupla con dos listas que almacenan respuestas 
        correctas e incorrectas respectivamente, opcionalmente se puede agregar 
        variantes para el enunciado.
    nombre_preg: nombre de la pregunta
    genEjercicio: indica si se genera o no el ejercicio, si es false, se retorna
        únicamente la lista de preguntas
    """ 
    correctas, incorrectas = [], []
    variantes = []
    if len(respuestas) == 2:
        correctas , incorrectas = respuestas
    elif len(respuestas) == 3:
        correctas, incorrectas, variantes = respuestas
    
    correctas2 = list(combinations(correctas,2))
    correctas3 = list(combinations(correctas,3))
    incorrectas2 = list(combinations(incorrectas,2))
    incorrectas3 = list(combinations(incorrectas,3))
    
    
    respuestas23 = list(product(correctas2,incorrectas3))    
    respuestas32 = list(product(correctas3,incorrectas2))
    # Aplana cada grupo de respuestas y coloca la puntuación que suma 100
    posibilidades = []
    
    e3 = 33.33333 # Se considera la tercera parte
    for (a,b), (c,d,e) in respuestas23:
        rtas = (a,b,c,d,e)
        puntos = (50,50,-e3,-e3,-e3)
        posibilidades.append((rtas,puntos))
    
    for (a,b,c), (d,e) in respuestas32:
        rtas = (a,b,c,d,e)
        puntos = (e3,e3,e3,-50,-50)
        posibilidades.append((rtas,puntos))
    
    shuffle(posibilidades)
    
    preguntas = []
    for rtas, puntos in posibilidades:
        
        p={'variante':variantes,'respuesta':rtas , 'puntos':puntos}
        #print( len(rtas) )
        preguntas.append(p)
    
    if genEjercicio:
        preguntas = EjercicioXML(enunciado, preguntas,nombre_preg,
        TIPOS['múltiples respuestas'])
    return preguntas



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def emparejar( enunciadoP, valoresEmparejar , nombre_preg ):
    '''
    Genera un ejercicio de emparejar, pero lo que se empareja cambia 
    según la lista valores, en cada pregunta se colocan las respuestas en 
    forma aleatoria.
    
    valoresEmparejar es una lista con dos listas:
        * Los valores a emparejar
        * la lista de variantes
    
    '''
    # Obtiene el valor más alto de variantes y le suma uno para asignarlo
    # a la variante de la tabla
    ivar = len(valoresEmparejar[0][1])+1 
    
    espacio = '<span style="width: 2ex; display: inline-block; text-align: center;"> </span>'
    espacio2 = '<span style="width: 7ex; display: inline-block; text-align: center;"> </span>'
    enunciado = '<p style="text-align: left;">'
    enunciado += enunciadoP
    enunciado += '</p>'
    enunciado += '<table border="0">'
    enunciado += '  @v%i  '%ivar
    enunciado += '</table>'

    
    n  = len(valoresEmparejar[0][0])
    if n > 10:
        raise Exception("Demasiadas opciones para emparejar, máximo 10")
    
    
    letras = 'abcdefghij'
    
    opciones = '~'.join(letras[:n])
    
    
    # lista de las opciones
    p = list( range( n ) )
    preguntas = []
    for valores , variantes in valoresEmparejar:
        # Baraja el orden de las respuestas        
        shuffle(p)
        
        # ajusta la tabla
        tabla = ""
        for i, (f,df) in enumerate(valores):
            tabla += '<tr>'
            tabla += f"<td>({letras[i]})"+espacio+f +espacio2 + '</td>'
            # Obtiene el índice de la respuesta
            v = p[i]
            # Asigna la derivada respectiva
            df = valores[v][1]
            # Asigna la letra correspondiente a la respuesta
            r = letras[v]
            # Ajusta las opciones a mostrar
            op = opciones
            if r == 'a':
                op = '='+opciones
            else:
                op = op.replace('~'+r, '~='+r)
            
            tabla += "<td>{1:MULTICHOICE:%s}"%op+espacio+ df +'</td>'
            tabla += '</tr>'
        variantes.append(tabla)
         
        preguntas.append( {'variante':variantes } )
    preguntas = EjercicioXML( enunciado, preguntas, nombre_preg, 
        TIPOS['preguntas anidadas'])
    return preguntas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def emparejarSimple( enunciadoP, valores , nombre_preg , maxPreg = 20 ):
    '''
    Se utiliza este tipo de pregunta para preguntas de emparejamiento simple
    en donde se utilzan ecuaciones, ya que para las preguntas de emparejamiento
    de Moodle no se puede utilizar ecuaciones en las dos partes de una misma 
    pareja.
    
    valores: lista con las parejas
    
    '''
    
    n  = len(valores)
    if n > 10:
        raise Exception("Demaciadas opciones para emparejar, máximo 10")
    
    valoresEmparejar = [(valores, []) for i in range(20)]
    
    return emparejar( enunciadoP, valoresEmparejar , nombre_preg )




