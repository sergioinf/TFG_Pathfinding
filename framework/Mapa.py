class Mapa:
    def __init__(self, n, d, m):
        self.nombre=n
        self.dimensiones=d
        self.mapa=m

    def getNombre(self):
        return self.nombre

    def getProcedencia(self):
        return self.procedencia

    def getDimensiones(self):
        return self.dimensiones

    def getMapa(self):
        return self.mapa


class MapaHPA:
    def __init__(self, n, d, m):
        Mapa.__init__(self, n, d, m)
