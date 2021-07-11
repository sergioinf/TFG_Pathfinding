import heapq
import math
import utiles
import heuristicos

from mapa import Mapa
from nodo import Nodo

class JPS():
    # Lista de nodos abiertos heap queue.
    # El nodo en la cima es el que esta más cerca del final.
    abiertos: list()
    mapa: Mapa

    def __init__(self, mapa):
        self.mapa = mapa
        self.abiertos = []
        self.heuristico = heuristicos.octil

    def findPath(self, filaI, colI, filaF, colF):
        self.it = 0

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

            jumpPoint = self.salto(neighbor[0], neighbor[1], y, x)

            if (jumpPoint):

                jx = jumpPoint[1]
                jy = jumpPoint[0]

                jumpNode = self.mapa.getNodoAt(jy, jx)

                if (jumpNode.cerrado):
                    continue

                d = heuristicos.octil(abs(jx - x), abs(jy - y))
                ng = nodo.g + d

                if (not jumpNode.abierto or ng < jumpNode.g):

                    jumpNode.g = ng
                    jumpNode.h = jumpNode.h or self.heuristico(abs(jy - filaF), abs(jx - colF))
                    jumpNode.f = jumpNode.g + jumpNode.h
                    jumpNode.padre = nodo

                    if (not jumpNode.abierto):
                        heapq.heappush(self.abiertos, (jumpNode.f, jumpNode))
                        jumpNode.abierto = True
                    else:
                        for i in range(len(self.abiertos)):
                            if (self.abiertos[i][1] == jumpNode):
                                self.abiertos[i] = (jumpNode.g - jumpNode.f, jumpNode)

    def salto(self, fila, columna, filaP, columnaP):
        dx = columna - columnaP
        dy = fila - filaP

        if (not self.mapa.isWalkableAt(fila, columna)):
            return None

        if fila == self.nodoObjetivo.fila and columna == self.nodoObjetivo.columna:
            return [fila, columna]

        # Diagonal
        if (dx != 0 and dy != 0):
            if ((self.mapa.isWalkableAt(fila + dy, columna - dx) and not self.mapa.isWalkableAt(fila, columna - dx)) or
                (self.mapa.isWalkableAt(fila - dy, columna + dx) and not self.mapa.isWalkableAt(fila - dy, columna))):
                return [fila, columna]
            if (self.salto(fila, columna + dx, fila, columna) or self.salto(fila + dy, columna, fila, columna)):
                return [fila, columna]
        # Horizontal / vertical
        else:
            if (dx != 0):
                if ((self.mapa.isWalkableAt(fila + 1, columna + dx) and not self.mapa.isWalkableAt(fila + 1, columna)) or
                (self.mapa.isWalkableAt(fila - 1, columna + dx) and not self.mapa.isWalkableAt(fila - 1, columna))):
                    return [fila, columna]
            else:
                if ((self.mapa.isWalkableAt(fila + dy, columna + 1) and not self.mapa.isWalkableAt(fila, columna + 1)) or
                (self.mapa.isWalkableAt(fila + dy, columna - 1) and not self.mapa.isWalkableAt(fila, columna - 1))):
                    return [fila, columna]

        return self.salto(fila + dy, columna + dx, fila, columna)

    def vecinos(self, nodo):
        padre = nodo.padre
        x = nodo.columna
        y = nodo.fila
        vecinos = []

        if (padre):

            px = padre.columna
            py = padre.fila

            dx = int((x - px) / max(abs(x - px), 1))
            dy = int((y - py) / max(abs(y - py), 1))

            if (dx != 0 and dy != 0):
                if (self.mapa.isWalkableAt(y + dy, x)):
                    vecinos.append([y + dy, x])

                if (self.mapa.isWalkableAt(y, x + dx)):
                    vecinos.append([y, x + dx])

                if (self.mapa.isWalkableAt(y + dy, x + dx)):
                    vecinos.append([y + dy, x + dx])

                if (not self.mapa.isWalkableAt(y, x - dx)):
                    vecinos.append([y + dy, x - dx])

                if (not self.mapa.isWalkableAt(y - dy, x)):
                    vecinos.append([y - dy, x + dx])

            else:
                if (dx == 0):
                    if (self.mapa.isWalkableAt(y + dy, x)):
                        vecinos.append([y + dy, x])

                    if (not self.mapa.isWalkableAt(y, x + 1)):
                        vecinos.append([y + dy, x + 1])

                    if (not self.mapa.isWalkableAt(y, x - 1)):
                        vecinos.append([y + dy, x - 1])
                else:
                    if (self.mapa.isWalkableAt(y, x + dx)):
                        vecinos.append([y, x + dx])

                    if (not self.mapa.isWalkableAt(y + 1, x)):
                        vecinos.append([y + 1, x + dx])

                    if (not self.mapa.isWalkableAt(y - 1, x)):
                        vecinos.append([y - 1, x + dx])

        else:
            neighborNodes = self.mapa.getNeighbors(nodo)
            for i in range(len(neighborNodes)):
                neighborNode = neighborNodes[i]
                vecinos.append([neighborNode.fila, neighborNode.columna])

        return vecinos

    def devolverSol(self):
        listaSol = utiles.recuperaCamino(self.nodoObjetivo)
        datos ="Nodos expandidos: "+str(self.it)+"\n"+"Longitud de la solución: "+str(len(listaSol))+"\n"+"Coste de la solución: "+ str(self.nodoObjetivo.g)
        return listaSol, datos, self.nodoObjetivo.g, self.it

