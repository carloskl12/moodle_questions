from src import EjercicioXML, TIPOS
from random import  randint, shuffle
from itertools import product 
def pSumaNaturales20():
    """
    Suma de números naturales cuyo resultado máximo es 20
    """
    numeroR=list(range(10,21))
    va = list(range(3,10))
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in coef:
        b = r-a #sumando 2
        s = f"{a}+{b}"
        
        otros = [ v for v in numeroR if v != r]
        shuffle(otros)
        rtas = [r]+otros[:3]
        p = { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'sumas naturales 20', TIPOS['opciones específicas'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pSumaNaturales40():
    """
    Suma de números naturales cuyo resultado máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a , r in coef:
        b = r - a #sumando 2
        s = f"{a}+{b}"
        
        otros = [ v for v in numeroR if v != r]
        shuffle(otros)
        rtas = [r]+otros[:3]
        
        p = { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'sumas naturales 40', TIPOS['opciones específicas'])
    return preguntas
    
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaNaturales20():
    """
    Resta de números naturales cuyo minuendo máximo es 20
    """
    numeroR = list(range(10,21))
    va = list(range(3,10))
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in coef:
        b=r-a #sumando 2
        s=f"{r}-{b}"
        
        otros = [ v for v in va if v != a]
        shuffle(otros)
        rtas = [a]+otros[:3]
        
        p= { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Resta naturales 20', TIPOS['opciones específicas'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaNaturales40():
    """
    Resta de números naturales cuyo minuendo máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    
    coef = list( product(va, numeroR) )
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for a, r in coef:
        b=r-a #sumando 2
        s=f"{r}-{b}"
        
        otros = [ v for v in va if v != a]
        shuffle(otros)
        rtas = [a]+otros[:3]
        
        p= { 'variante': [ s ], 'respuesta':rtas}
        
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Resta naturales 40', TIPOS['opciones específicas'])
    return preguntas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pProductoNaturales10(tablas):
    """
    Producto de números naturales  de 1 a 10
    """
    if isinstance(tablas, int):
        tablas = [tablas]
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    
    for factorA in tablas:
        for b in range(1,11):
            r = factorA*b
            
            s = "\( %i \\times %i \)"%(factorA,b)
            p= { 'variante': [ s ], 'respuesta':r}
            
            preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Producto naturales 10', TIPOS['selección múltiple'])
    return preguntas
    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pCocienteNaturales10(tablas):
    """
    Cociente de números naturales  de 1 a 10
    """
    if isinstance(tablas, int):
        tablas = [tablas]
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    
    for factorA in tablas:
        for b in range(1,11):
            r = factorA*b
            
            s = "\( %i \\div %i \)"%(r,factorA)
            p= { 'variante': [ s ], 'respuesta':b}
            
            preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 
        'Cociente naturales 10', TIPOS['selección múltiple'])
    return preguntas


