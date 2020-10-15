from random import choice, randint, shuffle

def creaCategoria(categoria):
  '''
  Del nombre dado retorna la declaración de una 
  categoría
  '''
  s="\n$CATEGORY: "+categoria
  s+='\n'
  return s
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def corrigeFormato( s):
  '''
  Ajusta el formato latex para que funcione sin problemas en moodle
  '''
  sn= s.replace('{','\{')
  sn=sn.replace('}','\}')
  sn=sn.replace('=','\=')
  return sn
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def creaEjercicio(enunciado, respuestas, categoria='ejercicio'):
  s='::%s::\n'%(categoria)
  # Selección múltiple con única respuesta
  s+=enunciado+'\n'
  s+='{\n'
  if isinstance(respuestas[0],str):
    respuestas=[corrigeFormato(rta) for rta in respuestas]
  s+='  =%s\n'%respuestas[0]
  for rta in respuestas[1:]:
    s+='  ~%s\n'%rta
  s+='}\n'


def creaEjercicioFV(enunciado,verdadero, categoria='ejercicio'):
  s='::%s::\n'%(categoria)
  s+=corrigeFormato(enunciado)
  if verdadero:
    s+='{T}\n'
  else:
    s+='{F}\n'
  return s

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def generaPol(grado, ordenado=False, nt=4):
  '''
  Genera un polinomio de un grado particular
  con coeficientes aleatorios, y términos
  ordenados o desordenados
  
  nt= número de términos del polinomio
  '''
  expo=list(range(grado+1))
  
  if len(expo) > nt:
    tmp= expo[:-1]
    shuffle(tmp)
    expo= [expo[-1]]+tmp[:nt-1]
  
  coef=[]
  for n in expo:
    coef.append(randint(2,9))
  coef+=[-c for c in coef]
  shuffle(coef)
  shuffle(expo)
  pol=''
  i=0
  for c, n in zip(coef,expo[:len(coef)]):
    if i== 0:
      pol=str(c)
    elif c>0:
      pol+='+'+str(c)
    else:
      pol+=str(c)
    if n>1:
      pol+=' x^{%i} '%n
    elif n==1:
      pol+=' x '
    elif n==0:
      pol+=' '
    i+=1
  return pol
