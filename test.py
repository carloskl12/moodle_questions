#import os
#import inspect #para los nombres de las funciones

from src import Ejercicio, TIPOS, Administrador
#from sympy import symbols, factor, cancel, latex
#from math import sin, cos, pi, tan

from random import  randint, shuffle
#from itertools import product, combinations, permutations
#from fractions import Fraction


def preguntaSumaFracciones():
    '''
    a/b+c/b
    a,b,c primos

    frac1=(a.f)/(b.f)
    frac2=c/b
    '''
    
    preguntas = []
    enunciado ='Si se requiere obtener el resultado de @v1 , para poderse operar,' 
    enunciado +=' la fracción @v2 puede simplificarse para:'
    primos = [2,3,5,7, 11, 13]
    factores = [2,3,4,5,6,7,8]

    for i, f in enumerate(factores):
        shuffle(primos)
        a = primos[0]
        b = primos[1]
        c = primos[2]
        
        frac1="\\frac{%i}{%i}"%(a*f,b*f)
        frac2="\\frac{%i}{%i}"%(c,b)
        op='+'
        if i%2 :
            op='-'
        var1 = "\( %s %s %s \)"%(frac1,op,frac2)
        if randint(0,1):
            var1 = "\( %s %s %s \)"%(frac2,op,frac1)
        var2='\( %s \)'%frac1
        
        p= { 'variante': [ var1, var2], 'respuesta':f}
        
        preguntas.append(p)
    
    preguntas = Ejercicio( enunciado, preguntas, 'Problema fracciones', TIPOS['selección múltiple'])
    return preguntas


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# la dirección relativa de este archivo

admin = Administrador()
admin.CreaCategoria('Test/ejemplo')
admin.Add( preguntaSumaFracciones() , total=3 )
admin.Add( preguntaSumaFracciones() )
admin.CreaCategoria( 'Test/ejemplo2')
admin.Add( preguntaSumaFracciones() )
admin.Add( preguntaSumaFracciones() )
admin.Fin()
    



