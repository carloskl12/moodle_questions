from src import EjercicioXML, TIPOS

from random import  randint, shuffle
from itertools import product, combinations, permutations

def pHallaPorcentaje():
    
    
    enunciado = "De un grupo de @v1 estudiantes, el día de hoy se presentaron "
    enunciado += "a clases @v2. El porcentaje de estudiantes que asistieron es:"
    
    datos = [ ]
    
    for total in (20,30, 40,50, 60):
        for p in range(40,91):
            parte = (p*total)//100
            if parte * 100 == p * total:
                datos.append( (total, parte, p))
    
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, revisa que hayas identificado la parte y el total correctamente"
    shuffle( datos )
    preguntas = []
    for total, parte ,p in datos:
        shuffle(offset)
        rOk = str(p)+"%"
        r2 = str(p+offset[0])+"%"
        r3 = str(p+offset[1])+"%"
        r4 = str(p+offset[2])+"%"
        
        respuestai = [rOk, r2, r3, r4]
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[total, parte], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Cálculo simple 1", 
        TIPOS['opciones específicas'])
    return preguntas



def pHallaPorcentaje2():
    
    enunciado = "En un laboratorioa se trató a @v1 ratones con un medicamento "
    enunciado += " nuevo, luego de una semana se observó que "
    enunciado += " @v2 ratones presentaron una respuesta favorable. "
    enunciado += " El porcentaje de ratones en que el tratamiento tuvo éxito es:"
    
    datos = [ ]
    
    for total in (20,30, 40,50, 60):
        for p in range(40,91):
            parte = (p*total)//100
            if parte * 100 == p * total:
                datos.append( (total, parte, p))
    
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, revisa que hayas identificado la parte y el total correctamente"
    shuffle( datos )
    preguntas = []
    for total, parte ,p in datos:
        shuffle(offset)
        rOk = str(p)+"%"
        r2 = str(p+offset[0])+"%"
        r3 = str(p+offset[1])+"%"
        r4 = str(p+offset[2])+"%"
        
        respuestai = [rOk, r2, r3, r4]
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[total, parte], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Cálculo simple 2", 
        TIPOS['opciones específicas'])
    return preguntas

def pHallaPorcentaje3():
    
    enunciado = "Un parqueadero tiene capacidad para @v1 autos. "
    enunciado += " Si a esta hora hay disponibles @v2 cupos, el  "
    enunciado += " porcentaje de ocupación del parqueadero es:"

    datos = [ ]
    
    for total in (20,30, 40,50, 60):
        for p in range(40,91):
            parte = (p*total)//100
            if parte * 100 == p * total:
                datos.append( (total, parte, p))
    
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, revisa que hayas identificado la parte y el total correctamente"
    fbBad2 = "¡Lo siento!, el porcentaje se da sobre la ocupación y no la disponibilidad"
    shuffle( datos )
    preguntas = []
    for total, parte ,p in datos:
        shuffle(offset)
        
        rOk = str(100 -p)+"%"
        r2 = str(100 -p + offset[0] )+"%"
        r3 = str(p+offset[1])+"%"
        r4 = str(p)+"%"
        
        respuestai = [rOk, r2, r3, r4]
        if len( set(respuestai) ) != 4:
            continue
        feedbacki = [fbOk, fbBad, fbBad, fbBad2]
        p={'variante':[total, parte], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Cálculo simple 3", 
        TIPOS['opciones específicas'])
    return preguntas

def pHallaPorcentaje4():
    
    enunciado = "En la receta de la mermelada interviene en su mayoría fruta y azucar. "
    enunciado += " Si se utilizan @v1 libras de fruta y @v2 libras de azucar,  "
    enunciado += "despreciando otros ingredientes, el porcentaje de fruta en la mermelada es:"

    datos = [ ]
    
    for total in (20,30, 40,50, 60):
        for p in range(40,91):
            parte = (p*total)//100
            if parte * 100 == p * total:
                datos.append( (total, parte, p))
    
    offset = [-1, -2, 1, 2]
    
    fbOk = "¡Correcto!"
    fbBad = "¡Lo siento!, recuerda que el total corresponde a la mermelada"
    
    shuffle( datos )
    preguntas = []
    for total, parte ,p in datos:
        shuffle(offset)
        
        rOk = str(p)+"%"
        r2 = str(100 -p + offset[0] )+"%"
        r3 = str(p+offset[1])+"%"
        r4 = str(100-p)+"%"
        fruta = parte
        azucar = total - parte
        respuestai = [rOk, r2, r3, r4]
        if len( set(respuestai) ) != 4:
            continue
        feedbacki = [fbOk, fbBad, fbBad, fbBad]
        p={'variante':[fruta, azucar], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Cálculo simple 4", 
        TIPOS['opciones específicas'])
    return preguntas



