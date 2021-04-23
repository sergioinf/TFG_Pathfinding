from Grafo import *

class Mapa:
    def __init__(self, n, d, m):
        self.nombre=n
        self.dimensiones=d
        self.mapa=m


class MapaHPA():
    def __init__(self, n, d, m, grafo=Graph(), tamCluster=0, clusters=[]):
        self.nombre = n
        self.dimensiones = d
        self.mapa = m
        self.grafoAbstracto = grafo
        self.tamCluster=tamCluster
        self.clusters=clusters
