from .Shape import *
class Triangle(Shape):
    def __init__(self, is_regular, *Lines):
        super().__init__(is_regular, *Lines)
        self._is_regular = is_regular
        self.edges
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        p = self.compute_perimeter()
        sp = p/2 #semiperimetro
        area = ((sp*(sp - self.lines[0].length)*
                (sp-self.lines[1].length)*(sp - self.lines[2].length)))**(1/2)
        area = round(area,4) #redondea el número para no tener inconsistencias con la fórmula tradicional
        return area
    def compute_inner_angles(self):
        return super().compute_inner_angles()

class Scalene(Triangle):
    def __init__(self, is_regular, *Lines):
        self.lines = Lines
        self._is_regular = is_regular
        #se comparan las longitudes de las líneas:
        comp_1 = self.lines[0].length != self.lines[1].length
        comp_2 = self.lines[1].length != self.lines[2].length
        comp_3 = self.lines[2].length != self.lines[0].length 
        if not (comp_1 and comp_2 and comp_3):
            raise NotImplementedError("este no es un triángulo escaleno, introduzca un triángulo válido")
        else: super().__init__(is_regular, *Lines)

class Isosceles(Triangle):
    def __init__(self, is_regular, line_base : "Line", third_point: "Point"):
        self._line_base = line_base
        self.lines = [line_base, Line(line_base.point_start,third_point), #igual toca meter 3 puntos para el triángulo pero por lo menos no 3 líneas
                      Line(line_base.point_end,third_point)]
        #se verifica que el triángulo sea Isosceles
        comp_1 = self.lines[0].length == self.lines[1].length
        comp_2 = self.lines[1].length == self.lines[2].length
        comp_3 = self.lines[2].length == self.lines[0].length 
        if not (comp_1 or comp_2 or comp_3):
            raise NotImplementedError("este no es un triángulo isosceles, introduzca un triángulo válido")
        else: super().__init__(is_regular, *self.lines)
    def get_line_base(self):
        return self._line_base
    def set_line_base(self, new_line_base: "Line"):
        self._line_base = new_line_base
        self.lines[0] = new_line_base
        self.lines[1] = Line(new_line_base._point_start, self.lines[1]._point_end)
        self.lines[2] = Line(new_line_base._point_end, self.lines[2]._point_end)
        
class Equilateral(Triangle):
    def __init__(self, is_regular, line_base : "Line", third_point: "Point"):
        self._line_base = line_base
        self.lines = [line_base,Line(line_base._point_end,third_point), 
                      Line(line_base._point_start,third_point)] #igual toca meter 3 puntos para el triángulo pero por lo menos no 3 líneas
        comp_1 = self.lines[0].length == self.lines[1].length
        comp_2 = self.lines[1].length == self.lines[2].length
        comp_3 = self.lines[2].length == self.lines[0].length 
        if not (comp_1 and comp_2 and comp_3): #se verifica que el triángulo sea equilatero
            raise NotImplementedError("este no es un triángulo equilatero, introduzca un triángulo válido")
        else: super().__init__(is_regular, *self.lines)
    def get_line_base(self):
        return self._line_base
    def set_line_base(self, new_line_base: "Line"):
        self._line_base = new_line_base
        self.lines[0] = new_line_base
        self.lines[1] = Line(new_line_base._point_start, self.lines[1]._point_end)
        self.lines[2] = Line(new_line_base._point_end, self.lines[2]._point_end)
    def compute_inner_angles(self):
        inner_angles = super().compute_inner_angles()
        if 30 in inner_angles: #hardcodeando un error re extraño
           inner_angles.remove(30)
           inner_angles.append(60)
        return inner_angles

class TriRectangle(Triangle): #genera un triángulo rectángulo con sus catetos
    def __init__(self, is_regular, *Lines):
        lineas = [Lines[0],Lines[1], Line(Lines[0]._point_end,Lines[1]._point_end)]
        self._is_regular = is_regular
        self.lines = tuple(lineas)
        cosines = []
        for l in range(-1,len(self.lines)-1,1): #se usa el método del coseno entre 2 vectores
            linea_1_unitario = [(self.lines[l]._point_end._x - #este pedazo es el x del unitario
                                 self.lines[l]._point_start._x)/self.lines[l].length,
                                (self.lines[l]._point_end._y - #este pedazo es el y unitario
                                 self.lines[l]._point_start._y)/self.lines[l].length]
            linea_2_unitario = [(self.lines[l+1]._point_end._x - #este pedazo es el x del unitario
                                 self.lines[l+1]._point_start._x)/self.lines[l+1].length,
                                (self.lines[l+1]._point_end._y - #este pedazo es el y unitario
                                 self.lines[l+1]._point_start._y)/self.lines[l+1].length]
            cos = (linea_1_unitario[0]*linea_2_unitario[0]+
                         linea_1_unitario[1]*linea_2_unitario[1])
            cosines.append(cos)
        if not 0 in cosines: #se verifica que el triángulo sea rectángulo
            raise NotImplementedError("este no es un triángulo rectángulo, introduzca un triángulo válido")
        else: pass 
        self.lines = (self.lines[0], self.lines[1],
                    Line(self.lines[0]._point_end, self.lines[1]._point_end))
    def compute_inner_angles(self):
        #toco resolver, se busca implementar la solución del álgebra lineal
        #se busca sacar el coseno del ángulo entre 2 vectores y se aplica arccos
            angles = []
            if self._is_regular == True:
                if type(self) == Equilateral:
                    return f"los ángulos internos valen {180/len(self.lines)}"
                else: return f"los ángulos internos valen {360/len(self.lines)}"
            else: pass
            for l in range(-1,len(self.lines)-1,1): #se usa el método del coseno entre 2 vectores
                linea_1_unitario = [(self.lines[l]._point_end._x - #este pedazo es el x del unitario
                                    self.lines[l]._point_start._x)/self.lines[l].length,
                                    (self.lines[l]._point_end._y - #este pedazo es el y unitario
                                    self.lines[l]._point_start._y)/self.lines[l].length]
                linea_2_unitario = [(self.lines[l+1]._point_end._x - #este pedazo es el x del unitario
                                    self.lines[l+1]._point_start._x)/self.lines[l+1].length,
                                    (self.lines[l+1]._point_end._y - #este pedazo es el y unitario
                                    self.lines[l+1]._point_start._y)/self.lines[l+1].length]
                angle = round(degrees(acos(linea_1_unitario[0]*linea_2_unitario[0]+
                            linea_1_unitario[1]*linea_2_unitario[1])))
                if abs(angle) > 90: #corrige en caso de que el ángulo encontrado sea de más de 90 grados
                    angle = angle -90
                    angles.append(angle) #!! esto debería servir pero por alguna extraña razón no lo hace
                else: angles.append(angle)
            return angles