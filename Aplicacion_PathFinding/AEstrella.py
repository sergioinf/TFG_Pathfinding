import heapq
import math
import utiles
import heuristicos

from mapa import Mapa
from nodo import Nodo

class AEstrella():
    # Lista de nodos abiertos heap queue.
    # El nodo en la cima es el que esta más cerca del final.
    abiertos: list()
    mapa: Mapa

    def __init__(self, mapa):
        self.mapa = mapa
        self.abiertos = []
        self.heuristico = heuristicos.octil

    def findPath(self, filaI, colI, filaF, colF):
        self.it=0
        self.nodoInicio = self.mapa.getNodoAt(filaI, colI)
        self.nodoObjetivo = self.mapa.getNodoAt(filaF, colF)

        self.nodoInicio.g = 0
        self.nodoInicio.f = 0

        heapq.heappush(self.abiertos, (self.nodoInicio.f, self.nodoInicio))
        self.nodoInicio.abierto = True


        while (len(self.abiertos) > 0):
            self.it+=1
            nodo = heapq.heappop(self.abiertos)[1]
            nodo.cerrado = True

            if (nodo == self.nodoObjetivo):
                return self.devolverSol()

            self.calculaSucesores(nodo)

        return []

    def calculaSucesores(self, nodo):
        filaF = self.nodoObjetivo.fila
        colF = self.nodoObjetivo.columna
        x = nodo.columna
        y = nodo.fila

        vecinos = self.vecinos(nodo)
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
                sigNodo.h = sigNodo.h or self.heuristico(abs(jy - filaF), abs(jx - colF))
                sigNodo.f = sigNodo.g + sigNodo.h
                sigNodo.padre = nodo

                if (not sigNodo.abierto):
                    heapq.heappush(self.abiertos, (sigNodo.f, sigNodo))
                    sigNodo.abierto = True
                else:
                    for i in range(len(self.abiertos)):
                        if (self.abiertos[i][1] == sigNodo):
                            self.abiertos[i] = (sigNodo.g - sigNodo.f, sigNodo)


    def vecinos(self, nodo):
        vecinos = []
        neighborNodes = self.mapa.getNeighbors(nodo)
        for i in range(len(neighborNodes)):
            neighborNode = neighborNodes[i]
            vecinos.append([neighborNode.fila, neighborNode.columna])

        return vecinos

    def devolverSol(self):
        listaSol = utiles.recuperaCamino(self.nodoObjetivo)
        datos ="Nodos expandidos: "+str(self.it)+"\n"+"Longitud de la solución: "+str(len(listaSol))+"\n"+"Coste de la solución: "+ str(self.nodoObjetivo.g)
        return listaSol, datos, self.nodoObjetivo.g, self.it
