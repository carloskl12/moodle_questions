import os
import inspect #para los nombres de las funciones

from src import Ejercicio, creaCategoria, TIPOS
#from sympy import symbols, factor, cancel, latex
from math import sin, cos, pi, tan

from random import choice, randint, shuffle
from itertools import product, combinations, permutations
from fractions import Fraction

numPreguntas=0


def preguntaSumaFracciones():
  '''
  a/b+c/d
  a,b,c primos
  
  frac1=(a.f)/(b.f)
  frac2=c/b
  
  '''
  global numPreguntas
  preguntas=[]
  enunciado='Si se requiere obtener el resultado de @v1 , para poderse operar,' 
  enunciado+=' la fracción @v2 puede simplificarse para:'
  primos=[2,3,5,7]
  factores=[2,3,4,5,6,7]

  for i, f in enumerate(factores):
    shuffle(primos)
    a=primos[0]
    b=primos[1]
    c=primos[2]
    
    frac1="\\frac{%i}{%i}"%(a*f,b*f)
    frac2="\\frac{%i}{%i}"%(c,b)
    op='+'
    if i%2:
      op='-'
    var1="\( %s %s %s \)"%(frac1,op,frac2)
    if randint(0,1):
      var1="\( %s %s %s \)"%(frac2,op,frac1)
    var2='\( %s \)'%frac1
    p={'variante':[var1,var2],'respuesta':f}
    preguntas.append(p)
  numPreguntas+=len(preguntas)
  print('  ',inspect.stack()[0][3], len(preguntas))
  preguntas= Ejercicio(enunciado, preguntas,'Problema fracciones',TIPOS['selección múltiple'])
  return preguntas


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# la dirección relativa de este archivo
myDir=os.path.dirname(__file__)
myPyName=os.path.basename(__file__)
myName=myPyName.replace('.py','')
print('mi nombre es:',myName)
dirSave=os.path.join('gift',myName+'.gift')
with open(dirSave, 'w') as f:
  s=''
  s+=creaCategoria('Parcial1/union')
  s+=preguntaSumaFracciones()()
  print('Numero de preguntas:',numPreguntas)
  f.write(s)


