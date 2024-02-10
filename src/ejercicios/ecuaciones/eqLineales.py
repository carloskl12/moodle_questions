from src import EjercicioXML, TIPOS

from itertools import combinations
from random import shuffle, randint


from fractions import Fraction
from jkpyUtils.math import Polinomio, CombinacionLineal

def pConceptosSEL():
    enunciado="Dado el sistema de ecuaciones formado por @v1, @v2"
    enunciado+=" es conveniente utilizar el "
    enunciado+=" método de @v3 porque (escoger la opción más correcta):"
    
    universal_set = list(range(2,10))
    #universal_set += [-i for i in universal_set]
    shuffle(universal_set)
    conjuntos = list(combinations(universal_set, 4))
    shuffle(conjuntos)
    conjuntos = conjuntos[:70]
    
    preguntas = []
    for a,b,c,d in conjuntos:
        eq1 = "%ix+%iy=%i"%(a,b,c)
        eq2 = "%ix=y-%i"%(d,a+b)
        
        v3 = "sustitución"
        rOk="Se puede despejar fácilmente la variable y en la segunda ecuación"
        r2 = "Se puede despejar fácilmente la variable y en la primera ecuación"
        r3 = "Se puede despejar fácilmente la variable x en la primera ecuación"
        r4 = "Se puede despejar fácilmente la variable x en la segunda ecuación"
        p={ "variante":[eq1, eq2, v3], 'respuesta':[rOk,r2,r3,r4] }
        preguntas.append(p)
        
        eq1 = "%ix+%iy=%i"%(a,b,c)
        eq2 = "%ix=%iy-%i"%(a,d,a+b)
        v3 = "igualación"
        rOk="Se puede despejar fácilmente el término con x en las dos ecuaciones"
        r2 = "Se puede despejar fácilmente el término con y en las dos ecuaciones"
        r3 = "Se puede despejar fácilmente la variable x en la primera ecuación"
        r4 = "Se puede despejar fácilmente la variable y en la segunda ecuación"
        p={ "variante":[eq1, eq2, v3], 'respuesta':[rOk,r2,r3,r4] }
        preguntas.append(p)
        
        eq1 = "%ix+%iy=%i"%(a,b,c)
        eq2 = "%ix+%iy=%i"%(13,b*2,d)
        v3 = "reducción"
        rOk="%i es múltiplo de %i, es decir que es  fácil eliminar y"%(b*2,b)
        r2 = "%i no es múltiplo de 13, es decir que es fácil eliminar x"%(a)
        r3 = "%i es múltiplo de %i, es decir que es fácil eliminar x"%(b*2,b)
        r4 = "%i no es múltiplo de 13, es decir que es fácil eliminar y"%(a)
        p={ "variante":[eq1, eq2, v3], 'respuesta':[rOk,r2,r3,r4] }
        
        preguntas.append(p)
        
    preguntas = EjercicioXML( enunciado, preguntas, 'Conceptos SEL', 
        TIPOS['opciones específicas'])
    return preguntas

def pConceptosTipoSEL():
    enunciado = "Luego de algunos pasos para resolver un sistema de ecuaciones"
    enunciado+= " se llegó a la igualdad @v1, entonces se puede afirmar que"
    enunciado+= " el sistema de ecuaciones lineales:"

    universal_set = list(range(2,10))
    #universal_set += [-i for i in universal_set]
    shuffle(universal_set)
    conjuntos = list(combinations(universal_set, 4))
    shuffle(conjuntos)
    conjuntos = conjuntos[:]
    
    sI = "Es independiente"
    sD = "Es dependiente"
    sIn = "Es inconsistente"
    
    uS = "Tiene única solución para x, y"
    iS = "Tiene infinitas soluciones"
    nS = "No tiene solución"
    
    preguntas = []
    for a,b,c,d in conjuntos:
        v1 = "%ix+%i=%ix-%i"%(a,b,c,d)
        p={ "variante":[v1], 'respuesta':[sI,sD,sIn] }
        preguntas.append(p)
        
        p={ "variante":[v1], 'respuesta':[uS,iS,nS] }
        preguntas.append(p)
        
        v1 = "%ix+%i=%ix-%i"%(a,b,a,d)
        p={ "variante":[v1], 'respuesta':[sIn, sI,sD] }
        preguntas.append(p)
        
        p={ "variante":[v1], 'respuesta':[nS,uS,iS] }
        preguntas.append(p)
        
        v1 = "%ix-%i=%ix-%i"%(a,b,a,b)
        p={ "variante":[v1], 'respuesta':[sD,sIn, sI] }
        preguntas.append(p)
        
        p={ "variante":[v1], 'respuesta':[iS, nS, uS] }
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 'Conceptos tipos SEL', 
        TIPOS['opciones específicas'])
    return preguntas


def pEcuacionLin():
    enunciado = "Dada la ecuación @v1, el valor de @v2 es @c1"
    
    universal_set = list(range(2,10))
    #universal_set += [-i for i in universal_set]
    shuffle(universal_set)
    conjuntos = list(combinations(universal_set, 3))
    shuffle(conjuntos)
    
    variables=['x', 'y', 'w', 'z', 't', 'a']
    preguntas = []
    for a,b,c in conjuntos:
        shuffle(variables)
        x=variables[0]
        
        # -a*x+b= c*x-d
        #  entonces c*x+a*x-b = d
        xs = randint(3,10)
        d = c*xs + a*xs - b
        
        p1 = Polinomio([-a,b],variable=x,orden_usual=True)
        p2 = Polinomio([c,-d],variable=x,orden_usual=True)
        eq = '%s=%s'%(str(p1),str(p2))
        p = {'variante':[eq, x] , 'respuesta':[xs]}
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 'Ecuacion lineal', TIPOS['completar'])
    return preguntas


def pSELs():
    enunciado = '<p style="text-align: left;"> '
    enunciado +='Dadas las ecuaciones \( @v1 \), \( @v2 \), los valores solución son:</p>'
    enunciado += '<p style="text-align: left;">'
    enunciado += '\(x=\) {1:SHORTANSWER:=@v3}'
    enunciado += ' , \(y=\) {1:SHORTANSWER:=@v4}'
    enunciado += '</p>'
    

    universal_set = list(range(2,7))
    universal_set += [-i for i in universal_set]
    shuffle(universal_set)
    conjuntos = list(combinations(universal_set, 4))
    shuffle(conjuntos)
    
    preguntas = []
    
    for a,b,c,d in conjuntos:
        if Fraction(a,c) == Fraction(b,d):
            #print("Linealmente dependientes", (a,b,c,d))
            continue
        # a*x+b*y= e
        # c*x+d*y= f
        #  
        xs = randint(-8,8)
        ys = randint(-8,8)
        e = a*xs + b*ys
        f = c*xs + d*ys 
        
        c1 = CombinacionLineal([a,b],['x', 'y'])
        c2 = CombinacionLineal([c,d],['x', 'y'])
        eq1 = '%s=%i'%(str(c1),e)
        eq2 = '%s=%i'%(str(c2),f)
        # Se plantea la respuesta con y sin el espacio en blanco
        p = {'variante':[eq1, eq2, xs,ys] }
        preguntas.append(p)
    preguntas = EjercicioXML( enunciado, preguntas, 'SELs ', TIPOS['preguntas anidadas'])
    return preguntas

