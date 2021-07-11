class Nodo():
    def __init__(self, fila, columna, walkable = True, f=0, g=0, h=0, abierto = False, cerrado = False, padre = None):
        self.columna = columna
        self.fila = fila
        self.walkable = walkable
        self.f = f
        self.g = g
        self.h = h
        self.abierto = abierto
        self.cerrado = cerrado
        self.padre = padre

    def __str__(self):
        return "("+str(self.fila)+", "+str(self.columna)+")"

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        return Nodo(self.fila, self.columna, self.walkable, self.f, self.g, self.h, self.abierto, self.cerrado, self.padre)

    def __lt__(self, other):
        return self.g - self.f < other.g-other.f

    def __gt__(self, other):
        return self.g - self.f > other.g - other.f
