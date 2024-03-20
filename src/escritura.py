"""
Funciones o clases para dar formato a la forma en que el usuario escribe 
respuestas en los campos de rellenar
"""
from fractions import Fraction

def complex2String(c):
    """
    convierte un complejo a un string en formato tradicional a+bi
    """
    s = str(c)
    s = s[1:-1]
    s = s.replace('j','i')
    if c.imag == 1 :
        s = s.replace('1i', 'i')
    return s

def polLatex2String(p):
    """
    Convierte un polinomio que está en formato latex a cadena de texto 
    que puede ingresar el usuario
    """
    return str(p).replace('^', '**').replace('{', '').replace('}','')

def frac2String(num,den):
    '''
    Convierte una fracción a su formato en texto plano
    '''
    return str( Fraction(num,den) )



