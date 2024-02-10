from src import EjercicioXML, TIPOS


from random import  randint, shuffle
from itertools import product, combinations, permutations
from math import sin, cos, pi, tan

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pRazonesTrigo():
    '''
    conceptos de ángulo suplementarios
    '''
    enunciado  = "Dado un \( \\Delta @v1 \), con ángulo recto en el "
    enunciado += " el vértice @v2, si \( m \\angle @v3^\circ\) ,  y"
    enunciado += " el lado \( @v4 \) , para hallar el lado \( @v5 \) "
    enunciado += " se puede plantear la ecuación:"
    
    vertices=list('ABCDEFG')
    triangulos = list(combinations(vertices,3))
    
    shuffle(triangulos)
    
    angulos = list(range(10,70,10))
    
    preguntas=[]
    for t in triangulos:
        A,B,C = t
        
        a = A.lower()
        b = B.lower()
        c = C.lower()
        
        # Se da un ángulo y un lado
        shuffle(angulos)
        ang = angulos[0]
        lado = randint(4,10)
        
        # Triángulo, vertice 90, angulo, lado conocido, lado a hallar
        variante=[A+B+C, C, "%s=%i"%(A,ang), "%s=%i"%(a,lado), b]
        
        rOk = "\( \\tan(%i) = \\frac{%i}{%s} \)"%(ang,lado,b)
        r2 = "\( \\tan(%i) = \\frac{%s}{%i} \)"%(ang,b,lado)
        r3 = "\( \\sin(%i) = \\frac{%i}{%s} \)"%(ang,lado,b)
        r4 = "\( \\sin(%i) = \\frac{%s}{%i} \)"%(ang,b,lado)
        
        p={'variante':variante, 'respuesta':[rOk, r2, r3, r4]}
        preguntas.append(p)
        
        # Triángulo, vertice 90, angulo, lado conocido, lado a hallar
        variante=[A+B+C, C, "%s=%i"%(A,ang), "%s=%i"%(b,lado), a]
        
        rOk = "\( \\tan(%i) = \\frac{%s}{%i} \)"%(ang,a,lado)
        r2 = "\( \\tan(%i) = \\frac{%i}{%s} \)"%(ang,lado,a)
        r3 = "\( \\sin(%i) = \\frac{%i}{%s} \)"%(ang,lado,a)
        r4 = "\( \\sin(%i) = \\frac{%s}{%i} \)"%(ang,a,lado)
        
        p={'variante':variante, 'respuesta':[rOk, r2, r3, r4]}
        preguntas.append(p)
        
        # Triángulo, vertice 90, angulo, lado conocido, lado a hallar
        variante=[A+B+C, C, "%s=%i"%(B,ang), "%s=%i"%(b,lado), c]
        
        rOk = "\( \\sin(%i) = \\frac{%i}{%s} \)"%(ang,lado,c)
        r2 = "\( \\sin(%i) = \\frac{%s}{%i} \)"%(ang,c,lado)
        r3 = "\( \\tan(%i) = \\frac{%i}{%s} \)"%(ang,lado,c)
        r4 = "\( \\tan(%i) = \\frac{%s}{%i} \)"%(ang,c,lado)
        
        p={'variante':variante, 'respuesta':[rOk, r2, r3, r4]}
        preguntas.append(p)
        
        # Triángulo, vertice 90, angulo, lado conocido, lado a hallar
        variante=[A+B+C, C, "%s=%i"%(B,ang), "%s=%i"%(c,lado), b]
        
        rOk = "\( \\sin(%i) = \\frac{%s}{%i} \)"%(ang,b,lado)
        r2 = "\( \\sin(%i) = \\frac{%i}{%s} \)"%(ang,lado,b)
        r3 = "\( \\tan(%i) = \\frac{%i}{%s} \)"%(ang,lado,b)
        r4 = "\( \\tan(%i) = \\frac{%s}{%i} \)"%(ang,b,lado)
        
        p={'variante':variante, 'respuesta':[rOk, r2, r3, r4]}
        preguntas.append(p)
        
        
        # Triángulo, vertice 90, angulo, lado conocido, lado a hallar
        variante=[A+B+C, C, "%s=%i"%(B,ang), "%s=%i"%(a,lado), c]
        
        rOk = "\( \\cos(%i) = \\frac{%i}{%s} \)"%(ang,lado,c)
        r2 = "\( \\cos(%i) = \\frac{%s}{%i} \)"%(ang,c,lado)
        r3 = "\( \\sin(%i) = \\frac{%i}{%s} \)"%(ang,lado,c)
        r4 = "\( \\sin(%i) = \\frac{%s}{%i} \)"%(ang,c,lado)
        
        p={'variante':variante, 'respuesta':[rOk, r2, r3, r4]}
        preguntas.append(p)
        
        # Triángulo, vertice 90, angulo, lado conocido, lado a hallar
        variante=[A+B+C, C, "%s=%i"%(B,ang), "%s=%i"%(c,lado), a]
        
        rOk = "\( \\cos(%i) = \\frac{%s}{%i} \)"%(ang,a,lado)
        r2 = "\( \\cos(%i) = \\frac{%i}{%s} \)"%(ang,lado,a)
        r3 = "\( \\sin(%i) = \\frac{%i}{%s} \)"%(ang,lado,a)
        r4 = "\( \\sin(%i) = \\frac{%s}{%i} \)"%(ang,a,lado)
        
        p={'variante':variante, 'respuesta':[rOk, r2, r3, r4]}
        preguntas.append(p)
        

    preguntas = EjercicioXML( enunciado, preguntas, 'Razones Trigo', 
        TIPOS['opciones específicas'])
    return preguntas



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pLeySenos():
    enunciado="Dado un \( \\Delta ABC \), si \( m \\angle A =@v1 ^\circ\), "
    enunciado+=" \( m \\angle B =@v2 ^\circ\), \( b=@v3 \) es correcto afirmar que  \( a \) mide :"
    
    # 
    datos=list(product(range(10,17),range(40,61,2)))
    avs=[]
    dts=[]

    shuffle(datos)
    for b, A in datos:
        B= A-20
        av= b*sin(pi*A/180.)/sin(pi*B/180.)
        av="%.2f"%av
        if not av in avs:
            #print('  * a=%isin(%i)/sin(%i)=%s'%(b,A,B,av))
            avs.append(av)
            dts.append((b,A,B))
        av= b*sin(pi*B/180.)/sin(pi*A/180.)
        av="%.2f"%av
        if not av in avs:
            avs.append(av)
            dts.append((b,B,A))
    preguntas=[]
    for d ,rta in zip(dts,avs):
        b,A,B=d
        p={'variante':[A,B,b], 'respuesta':rta}
        preguntas.append(p)

    preguntas= EjercicioXML(enunciado,preguntas,'Ley de Senos',0)
    return preguntas


def pLeyCosenos():
    enunciado="Dado un \( \\Delta ABC \), si \( m \\angle C =@v1 ^\circ\), "
    enunciado+=" \( a =@v2 \), \( b=@v3 \) es correcto afirmar que  \( c^2 \) mide :"
    #fracciones de pi
    datos=list(product(range(10,17),range(10,17),range(40,61,2)))
    avs=[]
    dts=[]
    #print(datos)
    shuffle(datos)
    for a,b, C in datos:
        av= a**2+b**2 - 2*a*b*cos(pi*C/180.)
        av="%.2f"%av
        if not av in avs:
            #print('  * a=%isin(%i)/sin(%i)=%s'%(b,A,B,av))
            avs.append(av)
            dts.append((a,b,C))
    
    preguntas=[]
    for d ,rta in zip(dts,avs):
        a,b,C=d
        p={'variante':[C,a,b], 'respuesta':rta}
        preguntas.append(p)
  
    preguntas= EjercicioXML(enunciado,preguntas,'Ley de cosenos',0)
    return preguntas



