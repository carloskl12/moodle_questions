from src import EjercicioXML, TIPOS, Administrador
from random import  randint, shuffle
from itertools import product 

def pSumaEnteros20():
    """
    Suma de números enteros cuyo resultado está entre -20 y 20
    """
    numeroR = list(range(10,21))
    numeroR += [-v for v in numeroR]
    va = list(range(3,10))
    va += [-v for v in va]
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for a, r in coef:
        b=r-a #sumando 2
        s=f"({a})+({b})"
        
        otros = [ v for v in numeroR if v != r]
        shuffle(otros)
        rtas = [r]+otros[:3]
        p = { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'sumas enteros 20', TIPOS['opciones específicas'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pSumaEnteros40():
    """
    Suma de números naturales cuyo resultado máximo es 40
    """
    numeroR = list(range(23,41))
    va = list(range(9,17))
    numeroR += [-v for v in numeroR]
    va += [-v for v in va]
    
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for a, r in coef:
        b=r-a #sumando 2
        s=f"({a})+({b})"
        
        otros = [ v for v in numeroR if v != r]
        shuffle(otros)
        rtas = [r ]+otros[:3]
        p = { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'sumas enteros 40', TIPOS['opciones específicas'])
    return preguntas
    
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaEnteros20():
    """
    Resta de números naturales cuyo minuendo máximo es 20
    """
    numeroR=list(range(10,21))
    va = list(range(3,10))
    numeroR += [-v for v in numeroR]
    va += [-v for v in va]
    
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in coef:
        b=r-a #sumando 2
        
        s = f"({r})-({b})"
        
        otros = [ v for v in va if v != a]
        shuffle(otros)
        rtas = [a]+otros[:3]
        
        p= { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Resta enteros 20', TIPOS['opciones específicas'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaEnteros40():
    """
    Resta de números naturales cuyo minuendo máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    numeroR += [-v for v in numeroR]
    va += [-v for v in va]
    
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in coef:
        b=r-a #sumando 2
        
        s = f"({r})-({b})"
        
        otros = [ v for v in va if v != a]
        shuffle(otros)
        rtas = [a]+otros[:3]
        
        p= { 'variante': [ s ], 'respuesta':rtas}
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Resta enteros 40', TIPOS['opciones específicas'])
    return preguntas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pProductoEnteros10(tablas):
    """
    Producto de números naturales  de 1 a 10
    """
    if isinstance(tablas, int):
        tablas = [tablas]
    
    signos = [-1]*10 + [1]*10
    shuffle(signos)
   
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for factorA in tablas:
        for b, s1, s2 in zip( range(1,11), signos[:10], signos[10:]) :
            factorA*=s1
            b*= s2
            r = factorA*b
            
            s = "\( (%i) \\times (%i) \)"%(factorA,b)
            p= { 'variante': [ s ], 'respuesta':r}
            
            preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Producto enteros 10', TIPOS['selección múltiple'])
    return preguntas
    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pCocienteEnteros10(tablas):
    """
    Cociente de números naturales  de 1 a 10
    """
    if isinstance(tablas, int):
        tablas = [tablas]
    signos = [-1]*10 + [1]*10
    shuffle(signos)
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for factorA in tablas:
        for b, s1, s2 in zip( range(1,11), signos[:10], signos[10:]) :
            factorA*=s1
            b*= s2
            r = factorA*b
            
            s = "\( (%i) \\div (%i) \)"%(r,factorA)
            p= { 'variante': [ s ], 'respuesta':b}
            
            preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Cociente enteros 10', TIPOS['selección múltiple'])
    return preguntas


