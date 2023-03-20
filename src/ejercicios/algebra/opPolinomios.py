from src import Ejercicio, TIPOS, Administrador
from random import  randint, shuffle

from itertools import product, combinations, permutations

from jkpyUtils.math import Polinomio


def genPositivosNegativos(vInicial, vFinal):
    """
    Genera una lista de numeros enteros desde 
    vInicial hasta vFinal-1, y sus respectivas versiones
    negativas
    """
    if vInicial<0:
        raise Exception("El valor inicial debe ser mayor o igual que cero")
    
    if vInicial >= vFinal:
        raise Exception("El valor inicial debe ser menor al valor final")
    numeros = list(range(vInicial,vFinal))
    for v in numeros:
        if v != 0:
            numeros.append(-v)
    return numeros

def pSumaPolinomiosG2(var='x'):
    """
    Suma de polinomios de grado 2
    """
    enunciado = "Si \( P(%s) = @v1 \) , y \( Q(%s) = @v2 \)"%var
    enunciado += " el resultado de \( P(%s) + Q(%s)\)"%var
    enunciado += " es igual a:"
    
    coefA = genPositivosNegativos(1,12)
    coefB = genPositivosNegativos(0,12)
    coefC = genPositivosNegativos(1,12)
    
    coefPol = list( product(coefA,coefB,coefC) )
    
    shuffle(coefPol)
    
    coefEj=[]
    for i in range(0,len(coefPol,2):
        if i+1 >= len(coefPol):
            break
        polR = Polinomio( coefPol[i] , orden_usual = True , variable = var)
        polA = Polinomio( coefPol[i+1] , orden_usual = True , variable = var)
        polB = polR - polA
        rta = "\( %s \)"%str(polR)
        p={'variante':[str(polA), str(polB)], 'respuesta':rta}
        preguntas.append(p)
        
        
        
    preguntas = Ejercicio( enunciado, preguntas, 'suma polinomios g2', 
        TIPOS['selección múltiple'])
    return preguntas
    

