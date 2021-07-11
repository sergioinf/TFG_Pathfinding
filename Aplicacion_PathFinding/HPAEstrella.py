import heapq
import math
import time

import utiles
import heuristicos

from mapa import *
from Dijkstra import *
from Grafo import *
from nodo import Nodo

class HPAEstrella():
    # Lista de nodos abiertos heap queue.
    # El nodo en la cima es el que esta más cerca del final.
    abiertos: list()

    mapa: Mapa
    mapaHPA : MapaHPA

    def __init__(self, mapa,mapaI, mapaG, mapaHPA):
        self.mapa = mapa
        self.mapaI = mapaI
        self.mapaG = mapaG
        self.mapaHPA = mapaHPA
        self.abiertos = []
        self.heuristico = heuristicos.octil

    def findPath(self, filaI, colI, filaF, colF):
        self.tiempo1 = time.time()
        grafo = self.insertar(filaI, colI, filaF, colF)

        self.tiempoInsertar = time.time()-self.tiempo1
        self.mapaHPA.grafoAbstracto = grafo

        self.nodoInicio = self.mapa.getNodoAt(filaI, colI)
        self.nodoObjetivo = self.mapa.getNodoAt(filaF, colF)

        self.nodoInicio.g = 0
        self.nodoInicio.f = 0

        heapq.heappush(self.abiertos, (self.nodoInicio.f, self.nodoInicio))
        self.nodoInicio.abierto = True
        self.it = 0
        while (len(self.abiertos) > 0):
            self.it+=1
            nodo = heapq.heappop(self.abiertos)[1]
            nodo.cerrado = True

            if (nodo == self.nodoObjetivo):
                return self.devolverSol(utiles.recuperaCamino(self.nodoObjetivo))
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

            jx = neighbor[0][1]
            jy = neighbor[0][0]
            ng = neighbor[1]

            sigNodo = self.mapa.getNodoAt(jy, jx)

            if (sigNodo.cerrado):
                continue

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
        v, sucesores = self.mapaHPA.grafoAbstracto.get_sucesores(nodo.fila, nodo.columna)
        A = []
        for i in sucesores:

            coste = i.get_weight(v)+self.mapa.getNodoAt(nodo.fila, nodo.columna).g
            A.append([i.id, coste])
        return A

    def insertar(self, filaI, colI, filaF, colF):
        grafo = self.mapaHPA.grafoAbstracto.__copy__()

        tamCluster = self.mapaHPA.tamCluster
        numClustersPorFila = self.mapaHPA.dimensiones//self.mapaHPA.tamCluster

        cI = (filaI // self.mapaHPA.tamCluster)*numClustersPorFila+(colI // self.mapaHPA.tamCluster)
        cD = (filaF // self.mapaHPA.tamCluster)*numClustersPorFila+(colF // self.mapaHPA.tamCluster)

        clusterInicio = self.mapaHPA.estructuraCluster[cI].copy()
        clusterDestino = self.mapaHPA.estructuraCluster[cD].copy()

        """malla = Mapa("provisional", 512, 512, self.mapaI)
        malla.construyeNodos()"""
        dijkstra = Dijkstra(self.mapaI)
        camino = dijkstra.findPath(filaI, colI, clusterInicio, (filaI//tamCluster)*tamCluster, (colI//tamCluster)*tamCluster, tamCluster)
        if camino != None:
            for r in camino:
                grafo.add_edge((filaI, colI), r[2], r[1], r[0])

        """malla2 = Mapa("provisional",512, 512, self.mapaG)
        malla2.construyeNodos()"""
        dijkstra = Dijkstra(self.mapaG)
        camino = dijkstra.findPath(filaF, colF, clusterDestino, (filaF//tamCluster)*tamCluster, (colF//tamCluster)*tamCluster, tamCluster)
        if camino != None:
            for r in camino:
                grafo.add_edge((filaF, colF), r[2], r[1], r[0])

        return grafo

    def devolverSol(self, listaNodos):
        listaSol = []
        for i in range(0, len(listaNodos)-1):
            nodo1 = self.mapaHPA.grafoAbstracto.get_verticeComp(listaNodos[i][0], listaNodos[i][1])
            nodo2 = self.mapaHPA.grafoAbstracto.get_verticeComp(listaNodos[i+1][0], listaNodos[i+1][1])
            sig = nodo1.get_camino(nodo2)
            if sig == None:
                sig = nodo2.get_camino(nodo1)
            listaSol = listaSol+sig
        datos ="Nodos expandidos: "+str(self.it)+"\n"+"Longitud de la solución: "+str(len(listaSol))+"\n"+"Coste de la solución: "+ str(self.nodoObjetivo.g)+"\n"
        return listaSol, datos, self.nodoObjetivo.g,self.it, self.tiempoInsertar
