import re
class Estilo_Java:
    CL_PALABRAS_CLAVE = '#770'
    CL_TIPOS_DATO = '#11A'
    CL_COMENTARIO = '#1A1'
    CL_LITERAL = '#A7A'
    CL_CODIGO = '#222'
    CL_FONDO = '#EEE'
    def __init__(self):
        '''
        Colores en formato html
            palabras_clave:'#...'
            tipos_dato:
            comentario:...
            literales: ...
            codigo:
        '''
        self.lenguaje = 'java'
        self.palabras_clave = [ 'abstract', 'assert', 'break', 'case', 'catch',
        'class', 'const', 'continue', 'default', 'do', 'else', 'enum',
        'extends', 'final', 'finally', 'for', 'goto', 'if', 'implements',
        'import', 'instanceof', 'interface', 'native', 'new', 'package',
        'private', 'protected', 'public', 'return', 'strictfp', 'super',
        'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try',
        'void', 'volatile', 'while', ]
        
        self.tipos_dato = [ 'boolean', 'byte', 'char', 'double', 'float', 'int',
                          'long', 'short', ]

    
    def __call__(self, palabra, tipo):
        '''
        Pasa un token y devuelve el formato en html
        '''
        if len(palabra) < 1:
            return ''
        
        dicTipos = {
          'comentario': self.CL_COMENTARIO,
          'palabra_clave':self.CL_PALABRAS_CLAVE,
          'tipos_dato': self.CL_TIPOS_DATO,
          'literal': self.CL_LITERAL,
          'identificador': self.CL_CODIGO,
          'espacio':self.CL_CODIGO,
          'salto_de_linea': self.CL_CODIGO,
          'operador': self.CL_CODIGO,
        }
        
        if tipo in ('codigo', 'operador', 'salto_de_linea', 'espacio', 'identificador'):
            valor = palabra 
            if valor == ' ':
                valor = '&nbsp;'
            return valor
        color = dicTipos.get(tipo, self.CL_CODIGO)
        return f'<span style="color:{color}">{palabra}</span>'


class TokenizadorJava:
    def __init__(self, estilo_java):
        self.estilo_java = estilo_java

    def tokenizar(self, codigo_java):
        # Definir patrones de expresiones regulares para cada tipo de token
        patrones = [
            (r'\/\/.*|\/\*.*?\*\/', 'comentario'),  # Comentarios
            (r'\b(?:' + '|'.join(map(re.escape, self.estilo_java.palabras_clave)) 
                + r')\b', 'palabra_clave'),  # Palabras clave y tipos de datos
            (r'\b(?:' + '|'.join(map(re.escape, self.estilo_java.tipos_dato)) + r')\b', 'tipos_dato'), 
            
            (r'\b(?:true|false|null)\b', 'literal'),  # Literales especiales
            (r'\s+', 'espacio'),  # Espacios en blanco
            (r'\s', 'espacio'),  # Espacios en blanco
            (r'\".*?\"|\'.*?\'', 'literal'),  # Cadenas y caracteres literales
            (r'\b(?:\d+\.\d*|\.\d+|\d+)\b', 'literal'),  # Números
            (r'\b\w+\b', 'identificador'),  # Identificadores (variables y nombres de funciones)
            (r'\n', 'salto_de_linea'),  # Saltos de línea
            (r'[\+\-\*/=\[\]\(\)\{\},;]', 'operador')  # Operadores y signos de puntuación
        ]

        tokens = []

        # Iterar sobre el código y aplicar los patrones
        posicion = 0
        while posicion < len(codigo_java):
            match = None
            for patron, tipo in patrones:
                regex = re.compile(patron)
                match = regex.match(codigo_java, posicion)
                if match:
                    valor = match.group()
                    posicion = match.end()
                    #valorbin = ' '.join( str(ord(c)) for c in valor)
                    #print("valor:", valor, valorbin )
                    tokens.append((valor, tipo))
                    
                    break

            if not match:
                # Si no se encuentra coincidencia, avanzar un carácter
                tokens.append((codigo_java[posicion], 'espacio'))
                #print( 'no hay match en:',codigo_java[posicion])
                posicion += 1

        return tokens

    def tokenizar_y_estilizar(self, codigo_java):
        tokens = self.tokenizar(codigo_java)
        codigo_formateado = f'<pre style="color:{self.estilo_java.CL_CODIGO}'
        codigo_formateado += f';background-color:{self.estilo_java.CL_FONDO}">'
        

        for token, tipo in tokens:
            # Aplicar estilo según el tipo de token
            codigo_formateado += self.estilo_java(token, tipo)
        codigo_formateado += '</pre>'
        return codigo_formateado




