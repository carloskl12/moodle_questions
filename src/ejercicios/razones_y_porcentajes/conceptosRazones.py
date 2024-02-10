from src import EjercicioXML, TIPOS


from random import  shuffle
from itertools import product, combinations, permutations

def preguntaSelMultiple( nombreGrupo, enunciado, respuestasOk, 
    respuestasBad, barajar = True):
    """
    Genera un ejercicio de selección múltiple con única respuesta 
    con 4 opciones y retroalimentación.
    
    nombreGrupo: El nombre del grupo de preguntas que se utiliza 
    como prefijo en la numeración de cada una de las preguntas 
    generadas.
    
    enunciado: enunciado de la pregunta
    
    respuestasOk: lista con tuplas de respuestas correctas y 
    retroalimentación.
    
    respuestasBad: lista con tuplas de respuestas incorrectas y 
    retroalimentación
    
    barajar: indica si se debe barajar las preguntas o no
    """
    
    # Verifica que las listas de respuestas sean adecuadas
    if not  isinstance(respuestasOk, list) or not  isinstance(respuestasBad, list):
        raise Exception("Las respuestas deben ser listas.")
    
    if len(respuestasOk) < 1:
        raise Exception("Debe existir al menos una respuesta correcta.")
    
    if len(respuestasBad) < 3:
        raise Exception("Debe existir al menos tres respuestas incorrectas.")
    
    # Verifica los tipos de las respuestas
    for i, v in enumerate(respuestasOk):
        if not isinstance(v, tuple):
            raise Exception("Se requiere una tupla para presentar " +
            f"una respuesta y su feedback. Error en el elemento {i}.")
        
        if len(v) != 2:
            raise Exception("En las respuestas correctas las tuplas"+
            f"deben presentar respuesta y feedback. Error en el elemento {i}.")
        
        pass
    
    
    for i, v in enumerate(respuestasBad):
        if not isinstance(v, tuple):
            raise Exception("Se requiere una tupla para presentar " +
            f"una respuesta incorrecta y su feedback. Error en el elemento {i}.")
        
        if len(v) != 2:
            raise Exception("En las respuestas incorrectas las tuplas"+
            f"deben presentar respuesta y feedback. Error en el elemento {i}.")
        
        pass
    
    if barajar:
        shuffle(respuestasOk)
        shuffle(respuestasBad)
    # genera las posibles combinaciones de 3 opciones incorrectas
    rb = list(combinations(respuestasBad,3))
    
    
    # genera todas las 4 opciones de selección múltiple,
    # donde la primera opción corresponde a la respuesta correcta
    respuestas =list( product(respuestasOk, rb))
    
    if barajar:
        shuffle(respuestas)
    
    preguntas=[]
    for rCorrecta, rTernas in respuestas:
        respuestai = [rCorrecta[0]] + [v[0] for v in rTernas]
        feedbacki = [rCorrecta[1]] + [v[1] for v in rTernas]

        p={'variante':[], 'respuesta':respuestai, 'feedback':feedbacki }
        preguntas.append(p)
    
    preguntas = EjercicioXML( enunciado, preguntas, nombreGrupo, 
        TIPOS['opciones específicas'])
    return preguntas
    



def pConceptoRazón():
    enunciado = "En las siguientes opciones, escoger la respuesta que más "
    enunciado += "se ajusta al concepto matemático de razón:"
    
    # Lista de tuplas con respuestas correctas y su respectivo feedback
    respuestasOk = [
     ("La comparación entre dos cantidades mediante una fracción.",
     "¡Correcto!, una razón se puede representar como una fracción."),
     ("Dos cantidades comparadas cuantitativamente.",
     "¡Correcto!, una razón es una comparación de dos cantidades."),
     ("Una fracción que representa la comparación entre dos cantidades.",
     "¡Correcto!, una fracción es una forma de representar una razón."),
    ]
    
    # Lista de tuplas con respuestas incorrectas y su respectivo feedback
    respuestasBad = [
        ("La comparación entre cantidades relacionadas.",
        "¡Lo siento!, existen formas más precisas de definir una razón."),
        ("Dos cantidades comparadas cualitativamente.",
        "¡Lo siento!, en matemáticas es común que las expresiones "
        +"no sean cualitativas."),
        ("Una fracción que compara cualitativamente dos cantidades.",
        "¡Lo siento!, una fracción no es una forma cualitativa "
        +"de representar relaciones."),
        ("Un número entero que representa una comparación de dos cantidades.",
        "¡Lo siento!, no todas las razones corresponden a un número entero."),
        ("La igualdad entre dos cantidades relacionadas.",
        "¡Lo siento!, la igualdad no se utiliza para representar una razón."),
    ]
    
    nombreGrupo = "razón"
    return preguntaSelMultiple(nombreGrupo, enunciado, respuestasOk, respuestasBad)
    


def pConceptoProporcion():
    enunciado = "En las siguientes opciones, escoger la respuesta que más "
    enunciado += "se ajusta al concepto matemático de proporción:"
    
    respuestasOk = [
        ("La relación cuantitativa entre dos razones expresada como una igualdad.",
         "¡Correcto!, una proporción es una relación cuantitativa representada como una igualdad."),
        ("La igualdad de dos cocientes entre cantidades.",
         "¡Correcto!, en proporciones, los cocientes entre cantidades son iguales."),
        ("La comparación de dos razones utilizando la igualdad.",
         "¡Correcto!, una proporción es una igualdad de dos razones."),
    ]
    
    respuestasBad = [
        ("La comparación entre cantidades relacionadas.",
         "¡Lo siento!, aunque las proporciones involucran comparación, esta definición no es suficientemente específica."),
        ("Dos cantidades comparadas cualitativamente.",
         "¡Lo siento!, en matemáticas es común que las expresiones no representen comparaciones cualitativas."),
        ("Una igualdad que compara cualitativamente dos cantidades.",
         "¡Lo siento!, una proporción se basa en comparaciones cuantitativas, no cualitativas."),
        ("Una fracción que representa una relación entre dos cantidades.",
         "¡Lo siento!, las proporciones son representadas por igualdades."),
        ("El cociente entre dos cantidades relacionadas.",
         "¡Lo siento!, las proporciones son representadas por igualdades."),
    ]
    
    nombreGrupo = "proporción"
    return preguntaSelMultiple(nombreGrupo, enunciado, respuestasOk, respuestasBad)
    

# Relación directamente proporcional
def pConceptoRDP():
    enunciado = "En las siguientes opciones, escoger la respuesta que más "
    enunciado += "se ajusta al concepto matemático de una relación directamente proporcional:"
    
    respuestasOk = [
        ("Una relación de dos cantidades, en las que si una aumenta la otra"+
        " también aumenta en la misma proporción.",
        "¡Correcto!, en una relación directamente proporcional, si una cantidad aumenta, la otra también lo hace proporcionalmente."),
        ("Una relación de dos cantidades, en las que si una disminuye la otra"+
        " también disminuye en la misma proporción.",
        "¡Correcto!, en una relación directamente proporcional, si una cantidad disminuye, la otra también lo hace proporcionalmente."),
        
        ("Una relación de dos cantidades que se puede plantear de la forma \(y=kx\).",
        "¡Correcto!, una relación directamente proporcional se puede plantear"+ 
        " como una ecuación lineal que pasa por el origen y pendiente positiva."),
    ]
    
    respuestasBad = [
        ("Una relación donde las cantidades son independientes entre sí.",
        "¡Lo siento!, en una relación directamente proporcional, las cantidades están relacionadas y se afectan entre sí."),
        ("Cuando dos cantidades son iguales.",
        "¡Lo siento!, una relación directamente proporcional no siempre implica que las cantidades sean iguales."),
        ("Una relación entre cantidades que aumentan y disminuyen en proporciones diferentes.",
        "¡Lo siento!, en una relación directamente proporcional, las cantidades aumentan o disminuyen en la misma proporción."),
        ("Una relación donde las cantidades varían aleatoriamente.",
        "¡Lo siento!, en una relación directamente proporcional, las cantidades varían de manera constante y predecible."),
        ("Un número entero que representa una comparación de dos cantidades.",
        "¡Lo siento!, esta definición se ajusta más al concepto de razón."),
    ]
    
    nombreGrupo = "RDP"
    return preguntaSelMultiple(nombreGrupo, enunciado, respuestasOk, respuestasBad)
    


# Relación inversamente proporcional
def pConceptoRIP():
    enunciado = "En las siguientes opciones, escoger la respuesta que más "
    enunciado += "se ajusta al concepto matemático de una relación inversamente proporcional:"
    
    respuestasOk = [
        ("Una relación de dos cantidades proporcionales, en las que si una "+
        "aumenta la otra disminuye.",
        "¡Correcto!, y además se debe cumplir que el producto de las dos cantidades es constante."),
        ("Una relación de dos cantidades proporcionales, en las que si una "+
        "disminuye la otra aumenta.",
        "¡Correcto!, y además se debe cumplir que el producto de las dos cantidades es constante."),
        
        ("Una relación de dos cantidades que se puede plantear de la forma \(y=k/x\).",
        "¡Correcto!, en una relación inversamente proporcional el producto de las dos cantidades relacionadas es constante."),
    ]
    
    respuestasBad = [
        ("Una relación donde las cantidades son independientes entre sí.",
        "¡Lo siento!, en una relación directamente proporcional, las cantidades están relacionadas y se afectan entre sí."),
        ("Cuando dos cantidades son iguales.",
        "¡Lo siento!, una relación directamente proporcional no siempre implica que las cantidades sean iguales."),
        ("Una relación entre cantidades que aumentan y disminuyen en proporciones diferentes.",
        "¡Lo siento!, en una relación directamente proporcional, las cantidades aumentan o disminuyen en la misma proporción."),
        ("Una relación donde las cantidades varían aleatoriamente.",
        "¡Lo siento!, en una relación inversamente proporcional el producto de las dos cantidades relacionadas es constante."),
        ("Una fracción que representa una comparación de dos cantidades.",
        "¡Lo siento!, esta definición se ajusta más al concepto de razón."),
    ]
    
    nombreGrupo = "RIP"
    return preguntaSelMultiple(nombreGrupo, enunciado, respuestasOk, respuestasBad)
    









