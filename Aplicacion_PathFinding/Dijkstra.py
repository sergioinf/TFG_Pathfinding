import heapq
import math
import utiles
import heuristicos

from mapa import Mapa
from nodo import Nodo

class Dijkstra():


    # Lista de nodos abiertos heap queue.
    # El nodo en la cima es el que esta más cerca del final.
    abiertos: list()
    mapa: Mapa

    def __init__(self, mapa):
        self.mapa = mapa
        self.abiertos = []


    def findPath(self, filaI, colI, listaObjetivos, fIC=0, cIC=0, tamCluster=512):

        self.nodoInicio = self.mapa.getNodoAt(filaI, colI)
        conjuntoObjetivos = set()
        for i in listaObjetivos:
            conjuntoObjetivos.add(i)
        caminos = []

        self.nodoInicio.g = 0
        self.nodoInicio.f = 0


        heapq.heappush(self.abiertos, (self.nodoInicio.f, self.nodoInicio))
        self.nodoInicio.abierto = True

        # while the open list is not empty
        while (len(self.abiertos) > 0):

            nodo = heapq.heappop(self.abiertos)[1]
            nodo.cerrado = True

            if (conjuntoObjetivos.__contains__((nodo.fila, nodo.columna))):
                caminos.append((utiles.recuperaCamino(nodo), nodo.g, (nodo.fila, nodo.columna)))
                conjuntoObjetivos.remove((nodo.fila, nodo.columna))

                if len(conjuntoObjetivos)==0:
                    return caminos

            self.calculaSucesores(nodo, fIC, cIC, tamCluster)
        return caminos


    def calculaSucesores(self, nodo, fIC, cIC, tamCluster):
        x = nodo.columna
        y = nodo.fila

        vecinos = self.vecinos(nodo, fIC, cIC, tamCluster)
        for i in range(len(vecinos)):

            neighbor = vecinos[i]

            jx = neighbor[1]
            jy = neighbor[0]

            sigNodo = self.mapa.getNodoAt(jy, jx)

            if (sigNodo.cerrado):
                continue

            if abs(y-jy)==1 and abs(x-jx)==1:
                ng = nodo.g + 1414
            else:
                ng = nodo.g + 1000

            if (not sigNodo.abierto or ng < sigNodo.g):

                sigNodo.g = ng
                sigNodo.h = 0
                sigNodo.f = sigNodo.g + sigNodo.h
                sigNodo.padre = nodo

                if (not sigNodo.abierto):
                    heapq.heappush(self.abiertos, (sigNodo.f, sigNodo))
                    sigNodo.abierto = True
                else:
                    for i in range(len(self.abiertos)):
                        if (self.abiertos[i][1] == sigNodo):
                            self.abiertos[i] = (sigNodo.g - sigNodo.f, sigNodo)


    def vecinos(self, nodo, fIC, cIC, tamCluster):
        vecinos = []

        neighborNodes = self.mapa.getNeighbors(nodo)
        for i in range(len(neighborNodes)):
            neighborNode = neighborNodes[i]
            if neighborNode.fila >= fIC and neighborNode.fila < fIC+tamCluster and neighborNode.columna >= cIC and neighborNode.columna < cIC+tamCluster:
                vecinos.append([neighborNode.fila, neighborNode.columna])

        return vecinos
