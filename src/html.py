"""
Clases para facilitar el uso de htm en las preguntas, esto solo 
funciona correctamente en el formato XML
"""
import math
class HtmlOl:
    """
    Encapsula un tag de lista ordenada
    """
    def __init__(self):
        self.style = "text-align: left;"
    
    def __call__(self, *items):
        s = "<ol>"
        for v in items:
            s+= '<li style="'+self.style+'">'
            s+= str(v)
            s+= '</li>'
        s+= '</ol>'
        return s

class HtmlCanvas:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.style = "border: 2px solid #777;"
        self.id = "idCanvas"
        self.s = "const canvas = document.getElementById('idCanvas'); "
        self.s += "const ctx = canvas.getContext('2d'); "

    def __setattr__(self, name, value):
        if name not in ('w', 'h', 'style', 'id', 's'):
            if isinstance(value, str):
                value = f'"{value}"'
            self.s += f"ctx.{name} = {value};"
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name not in ('w', 'h', 'style', 'id', 's'):
            def method_wrapper(*args, **kwargs):
                nargs =[]
                for a in args:
                    if isinstance(a, str):
                        a = f'"{a}"'
                    else:
                        a = str(a)
                    nargs.append(a)
                args_str = ", ".join(nargs)
                kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
                all_args = ", ".join(filter(None, [args_str, kwargs_str]))
                self.s += f"ctx.{name}({all_args});"
            return method_wrapper
        raise AttributeError(f"'HtmlCanvas' object has no attribute '{name}'")

    def __call__(self):
        canvas = f'\n<canvas id="{self.id}" '
        canvas += f'width="{self.w}" height="{self.h}" '
        canvas += f'style="{self.style}"></canvas>\n'
        canvas += f"<script> {self.s} </script>"
        return canvas

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Plot:
    def __init__(self, w, h, xtick, ytick):
        self.w = w
        self.h = h
        self.setXtick(xtick)
        self.setYtick(ytick)
        
        # Crea el canvas
        self.canvas = HtmlCanvas(w,h)
    
    def setXtick(self,xtick):
        self.xtick = xtick
        self.xmin = xtick[0]
        self.xmax = xtick[-1]
        self.width = self.xmax - self.xmin
        self.sx = self.w/self.width
    
    def setYtick(self, ytick):
        self.ytick = ytick
        self.ymin = ytick[0]
        self.ymax = ytick[-1]
        self.height = self.ymax - self.ymin
        self.sy = self.h/self.height
    
    def global2local(self, x, y):
        """
        Transforma las coordenadas locales globales a locales
        de acuerdo a como se maneja en el canvas, se utiliza
        el prefijo c para indicar canvas, cx, cy serían 
        coordenadas locales del canvas
        """
        cx = (x-self.xmin)*self.sx
        cy = self.h - (y - self.ymin)*self.sy
        return round(cx), round(cy)
    
    def global2localR(self,x,y):
        """
        No redondea
        """
        cx = (x-self.xmin)*self.sx
        cy = self.h - (y - self.ymin)*self.sy
        return cx, cy

    def plot(self, xlist, ylist, color="#00F", lineWidth=1):
        ctx = self.canvas
        ctx.beginPath()
        x0,y0 = self.global2localR(xlist[0],ylist[0])
        ctx.moveTo(x0,y0)
        for x, y in zip(xlist[1:],ylist[1:]):
            if y == None:
                x1, y1 = self.global2localR(x,0)
                y1 = None
            else:
                x1, y1 = self.global2localR(x,y)
            if y == None:
                x0,y0=x1,y1
                continue
            if y0 == None:
                ctx.moveTo(x1,y1)
            else:
                ctx.lineTo(x1, y1)
            x0,y0=x1,y1
            
        ctx.strokeStyle = color
        ctx.lineWidth = lineWidth
        ctx.stroke()
    
    def plotFx(self, fx, color= "#00f", colorA = "#f00"):
        
        self.plot(fx.x,fx.y, color=color)
        for jump in fx.jumps:
            left ,right = jump
            if left[1] != None :
                x0,y0 = left[:2]
                #valor definido en la función
                self.drawPoint(x0,y0,color=color, fill = left[2])
            if right[1] !=None:
                x0,y0 = right[:2]
                #valor definido en la función
                self.drawPoint(x0,y0,color=color, fill = right[2])
            if left[1] == None or right[1] == None:
                self.drawVAsymptote(left[0], color=colorA)
    def drawPoint(self, x,y, color="#00f", fill=False):
        """
        Dibuja un punto en la coordenada x,y 
        representado por un círuclo
        """
        ctx = self.canvas
        ctx.beginPath();
        x0,y0 = self.global2localR(x,y)
        ctx.arc(x0, y0, 3, 0, math.pi * 2);
        ctx.strokeStyle = color
        ctx.lineWidth = 1
        if fill:
            ctx.fillStyle = color
        else:
            ctx.fillStyle = "#fff"
        ctx.fill()
        ctx.stroke()
    def drawLine(self, x0,y0, x1,y1, color, lineWidth):
        ctx = self.canvas
        ctx.beginPath()
        ctx.moveTo(x0,y0)
        ctx.lineTo(x1, y1)
        ctx.strokeStyle = color
        ctx.lineWidth = lineWidth
        ctx.stroke()
        
    
    def drawGrid(self, color="#accfec"):
        xtick = self.xtick[1:-1]
        ytick = self.ytick[1:-1]
        ctx = self.canvas
        ctx.beginPath()
        
        for x in xtick:
            x0, y0 = self.global2local(x,self.ymin)
            x1, y1 = self.global2local(x,self.ymax)
            ctx.moveTo(x0,y0)
            ctx.lineTo(x1, y1)
        
        for y in ytick:
            x0, y0 = self.global2local(self.xmin,y)
            x1, y1 = self.global2local(self.xmax,y)
            ctx.moveTo(x0,y0)
            ctx.lineTo(x1, y1)
        
        ctx.strokeStyle = color
        ctx.lineWidth = 1
        ctx.stroke()

    def drawLineDash(self,x0,y0,x1,y1, wline=5, wspace=5, color="#f00", lineWidth=1):
        """
        wline: ancho de linea
        wspace: ancho del espacio
        """
        ctx = self.canvas
        x0,y0 = self.global2localR(x0,y0)
        x1,y1 = self.global2localR(x1,y1)
        ctx.setLineDash([wline, wspace])
        ctx.strokeStyle = color
        ctx.beginPath()
        ctx.moveTo(x0, y0)
        ctx.lineTo(x1, y1)
        ctx.stroke()
        ctx.setLineDash([])
    
    def drawVAsymptote(self,x, color="#f00"):
        x0,y0 = x, self.ymin
        x1, y1 = x0, self.ymax
        self.drawLineDash(x0,y0,x1,y1,color=color)

    def drawHAsymptote(self, y, color="#f00"):
        x0,y0 = self.xmin, y
        x1, y1 = self.xmax, y
        self.drawLineDash(x0,y0,x1,y1,color=color)

    def drawAxis(self, color = "#77767b"):
        # no se dibuja el primer y último elemento, estos son 
        # solo referencias para ajustar la escala
        xtick = self.xtick[1:-1]
        ytick = self.ytick[1:-1]
        ctx = self.canvas
        if self.xmin < 0 and self.xmax > 0:
            # Grafica eje y
            x0, y0 = self.global2local(0,self.ymin)
            x1, y1 = self.global2local(0,self.ymax)
            self.drawLine(x0,y0,x1,y1,color, 1)
            # Grafica las rayitas
            ctx.beginPath()
            for y in ytick:
                cx, cy = self.global2local(0,y)
                ctx.moveTo(cx-5,cy)
                ctx.lineTo(cx+5, cy)
            ctx.stroke()
            
            # texto
            ctx.font = "12px Arial"
            ctx.fillStyle = color
            ctx.textBaseline = "middle"
            ctx.textAlign = "right"
            for y in ytick:
                if y == 0:
                    continue
                cx, cy = self.global2local(0,y)
                ctx.fillText(str(y), cx-12,cy)
            
        if self.ymin < 0 and self.ymax > 0:
            x0, y0 = self.global2local(self.xmin,0)
            x1, y1 = self.global2local(self.xmax,0)
            self.drawLine(x0,y0,x1,y1,color, 1)
            # Grafica las rayitas
            ctx.beginPath()
            for x in xtick:
                cx, cy = self.global2local(x,0)
                ctx.moveTo(cx,cy+5)
                ctx.lineTo(cx, cy-5)
            ctx.stroke()
            # texto
            for x in xtick:
                if x == 0:
                    continue
                cx, cy = self.global2local(x,0)
                ctx.fillText(str(x), cx+3,cy+15)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Function:
    """
    Encapsula los datos de una función para utilizarse en el Plot
    """
    def __init__(self,x):
        '''
        x: lista de puntos en x
        '''
        self.x = x
        self.y = [ 0 ]*len(x)
        # un salto se configura como una tupla que 
        # contiene información de la parte izquierda y derecha del salto
        # (x,y, < valor incluido >)
        # Por ejemplo una asíntota en 2
        # ( (2,None, False), (2,None,False))
        # Un salto en 2, pasa de 5 a 9, cerrado en 5, y abierto en 9
        # ( (2, 5, True), (2,9,False) )
        self.jumps = []
        self.run() # ejecuta la función para hallar y
    
    def tipoSalto(self,x,y, definido ):
        if definido:
            if y == None:
                #No puede haber un salto definido con valor de y indefinido
                return "imposible" 
            else:
                return "extremo cerrado"
        else:
            if y == None:
                return "asíntota vertical"
            else:
                return "extremo abierto"
    
    def run(self):
        """
        Esta función es la que se debe ajustar para crear otras funciones
        heredando de esta clase
        """
        tramo = 0
        for i, xi in enumerate(self.x):
            if xi < 2:
                self.y[i] = xi
                tramo = 0
            else:
                if tramo == 0:
                    salto = ( (2, xi , False ) , (2, None, False) )
                    self.jumps.append(salto)
                    tramo = 1
                    self.y[i] = None
                    print("salto en:", xi)
                else:
                    self.y[i] = 1/(xi-2)
    
