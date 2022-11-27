from src import Ejercicio, TIPOS, Administrador
from random import  randint, shuffle

def pSumaNaturales20():
    """
    Suma de números naturales cuyo resultado máximo es 20
    """
    numeroR=list(range(10,21))
    va = list(range(3,10))
    shuffle(numeroR)
    shuffle(va)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for i in range(6):
        a=va[i] #sumando
        b=numeroR[i]-a #sumando 2
        r=numeroR[i] #resultado
        s="%i+%i"%(a,b)
        p= { 'variante': [ s ], 'respuesta':r}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'sumas naturales 20', TIPOS['selección múltiple'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pSumaNaturales40():
    """
    Suma de números naturales cuyo resultado máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    shuffle(numeroR)
    shuffle(va)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for i in range(6):
        a=va[i] #sumando
        b=numeroR[i]-a #sumando 2
        r=numeroR[i] #resultado
        s="%i+%i"%(a,b)
        p= { 'variante': [ s ], 'respuesta':r}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'sumas naturales 40', TIPOS['selección múltiple'])
    return preguntas
    
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaNaturales20():
    """
    Resta de números naturales cuyo minuendo máximo es 20
    """
    numeroR=list(range(10,21))
    va = list(range(3,10))
    shuffle(numeroR)
    shuffle(va)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for i in range(6):
        a=va[i] #sumando
        b=numeroR[i]-a #sumando 2
        r=numeroR[i] #resultado
        s="%i-%i"%(r,b)
        p= { 'variante': [ s ], 'respuesta':a}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Resta naturales 20', TIPOS['selección múltiple'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRestaNaturales40():
    """
    Resta de números naturales cuyo minuendo máximo es 40
    """
    numeroR=list(range(23,41))
    va = list(range(9,17))
    shuffle(numeroR)
    shuffle(va)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for i in range(6):
        a=va[i] #sumando
        b=numeroR[i]-a #sumando 2
        r=numeroR[i] #resultado
        s="%i-%i"%(r,b)
        p= { 'variante': [ s ], 'respuesta':a}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Resta naturales 40', TIPOS['selección múltiple'])
    return preguntas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pProductoNaturales10(factorA):
    """
    Producto de números naturales  de 1 a 10
    """
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for b in range(1,11):
        r = factorA*b
        
        s = "\( %i \\times %i \)"%(factorA,b)
        p= { 'variante': [ s ], 'respuesta':r}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Producto naturales 10', TIPOS['selección múltiple'])
    return preguntas
    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pCocienteNaturales10(factorA):
    """
    Cociente de números naturales  de 1 a 10
    """
    
    preguntas = []
    enunciado ='El resultado de @v1 es:' 
    for b in range(1,11):
        r = factorA*b
        
        s = "\( %i \\div %i \)"%(r,factorA)
        p= { 'variante': [ s ], 'respuesta':b}
        
        preguntas.append(p)
    preguntas = Ejercicio( enunciado, preguntas, 
        'Cociente naturales 10', TIPOS['selección múltiple'])
    return preguntas


