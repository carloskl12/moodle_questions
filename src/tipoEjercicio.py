from src import EjercicioXML, TIPOS, Administrador
#from sympy import symbols, factor, cancel, latex
#from math import sin, cos, pi, tan

from random import choice, randint, shuffle
from itertools import product, combinations, permutations
from fractions import Fraction
from jkpyUtils.math import Polinomio, linspace

from src.html import Plot, Function

def preguntaGraficaMR( plot, respuestas, nombre_preg ):
    """
    Genérico para analizar una gráfica
    """ 
    enunciado = plot.canvas()
    enunciado += "<p> De acuerdo a la gráfica de la función \( f \) "
    enunciado += " se puede decir que:<p>"
    
    correctas , incorrectas = respuestas
    
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
        
        p={'variante':[],'respuesta':rtas , 'puntos':puntos}
        #print( len(rtas) )
        preguntas.append(p)
    preguntas= EjercicioXML(enunciado, preguntas,nombre_preg,
    TIPOS['múltiples respuestas'])
    #print("******* preguntas",len(preguntas))
    return preguntas
