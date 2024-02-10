from src import EjercicioXML, TIPOS


from random import   shuffle
from itertools import product, combinations, permutations


feedbackTuple = (
    "¡Correcto!",
    "¡Lo siento!, revisa qué tipo de cantidades involucra la pregunta",
    "¡Lo siento!, revisa nuevamente el enunciado, en particular la pregunta",
    "¡Lo siento!, podrían ser estas cantidades, pero hay una mejor opción"
)


problemas=[
    ( "Un auto viaja a una velocidad constante de 60 km/h. ¿Cuántos kilómetros recorrerá en 3 horas?",( # Identifica cantidades
            ("Distancia y tiempo",0),
            ("Velocidad y tiempo",1),
            ("Velocidad y distancia",1),
            ("Distancia y autos",1),
        ),
        (# Identifica la ecuación
            ('x', 60, 3, 1 )
        ),
        ( # Resuelve la pregunta.
            ("En 3 horas recorrerá %s kilómetros", "180") 
        ),
    ),
    ("Si 5 trabajadores pueden construir una casa en 20 días, ¿cuántos días tomará construir 4 casas?",(
            ("Días y casas", 0),
            ("Trabajadores y casas", 1),
            ("Trabajadores y días", 1),
            ("Trabajadores y tiempo", 1),
        ),
        (
            ('x', 20,4,1)
        ),
        (
            ("Para construir 4 casas tomará %s días", "80")
        )
    ),
    ( "Si un paquete de 8 lápices cuesta $40, ¿cuánto costarán 12 lápices?",
        (
            ("Dinero y lápices", 0),
            ("Dinero y paquetes", 3),
            ("Paquetes y lápices", 2),
            ("Costo y dinero", 2),
        ),
        (
            ('x', 40, 12,8)
        ),
        (
            ("El costo de 12 lápices es $%s", "60")
        )
    ),
    ( "Una manguera llena una piscina en 6 horas. ¿Cuánto tiempo tomará llenar dos piscinas iguales?",
        (
            ("Piscinas y horas", 0),
            ("Piscinas y mangueras", 1),
            ("Horas y mangueras", 1),
            ("Tiempo y mangueras", 1),
        ),
        (
            ('x', 6, 2,1)
        ),
        (
            ("Para llenar dos piscinas iguales se tardarán %s horas", "12")
        )
        
    ),
    ("Un estudiante estudia 2 horas al día y avanza 10 páginas en su libro. ¿Cuántas páginas avanzará en 5 horas de estudio?",
        (
            ("Páginas y horas", 0),
            ("Páginas y libros", 1),
            ("Libros y horas", 1),
            ("Libros y tiempo", 1),
        ),
        (
            ('x', 10, 5, 2)
        ),
        (
            ("En 5 horas de estudio avanzará %s páginas", "25")
        )
    ),
    #%%%%% Rlación inversa
    ("Si 6 obreros tardan 12 días en construir una pared, ¿cuántos días tomará si solo trabajan 4 obreros?",
        (
            ("Días y obreros", 0),
            ("Días y paredes", 1),
            ("Obreros y paredes", 1),
            ("Paredes y tiempo", 1),
        ),
        (
            ('x', 6, 12, 4)
        ),
        (
            ("Si trabajan 4 obreros tomará %s días", "18")
        )
        
    ),
    ("Una impresora tarda 5 horas en imprimir 200 libros, ¿cuánto tiempo tardarán dos impresoras para realizar la misma tarea?",
        (
            ("Horas e impresoras", 0),
            ("Horas y libros", 1),
            ("Impresoras y libros", 1),
            ("Tiempo y libros", 1),
        ),
        (
            ('x', 1, 5,2)
        ),
        (
            ("Dos impresoras tardarán %s horas para realizar la misma tarea", "2.5")
        )
        
    ),
    ("Si un auto que va al 60 km/h tarda 2 horas en ir de A hasta B, ¿Cuánto tiempo tarda en el mismo recorrido si va a 80 km/h?",
        (
            ("Horas y velocidad", 0),
            ("Horas y distancia", 1),
            ("Distancia y velocidad", 1),
            ("Tiempo y distancia", 1),
        ),
        (
            ('x', 60,2,80)
        ),
        (
            ("Si el auto va a 80 km/h tardará %s horas", "1.5")
        )
    ),
    ("Una llave llena una piscina en 9 horas. Si quieres llenarla en 3 horas, ¿cuántas llaves iguales necesitarás?",
        (
            ("Llaves y horas", 0),
            ("Llaves y piscinas", 1),
            ("Horas y piscinas", 1),
            ("Tiempo y piscinas", 1),
        ),
        (
            ('x', 9, 1, 3)
        ),
        (
            ("Se necesitan %s llaves iguales", "3")
        )
        
    ),
    ("Un equipo de aseo con 3 personas limpia 12 habitaciones en 4 horas. ¿Cuánto tardarán en limpiar las mismas habitaciones tres equipos de aseo iguales?",
        (
            ("Horas y equipos", 0),
            ("Horas y habitaciones", 2),
            ("Horas y personas", 3),
            ("Equipos y habitaciones", 3),
        ),
        (
            ('x', 1, 4,3)
        ),
        (
            ("Tres equipos de aseo iguales tardarán %s horas aproximadamente.", "1.33")
        )
        
    ),
]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pIdentificaVariables():
    
    enunciado = "En el enunciado dado identifique las dos cantidades"
    enunciado += " con las que se puede crear la tabla de datos para"
    enunciado += " luego aplicar la respectiva regla de tres: @v1"
    
    
    # Ajusta los datos de los problemas
    datos = [ (v[0], v[1]) for v in problemas ]
    
    preguntas =[]
    for problema, rs in datos:
        
        respuestai = [ v[0] for v in rs]
        feedbacki = [ feedbackTuple[v[1]] for v in rs]
        p={'variante':[problema], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, "Cantidades", 
        TIPOS['opciones específicas'])
    return preguntas
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def pIdentificaRelacion():
    
    enunciado = "En el enunciado dado, identifique qué tipo"
    enunciado += " de regla de tres se debe aplicar"
    enunciado += " para resolver el interrogante: @v1"
    
    # Ajusta los datos de los problemas
    datos = [ (v[0], v[1]) for v in problemas ]
    
    preguntas =[]
    for problema, rs in datos:
        variables = rs[0][0].lower()
        rOk = "Regla de tres simple directa"
        r2 = "Regla de tres simple inversa"
        if len(preguntas) > 5:
            tmp = rOk
            rOk = r2
            r2 = tmp
        respuestai = [ rOk, r2 ]
        feedbacki = [ "¡Correcto!", "¡Lo siento!, revisa la relación entre las cantidades: "+variables]
        p={'variante':[problema], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
        
    #shuffle(preguntas)
    preguntas = EjercicioXML( enunciado, preguntas, "Relación", 
        TIPOS['opciones específicas'])
    return preguntas


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def getEq(var, den1, num2,den2):
    """
    Genera la ecuación correspondiente a:
    var/den1 = num2/den2
    """
    v = (var, str(den1), str(num2), str(den2))
    return "\( \\frac{%s}{%s} = \\frac{%s}{%s} \)"%v

def getSol(var, den1, num2, den2):
    """
    Calcula la solucíon de una ecuación
    var/den1 = num2/den2
    """
    return (den1*num2/den2)

def pIdentificaEq():
    
    enunciado = "En el enunciado dado, identifique la "
    enunciado += " ecuación que modela adecuadamente"
    enunciado += " la situación: @v1"
    
    preguntas =[]
    
    for i, problema in enumerate(problemas):
        
        rel = "directamente proporcionales"
        if i > 4:
            rel = "inversamente proporcionales"
        
        # general as ecuaciones de las opciones
        v1 = problema[2]
        v2 = ('x' , v1[3], v1[2], v1[1] )
        v3 = ('x' , v1[3]+1, v1[2], v1[1] +1 )
        v4 = ('x' , v1[1]+1, v1[2], v1[3] +1 )
        respuestai = [ getEq(*v) for v in (v1,v2,v3,v4) ]
        # valida unicidad
        verifica = [ getSol(*v) for v in (v1,v2,v3,v4) ]
        if len( set(verifica) ) != 4:
            raise Exception("Hay un error en las respuestas:"+str(respuestai))
        # Genera el feedback
        f = "¡Lo siento!, recuerda que las cantidades "+problema[1][0][0].lower()
        f += " son "+ rel
        
        f2 = "¡Lo siento!, verifica las cantidades utilizadas"
        feedbacki = [ '¡Correcto!', f, f2, f2]
        
        p={'variante':[problema[0]], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
        
    preguntas = EjercicioXML( enunciado, preguntas, "Ecuación", 
        TIPOS['opciones específicas'])
    return preguntas


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def convertir_a_string(valor):
    if valor.is_integer():
        return str(int(valor))
    else:
        return str(round(valor, 2))

def pResuelveProblema():
    
    enunciado = "@v1"
    
    preguntas =[]
    
    for i, problema in enumerate(problemas):
        
        rel = "directamente proporcionales"
        if i > 4:
            rel = "inversamente proporcionales"
        
        # general as ecuaciones de las opciones
        v1 = problema[2]
        v2 = ('x' , v1[3], v1[2], v1[1] )
        v3 = ('x' , v1[3]+1, v1[2], v1[1] +1 )
        v4 = ('x' , v1[1]+1, v1[2], v1[3] +1 )
        # valida unicidad
        respuestai = [ getSol(*v) for v in (v1,v2,v3,v4) ]
        if len( set(respuestai) ) != 4:
            raise Exception("Hay un error en las respuestas:"+str(respuestai))
        
        # Ajusta adecuadamente los valores de respuesta
        respuestai = [ convertir_a_string(v) for v in respuestai] #problemas[3][0]%
        
        respuestai = [problema[3][0]%v for v in respuestai]
        
        # Genera el feedback
        f = "¡Lo siento!, recuerda que las cantidades "+problema[1][0][0].lower()
        f += " son "+ rel
        
        f2 = "¡Lo siento!, verifica las cantidades utilizadas"
        feedbacki = [ '¡Correcto!', f, f2, f2]
        
        p={'variante':[problema[0]], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
        
    preguntas = EjercicioXML( enunciado, preguntas, "Problema", 
        TIPOS['opciones específicas'])
    return preguntas
