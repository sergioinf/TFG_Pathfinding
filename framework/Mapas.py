from Grafo import *

class Mapa:
    def __init__(self, n, d, m):
        self.nombre=n
        self.dimensiones=d
        self.mapa=m

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return Mapa(self.nombre, self.dimensiones, self.mapa.__copy__())


class MapaHPA():
    def __init__(self, n, d, m, grafo=Graph(), tamCluster=0, clusters=[]):
        self.nombre = n
        self.dimensiones = d
        self.mapa = m
        self.grafoAbstracto = grafo
        self.tamCluster=tamCluster
        self.clusters=clusters

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return MapaHPA(self.nombre, self.dimensiones, self.mapa.__copy__(), self.grafoAbstracto.__copy__(), self.tamCluster, self.clusters)
