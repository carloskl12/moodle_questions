from src import EjercicioXML, TIPOS, Administrador
from random import  randint, shuffle
from itertools import permutations, product, combinations

def pSumaRestaFraccionesCD(num_min=1, num_max=20, den_min=2, den_max=9):
    """
    Suma-resta de fracciones con común denominador y 
    resultados del numerador irán desde v_min hasta vmax
    """
    numeradores=list(range(num_min,num_max+1))
    denominadores= list(range(den_min,den_max+1))
    
    # Genera valores de 2 a num_max/2 en una cantidad igual al número
    # de numeradores, este valor se utilizará para crear
    # los numeradores de la operación de suma o resta
    # para llegar al resultado dado por "numeradores"
    modV = num_max//2 -2;
    avalues = [(i%modV)+2 for i in range(len(numeradores))]
    
    shuffle(numeradores)
    shuffle(denominadores)
    shuffle(avalues)
    
    N_DEN= len(denominadores)
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for i, num in enumerate(numeradores):
        a , b = avalues[i], 0
        den = denominadores[i%N_DEN]
        if i%2 == 0:
            # suma 
            b = num - a
            s = "\( \\frac{%i}{%i} +\\frac{%i}{%i} \)"%(b,den,a,den)
            r3 = "\(\\frac{%i}{%i} \)"%(b-a,den)
        else:
            # resta
            b = num + a
            s = "\( \\frac{%i}{%i} -\\frac{%i}{%i} \)"%(b,den,a,den)
            r3 = "\(\\frac{%i}{%i} \)"%(b+a,den)
        
        rOk = "\(\\frac{%i}{%i} \)"%(num,den)
        r1 = "\(\\frac{%i}{%i} \)"%(num,den*2)
        r2 = "\(\\frac{%i}{%i} \)"%(num,den//2)
        
        p= { 'variante': [ s ], 'respuesta':[rOk, r1, r2, r3]}
        
        preguntas.append(p)
    # mezcla las preguntas por si no se toman todas
    # para que no queden las que tienen denominador de un solo número primo
    shuffle(preguntas)
    preguntas = EjercicioXML( enunciado, preguntas, 'suma - resta fracciones común denominador', 
        TIPOS['opciones específicas'])
    return preguntas


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pSumaRestaFraccionesSimplifica( max_num=20, max_v = 60):
    """
    Suma y resta de fracciones, donde se debe simplificar una fracción para 
    poder hallar el resultado.
    
    max_num: indica el valor máximo como resultado del numerador
    max_v: indica el valor más grande que puede aparecer en un numerador
    """
    
    
    # denominadores de la fracción irreducible
    primos = [2,3,5,7] 
    
    denA = {}
    for p in primos:
        numsA = []
        # Halla los numeradores que no son múltiplos de p
        for i in range(1,max_num+1):
            if i%p != 0:
                numsA.append(i)
        shuffle(numsA)
        numsB = numsA[:]
        shuffle(numsB)
        denA[p]={"numsA":numsA, "numsB":numsB }
    
    # Junta todas las posibles sumas
    pp=[]
    for p, v in denA.items():
        for na, nb in zip(v["numsA"], v["numsB"]):
            pp.append( (na,nb,p))
    
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    for na,nb,p in pp:
        valores=[]
        # Itera sobre los múltiplos del denominador
        for mul in range(2,8):
            
            if mul%2 == 0:
                #Suma na/p + mul*nb/mul*p
                r = na+nb
                
                op = "+"
            else:
                r = na - nb
                
                op = "-"
            valores.append( (na,nb,mul,p,op,r) )
        # Desordena para que no se asocie cual
        # fracción simplificar según el valor por el cual se amplifica
        shuffle(valores)
        i=0
        for na, nb, mul, den, op, r in valores:
            if i%2 == 0:
                # amplifica la primera fracción
                numA = na*mul
                denA = den*mul
                numB = nb
                denB = den
            else:
                numA = na
                denA = den
                numB = nb*mul
                denB = den*mul
            
            s = "\( \\frac{%i}{%i} %s \\frac{%i}{%i} \)"%(numA,denA,op,numB,denB)
            rOk = "\(\\frac{%i}{%i} \)"%(r,den)
            r1 =   "\(\\frac{%i}{%i} \)"%(numA+numB,den)
            r2 = "\(\\frac{%i}{%i} \)"%(r,den*mul)
            r3 = "\(\\frac{%i}{%i} \)"%(numA+numB,denA+denB)
            
            p= { 'variante': [ s ], 'respuesta':[rOk, r1, r2, r3]}
            
            # Valida si los números no son muy grandes
            if numA <= max_v and numB <= max_v:
                preguntas.append(p)
            i+=1
    preguntas = EjercicioXML( enunciado, preguntas, 
        'suma-resta simplifica', TIPOS['opciones específicas'])
    return preguntas
    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pSumaRestaFraccionesAmplifica( max_num=20, max_v = 60):
    """
    Suma y resta de fracciones, donde se debe simplificar una fracción para 
    poder hallar el resultado.
    
    max_num: indica el valor máximo como resultado del numerador
    max_v: indica el valor más grande que puede aparecer en un numerador
    """
    
    # Los pares van de la forma k,b  siendo la suma o resta a/kb + c/b
    pares= list( product([2,3,5,7],repeat=2) )
    
    coef = []
    for k,b in pares:
        
        
        for ai in range(2,max_num):
            if ai%k != 0:
                coef.append( ( ai, k, b, randint(2,9) )   )
    
    #print("Coef:",len(coef))
    shuffle(coef)
    
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    i=0
    for a, k, b, c in coef:
        valores=[]
        
        # a/kb + c/b = (a+kc)/kb
        
        if randint(0,1) == 0:
            numA = a
            denA = k*b
            
            opA = a #numerador ajustado a común denominador de la fracción A
            
            numB = c
            denB = b
            
            opB = k*c #numerador ajustado a común denominador de la fracción B
        else:
            numA = c
            denA = b
            
            opA = k*c #numerador ajustado a común denominador de la fracción A
            
            numB = a
            denB = k*b
        
            opB = a #numerador ajustado a común denominador de la fracción B
        
        if i%2 == 0:
            #Suma na/p + mul*nb/mul*p
            op = "+"
            numR = opA + opB
            numRx = numA+numB
        else:
            op = "-"
            numR = opA - opB
            numRx = numA - numB
        
        s = "\( \\frac{%i}{%i} %s \\frac{%i}{%i} \)"%(numA,denA,op,numB,denB)
        rOk = "\(\\frac{%i}{%i} \)"%(numR,k*b)
        r1 =   "\(\\frac{%i}{%i} \)"%(numRx,k*b)
        r2 = "\(\\frac{%i}{%i} \)"%(numR,b)
        r3 = "\(\\frac{%i}{%i} \)"%(numRx,b)
            
        p= { 'variante': [ s ], 'respuesta':[rOk, r1, r2, r3]}
        preguntas.append(p)
        i+=1
    preguntas = EjercicioXML( enunciado, preguntas, 
        'suma-resta amplifica', TIPOS['opciones específicas'])
    return preguntas


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pMulDivFracciones():
    """
    Multiplicación y división de fracciones
    """
    v1=list(range(2,10))
    fracs = list( combinations(v1,2) )
    operations = list( combinations( fracs[:20], 2 ) )
    shuffle(operations)
    
    
    
    preguntas = []
    enunciado ='El resultado de @v1 es:'
    i=0
    for f1, f2 in operations:
        a , b = f1
        c , d = f2
        
        if i%2 == 0:
            
            op = "\\times"
            numR = a*c
            denR = b*d
            
            numX = a*d
            denX = b*c
        else:
            op = "\\div"
            numR = a*d
            denR = b*c
            
            numX = a*c
            denX = b*d
            
            
        s = "\( \\frac{%i}{%i} %s \\frac{%i}{%i} \)"%(a,b,op,c,d)
        rOk = "\(\\frac{%i}{%i} \)"%(numR,denR)
        r1 =   "\(\\frac{%i}{%i} \)"%(numX,denX)
        p= { 'variante': [ s ], 'respuesta':[rOk, r1]}
        preguntas.append(p)
        i+=1
    
    preguntas = EjercicioXML( enunciado, preguntas, 
        'multiplica-divide', TIPOS['opciones específicas'])
    return preguntas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pAmplificaReduceFracciones(max_num=60):
    v = [2, 3, 5, 7]
    
    fracs = []
    for p in v:
        for i in range(2,11):
            if i%p != 0:
                fracs.append( (p,i) )
    
    pares=[]
    for a,b in fracs:
        
        for i in range(2,11):
            c = i*a
            d = i*b
            
            if c <= max_num and d<=max_num:
                pares.append( ((a,b), (c,d)))
    shuffle(pares)
    preguntas = []
    enunciado ='La fracción @v1 es equivalente a:'
    i=0
    for f1, f2 in pares:
        a , b = f1
        c , d = f2
        
        if i%2 == 0: #reduce
            tmp = a
            a = c
            c = tmp
            tmp = b
            b = d
            d = tmp
        s=  "\(\\frac{%i}{%i} \)"%(a,b)
        rOk = "\(\\frac{%i}{%i} \)"%(c,d)
        r1 =   "\(\\frac{%i}{%i} \)"%(d,c)
        p= { 'variante': [ s ], 'respuesta':[rOk, r1]}
        preguntas.append(p)
        i+=1
    preguntas = EjercicioXML( enunciado, preguntas, 
        'amplifica-reduce', TIPOS['opciones específicas'])
    return preguntas



