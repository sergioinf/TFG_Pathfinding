from nodo import Nodo
import numpy as np
from Grafo import *
import copy

class Mapa():
    def __init__(self,nombre, alto, ancho, matriz, nodos = None, cop = False):
        self.nombre = nombre
        self.matriz = matriz
        self.ancho = ancho
        self.alto = alto
        if cop:
            self.nodos = nodos
        else:
            self.nodos = np.empty([ancho, alto], dtype=Nodo)


    def copy(self):
        return Mapa(self.nombre, self.alto, self.ancho, np.copy(self.matriz),copy.deepcopy(self.nodos), True)

    def construyeNodos(self):
        for i in range(self.alto):
            for j in range(self.ancho):
                if self.matriz[i, j]=='.':
                    self.nodos[i, j]=Nodo(i, j, True)
                else:
                    self.nodos[i,j]=Nodo(i, j, False)
        return self.nodos

    def getNodoAt(self, fila, columna):
        return self.nodos[fila, columna]

    def isInside(self, fila, columna):
        return (columna >= 0 and columna < self.ancho) and (fila >= 0 and fila < self.alto)

    def isWalkableAt(self, fila, columna):
        return self.isInside(fila, columna) and self.nodos[fila, columna].walkable

    def setWalkableAt(self, fila, columna, walkable):
        self.nodos[fila, columna].walkable = walkable

    def getNeighbors(self, nodo):
        x = nodo.columna
        y = nodo.fila

        nodos = self.nodos
        vecinos = []

         # ↑
        if (self.isWalkableAt(y-1, x)):
            vecinos.append(nodos[y - 1, x])

        # →
        if (self.isWalkableAt(y, x + 1)):
            vecinos.append(nodos[y, x + 1])

        # ↓
        if (self.isWalkableAt(y + 1, x)):
            vecinos.append(nodos[y + 1, x])

        # ←
        if (self.isWalkableAt(y, x - 1)):
            vecinos.append(nodos[y, x - 1])

        # ↖
        if (self.isWalkableAt(y - 1, x - 1)):
            vecinos.append(nodos[y - 1, x - 1])

        # ↗
        if (self.isWalkableAt(y - 1, x + 1)):
            vecinos.append(nodos[y - 1, x + 1])

        # ↘
        if (self.isWalkableAt(y + 1, x + 1)):
            vecinos.append(nodos[y + 1, x + 1])

        # ↙
        if (self.isWalkableAt(y + 1, x - 1)):
            vecinos.append(nodos[y + 1, x - 1])

        return vecinos


class MapaHPA():
    def __init__(self, n, d, m, grafo, tamCluster=0, clusters=[], estructuraCluster=[]):
        self.nombre = n
        self.dimensiones = d
        self.mapa = m
        self.grafoAbstracto = grafo
        self.tamCluster=tamCluster
        self.clusters=clusters
        self.estructuraCluster=estructuraCluster

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return MapaHPA(self.nombre, self.dimensiones, self.mapa.__copy__(), self.grafoAbstracto.__copy__(), self.tamCluster, self.clusters, self.estructuraCluster)
