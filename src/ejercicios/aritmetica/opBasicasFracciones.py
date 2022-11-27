from src import Ejercicio, TIPOS, Administrador
from random import  randint, shuffle

def pSumaRestaFraccionesCD():
    """
    Suma-resta de fracciones con común denominador 
    """
    numeroR=list(range(10,21))
    va = list(range(3,10))
    shuffle(numeroR)
    shuffle(va)
    signos =  [ 1, 1,-1,-1,-1,-1]
    signos2 = [-1,-1,-1,-1, 1, 1]
    aValues = [si*va[i] for i,si in enumerate(signos)]
    rValues = [si*numeroR[i] for i,si in enumerate(signos2)]
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for a, r in zip(aValues, rValues):
        b=r-a #sumando 2
        s="(%i)+(%i)"%(a,b)
        p= { 'variante': [ s ], 'respuesta':r}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'sumas enteros 20', TIPOS['selección múltiple'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pSumaEnteros40():
    """
    Suma de números naturales cuyo resultado máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    shuffle(numeroR)
    shuffle(va)
    signos =  [ 1, 1,-1,-1,-1,-1]
    signos2 = [-1,-1,-1,-1, 1, 1]
    aValues = [si*va[i] for i,si in enumerate(signos)]
    rValues = [si*numeroR[i] for i,si in enumerate(signos2)]
    
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for a, r in zip(aValues, rValues):
        b=r-a #sumando 2
        
        s="(%i)+(%i)"%(a,b)
        p= { 'variante': [ s ], 'respuesta': r}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'sumas naturales 40', TIPOS['selección múltiple'])
    return preguntas
    
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaEnteros20():
    """
    Resta de números naturales cuyo minuendo máximo es 20
    """
    numeroR=list(range(10,21))
    va = list(range(3,10))
    shuffle(numeroR)
    shuffle(va)
    signos =  [ 1, 1,-1,-1,-1,-1]
    signos2 = [-1,-1,-1,-1, 1, 1]
    aValues = [si*va[i] for i,si in enumerate(signos)]
    rValues = [si*numeroR[i] for i,si in enumerate(signos2)]
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in zip(aValues, rValues):
        b=r-a #sumando 2
        
        s = "(%i)-(%i)"%(r,b)
        p = { 'variante': [ s ], 'respuesta': a }
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Resta enteros 20', TIPOS['selección múltiple'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaEnteros40():
    """
    Resta de números naturales cuyo minuendo máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    shuffle(numeroR)
    shuffle(va)
    signos =  [ 1, 1,-1,-1,-1,-1]
    signos2 = [-1,-1,-1,-1, 1, 1]
    aValues = [si*va[i] for i,si in enumerate(signos)]
    rValues = [si*numeroR[i] for i,si in enumerate(signos2)]
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in zip(aValues, rValues):
        b = r-a #sumando 2
        s = "(%i)-(%i)"%( r, b)
        p = { 'variante': [ s ], 'respuesta': a }
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Resta enteros 40', TIPOS['selección múltiple'])
    return preguntas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pProductoEnteros10(factorA):
    """
    Producto de números naturales  de 1 a 10
    """
    signos = [-1]*10 + [1]*10
    shuffle(signos)
   
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for b, s1, s2 in zip( range(1,11), signos[:10], signos[10:]) :
        factorA*=s1
        b*= s2
        r = factorA*b
        
        s = "\( (%i) \\times (%i) \)"%(factorA,b)
        p= { 'variante': [ s ], 'respuesta':r}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Producto enteros 10', TIPOS['selección múltiple'])
    return preguntas
    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pCocienteEnteros10(factorA):
    """
    Cociente de números naturales  de 1 a 10
    """
    signos = [-1]*10 + [1]*10
    shuffle(signos)
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for b, s1, s2 in zip( range(1,11), signos[:10], signos[10:]) :
        factorA*=s1
        b*= s2
        r = factorA*b
        
        s = "\( (%i) \\div (%i) \)"%(r,factorA)
        p= { 'variante': [ s ], 'respuesta':b}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Cociente enteros 10', TIPOS['selección múltiple'])
    return preguntas


