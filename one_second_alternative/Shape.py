from math import degrees,acos
class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
    def set_x(self,new_x):
        self._x = new_x
    def set_y(self,new_y):
        self._y = new_y 
    def get_x(self):
        return self._x
    def get_y(self):    
        return self._y

class Line:
    def __init__(self, point_start: "Point", point_end: "Point"):
        self._point_start = point_start
        self._point_end = point_end
        self.length = (float(self._point_end._x - self._point_start._x)**2 +
                  float(self._point_end._y - self._point_start._y)**2)**(1/2)
    def get_point_start(self):
        return self._point_start
    def get_point_end(self):        
        return self._point_end
    def set_point_start(self, new_point_start: "Point"):
        self._point_start = new_point_start
    def set_point_end(self, new_point_end: "Point"):
        self._point_end = new_point_end

class Shape:
    def __init__(self, is_regular: bool, *Lines: "Line"):
        some_edges = []
        self.lines = Lines
        self._is_regular = is_regular
        for i in Lines:
            some_edges.append([i._point_start._x, i._point_start._y])
            some_edges.append([i._point_end._x, i._point_end._y])
            some_edges.pop()
        edges = some_edges
        self.edges = edges
    def get_lines(self):
        return self.lines
    def set_lines(self, *new_lines: "Line"):
        self.lines = new_lines
    def get_is_regular(self):
        return self._is_regular
    def set_is_regular(self, new_is_regular: bool):
        self._is_regular = new_is_regular
    def get_edges(self):
        return self.edges
    def set_edges(self, new_edges):
        self.edges = new_edges
    
    def compute_area(self):
        raise NotImplementedError("a esta clase falta calcularle el area")
    def compute_perimeter(self):
        perimeter = 0
        for line in self.lines:
            perimeter += line.length
        return perimeter
    def compute_inner_angles(self):
        #toco resolver, se busca implementar la solución del álgebra lineal
        #se busca sacar el coseno del ángulo entre 2 vectores y se aplica arccos
        angles = []
        if self._is_regular == True:
            if str(type(self)) == "Equilateral":
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
                angles.append(angle)
            else: angles.append(angle)
        return angles