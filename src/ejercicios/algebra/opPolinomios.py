from src import EjercicioXML, TIPOS, Administrador
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
    numeros += [ -v for v in numeros if v != 0]
    return numeros

def pSumaPolinomiosG2(var='x'):
    """
    Suma de polinomios de grado 2
    """
    enunciado = f"Si \( P({var}) = @v1 \) , y \( Q({var}) = @v2 \)"
    enunciado += f" el resultado de \( P({var}) + Q({var})\)"
    enunciado += " es igual a:"
    
    coefA = genPositivosNegativos(1,11)
    
    
    coefB = genPositivosNegativos(0,11)
    coefC = genPositivosNegativos(1,11)
    
    coefPol = list( product(coefA,coefB,coefC) )
    
    shuffle(coefPol)
    N = 200
    if len(coefPol) < N:
        N = len(coefPol)
    
    preguntas = []
    for i in range(0,N,2):
        if i+1 >= len(coefPol):
            break
        polR = Polinomio( coefPol[i] , orden_usual = True , variable = var)
        polA = Polinomio( coefPol[i+1] , orden_usual = True , variable = var)
        polB = polR - polA
        
        polR2 = polA - polB
        polR3 = polB - polA
        polR4 = Polinomio(polR)
        polR4.escalar(-1)
        rtas = [ "\( %s \)"%str(p) for p in (polR, polR2, polR3, polR4) ]
        p={'variante':[str(polA), str(polB)], 'respuesta':rtas}
        preguntas.append(p)
        
        
        
    preguntas = EjercicioXML( enunciado, preguntas, 'suma polinomios g2', 
        TIPOS['opciones específicas'])
    return preguntas


def pRestaPolinomiosG2(var='x'):
    """
    Suma de polinomios de grado 2
    """
    enunciado = f"Si \( P({var}) = @v1 \) , y \( Q({var}) = @v2 \)"
    enunciado += f" el resultado de \( P({var}) - Q({var})\)"
    enunciado += " es igual a:"
    
    coefA = genPositivosNegativos(1,11)
    
    
    coefB = genPositivosNegativos(0,11)
    coefC = genPositivosNegativos(1,11)
    
    coefPol = list( product(coefA,coefB,coefC) )
    
    shuffle(coefPol)
    N = 200
    if len(coefPol) < N:
        N = len(coefPol)
    
    preguntas = []
    for i in range(0,N,2):
        if i+1 >= len(coefPol):
            break
        polR = Polinomio( coefPol[i] , orden_usual = True , variable = var)
        polA = Polinomio( coefPol[i+1] , orden_usual = True , variable = var)
        polB = polR - polA
        
        polR2 = polA - polB
        polR3 = polB - polA
        polR4 = Polinomio(polR)
        polR4.escalar(-1)
        rtas = [ "\( %s \)"%str(p) for p in ( polR2, polR, polR3, polR4) ]
        p={'variante':[str(polA), str(polB)], 'respuesta':rtas}
        preguntas.append(p)
        
        
        
    preguntas = EjercicioXML( enunciado, preguntas, 'resta polinomios g2', 
        TIPOS['opciones específicas'])
    return preguntas


def pMultiplicaPol():
    universal_set = list(range(1,10))
    shuffle(universal_set)
    conjuntos = list(combinations(universal_set, 6))
    
    enunciado = "El resultado de \( @v1 \) es:"
    
    preguntas = []
    
    factores=[2,3,4,5]
    for vv in conjuntos:
        vv = list(vv)
        shuffle(vv)
        v1,v2,v3,v4,v5 = vv
        shuffle(factores)
        p1=Polinomio((1,v1), orden_usual=True)
        
        
        p = { "variante":[], 'respuesta':parejas}
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 'Repaso Fact', TIPOS['emparejar'])
    return preguntas


def pCasosFact():
    universal_set = list(range(1,10))
    shuffle(universal_set)
    conjuntos = list(combinations(universal_set, 5))
    
    enunciado = "Emparejar las expresiones con su forma factorizada:"
    
    preguntas = []
    
    factores=[2,3,4,5]
    for vv in conjuntos:
        vv = list(vv)
        shuffle(vv)
        v1,v2,v3,v4,v5 = vv
        shuffle(factores)
        p=Polinomio((1,v1), orden_usual=True)
        pB='%i(%s)'%(factores[0], str(p))
        p.escalar(factores[0])
        pA="\( %s \)"%str(p)
        
        parejas=[]
        parejas.append( (pA,pB) )
        
        #Trinomio cuadrado perfecto
        p1=Polinomio((1,v2), orden_usual=True)
        pA="\( %s \)"%str(p1*p1)
        pB="(%s)(%s)"%(str(p1),str(p1))
        parejas.append( (pA,pB) )
        
        # Trinomio 
        p1=Polinomio((1,v2), orden_usual=True)
        p2=Polinomio((1,v3), orden_usual=True)
        pA="\( %s \)"%str(p1*p2)
        pB="(%s)(%s)"%(str(p1),str(p2))
        parejas.append( (pA,pB) )
        
        # Diferencia de cuadrados
        p1=Polinomio((1,v4), orden_usual=True)
        p2=Polinomio((1,-v4), orden_usual=True)
        pA="\( %s \)"%str(p1*p2)
        pB="(%s)(%s)"%(str(p1),str(p2))
        parejas.append( (pA,pB) )
        
        p = { "variante":[], 'respuesta':parejas}
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 'Repaso Fact', TIPOS['emparejar'])
    return preguntas

