from src import EjercicioXML, TIPOS


from random import  randint, shuffle
from itertools import product, combinations, permutations


def pHallaDescuento():
    
    
    enunciado = "Si un producto cuesta normalmente $@v1, y hoy está "
    enunciado += "  con un descuento de %@v2. El valor del producto es:"
    
    datos = [ ]
    precios = [ 200, 300, 400, 500, 600, 700, 800]
    for p in range(10,41):
        shuffle(precios)
        datos.append( (p, precios[0]) )
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, halla correctamente el valor del descuento para aplicarlo al precio normal"
    shuffle( datos )
    preguntas = []
    for p , precioNormal in datos:
        
        valorDescuento = p*precioNormal//100
        precioDescuento = precioNormal - valorDescuento
        
        
        shuffle(offset)
        rOk = "$"+str(precioDescuento)
        r2 = "$"+str(precioDescuento + offset[0])
        r3 = "$"+str(precioDescuento + offset[1])
        r4 = "$"+str(precioDescuento + offset[2])
        
        respuestai = [rOk, r2, r3, r4]
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[precioNormal, p], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Precio con descuento", 
        TIPOS['opciones específicas'])
    return preguntas


def pHallaDescuento2():
    
    
    enunciado = "Si un producto cuesta normalmente $@v1, y hoy se puede hallar en "
    enunciado += "  $@v2. El descuento es de:"
    
    datos = [ ]
    precios = [ 200, 300, 400, 500, 600, 700, 800]
    for p in range(10,41):
        shuffle(precios)
        datos.append( (p, precios[0]) )
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, revisa que hayas identificado la parte y el total correctamente"
    shuffle( datos )
    preguntas = []
    for p , precioNormal in datos:
        
        valorDescuento = p*precioNormal//100
        precioDescuento = precioNormal - valorDescuento
        
        
        shuffle(offset)
        rOk = str(p)+"%"
        r2 = str(p+offset[0])+"%"
        r3 = str(p+offset[1])+"%"
        r4 = str(p+offset[2])+"%"
        
        respuestai = [rOk, r2, r3, r4]
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[precioNormal, precioDescuento], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Porcentaje descuento", 
        TIPOS['opciones específicas'])
    return preguntas


def pHallaIncremento():
    
    
    enunciado = "Si un producto cuesta normalmente $@v1, y hoy "
    enunciado += "  su precio incrementó %@v2. El valor del producto es:"
    
    datos = [ ]
    precios = [ 200, 300, 400, 500, 600, 700, 800]
    for p in range(10,41):
        shuffle(precios)
        datos.append( (p, precios[0]) )
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, halla correctamente el valor del incremento para aplicarlo al precio normal"
    shuffle( datos )
    preguntas = []
    for p , precioNormal in datos:
        
        valorIncremento = p*precioNormal//100
        precioIncremento = precioNormal + valorIncremento
        
        
        shuffle(offset)
        rOk = "$"+str(precioIncremento)
        r2 = "$"+str(precioIncremento + offset[0])
        r3 = "$"+str(precioIncremento + offset[1])
        r4 = "$"+str(precioIncremento + offset[2])
        
        respuestai = [rOk, r2, r3, r4]
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[precioNormal, p], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Precio con incremento", 
        TIPOS['opciones específicas'])
    return preguntas

def pHallaIncremento2():
    
    
    enunciado = "Si un producto cuesta normalmente $@v1, y hoy "
    enunciado += "  su precio es de $@v2. El incremento es de:"
    
    datos = [ ]
    precios = [ 200, 300, 400, 500, 600, 700, 800]
    for p in range(10,41):
        shuffle(precios)
        datos.append( (p, precios[0]) )
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, identifica correctamente el precio normal y el valor de incremento"
    shuffle( datos )
    preguntas = []
    for p , precioNormal in datos:
        
        valorIncremento = p*precioNormal//100
        precioIncremento = precioNormal + valorIncremento
        
        
        shuffle(offset)
        rOk = str(p)+"%"
        r2 = str(p+offset[0])+"%"
        r3 = str(p+offset[1])+"%"
        r4 = str(p+offset[2])+"%"
        
        respuestai = [rOk, r2, r3, r4]
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[precioNormal, precioIncremento], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Porcentaje incremento", 
        TIPOS['opciones específicas'])
    return preguntas



