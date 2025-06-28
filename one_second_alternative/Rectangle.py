from .Shape import *
class Rectangle(Shape):
    def __init__(self, is_regular, *Lines):
        self.lines = Lines
        self._is_regular = is_regular
        super().__init__(is_regular, *Lines)
        if not len(self.lines) == 4:
            print(len(self.lines))
            print(self.lines)
            raise NotImplementedError("estas líneas no pueden formar un rectángulo")

class Square(Rectangle):
    def __init__(self,is_regular = True, *Lines):
        super().__init__(is_regular, *Lines)
        self.lines = Lines
        print(len(self.lines))
        lineas = []
        for l in self.lines:
            lineas.append(l.length)
            print(l.length)
        if not (len(self.lines) == 4 and (lineas.count(lineas[0]) == 4)):
            raise NotImplementedError("estas líneas no pueden formar un cuadrado")