import time

import numpy as np

from Nodos import *
from Grafo import *
from Nodos import NodoArbol


class Agente:
    def __init__(self, i=None, o=None, m=None):
        self.inicial=i
        self.objetivo=o
        self.mapa = m

    def esFinal(self, nodo):
        if nodo.fila==self.objetivo.fila and nodo.columna == self.objetivo.columna:
            return True
        else:
            return False

    def recuperaSolucion(self, nodo, lista, malla):
        lista.append(nodo)
        if nodo.puntPadreF == -1 :
            return lista
        else :
            return self.recuperaSolucion(malla[nodo.puntPadreF, nodo.puntPadreC], lista, malla)

    def aEstrella(self):
        t_0 = time.time()
        longitud = len(self.mapa)
        malla = np.empty([longitud, longitud], dtype=NodoArbol)
        abiertos = [self.inicial]
        it=0
        exito=False

        while len(abiertos)>0 :
            it+=1
            """if it == 10000:
                break"""
            nActual = abiertos.pop()
            malla[nActual.fila, nActual.columna]=nActual

            if self.esFinal(nActual) :
                exito = True
                break

            sucesores = nActual.calculaSucesores(self.mapa, self.objetivo)

            for n2 in sucesores :
                if malla[n2.fila, n2.columna]==None and abiertos.count(n2)==0 :
                    #n2.puntPadreF=nActual.fila
                    #n2.puntPadreC=nActual.columna
                    #n2.g=nActual.g+nActual.costeArco(n2)
                    #n2.f=n2.g+n2.h(n2.fila, n2.columna, self.objetivo)
                    abiertos.append(n2)
                elif malla[n2.fila, n2.columna]!=None:
                    n2viejo = malla[n2.fila, n2.columna]
                    if n2.g<n2viejo.g:
                        malla[n2.fila, n2.columna]=None
                        abiertos.append(n2)
                else:
                    indice = abiertos.index(n2)
                    n2viejo = abiertos.pop(indice)
                    if n2.g<n2viejo.g:
                        abiertos.append(n2)
                    else:
                        abiertos.append(n2viejo)

            abiertos.sort(reverse = True)

        if exito==False :
            t_1=time.time()
            return None
        else :
            listaSol = self.recuperaSolucion(nActual, [], malla)
            t_1 = time.time()
            datos ="Nodos expandidos: "+str(it)+"\n"+"Longitud de la solución: "+str(len(listaSol))+"\n"+"Coste de la solución: "+ str(nActual.g)+"\n"

            return [listaSol, datos, nActual.g, t_1-t_0, it]

    def dijkstra(self, listaObjetivos, fIC, cIC, tamCluster):
        nActual = self.inicial
        malla = np.empty([len(self.mapa), len(self.mapa)], dtype=NodoArbol)
        abiertos = [nActual]
        caminos = []
        contador = 0
        exito = False
        it=0

        while len(abiertos)>0:
            it+=1
            nActual = abiertos.pop()
            malla[nActual.fila, nActual.columna] = nActual
            esFinal = self.esFinalDijkstra(nActual, listaObjetivos)
            if esFinal[1]:
                cSol = self.recuperaSolucion(nActual, [], malla)
                caminos.append((esFinal[0], cSol, nActual.g))
                contador+=1
                exito = True

            if contador == len(listaObjetivos):
                break

            sucesores = nActual.calculaSucesoresDijkstra(self.mapa, fIC, cIC, tamCluster)

            for n2 in sucesores:
                if malla[n2.fila, n2.columna]==None and abiertos.count(n2)==0:
                   abiertos.append(n2)
                elif abiertos.count(n2)!=0:
                    n2viejo = abiertos.pop(abiertos.index(n2))

                    if n2.g<n2viejo.g:
                        abiertos.append(n2)
                    else:
                        abiertos.append(n2viejo)

            abiertos.sort(reverse = True)

        if exito==True:
            return caminos, it
        else:
            return None, it

    def esFinalDijkstra(self, nodo, lista=[]):
        for i in lista:
            if i.fila==nodo.fila and i.columna == nodo.columna:
                return (i, True)
        return (0, False)

    def hpaEstrella(self, grafo):
        t_0 = time.time()
        longitud = len(self.mapa)
        malla = np.empty([longitud, longitud], dtype=NodoArbol)
        abiertos = [self.inicial]
        it=0
        exito=False

        while len(abiertos)>0 :
            it+=1
            nActual = abiertos.pop()
            malla[nActual.fila, nActual.columna]=nActual

            if self.esFinal(nActual) :
                exito = True
                break

            sucesores = nActual.calculaSucesoresHPA(nActual, grafo, self.objetivo)
            for n2 in sucesores :
                if malla[n2.fila, n2.columna]==None and abiertos.count(n2)==0 :
                    abiertos.append(n2)
                elif malla[n2.fila, n2.columna]!=None:
                    n2viejo = malla[n2.fila, n2.columna]
                    if n2.g<n2viejo.g:
                        malla[n2.fila, n2.columna]=None
                        abiertos.append(n2)
                else:
                    indice = abiertos.index(n2)
                    n2viejo = abiertos.pop(indice)
                    if n2.g<n2viejo.g:
                        abiertos.append(n2)
                    else:
                        abiertos.append(n2viejo)

            abiertos.sort(reverse = True)

        if exito==False :
            return None
        else :
            listaNodos = self.recuperaSolucionHPA(nActual,[], malla)
            print("")
            listaSol = []

            for i in range(0, len(listaNodos)-1):
                nodo1 = grafo.get_verticeComp(listaNodos[i].fila, listaNodos[i].columna)
                nodo2 = grafo.get_verticeComp(listaNodos[i+1].fila, listaNodos[i+1].columna)
                sig = nodo1.get_camino(nodo2)
                if sig == None:
                    sig = nodo2.get_camino(nodo1)
                listaSol = listaSol+sig
            t_1 = time.time()
            datos ="Nodos expandidos: "+str(it)+"\n"+"Longitud de la solución: "+str(len(listaSol))+"\n"+"Coste de la solución: "+ str(nActual.g)+"\n"

            return [listaSol, datos, nActual.g,t_1-t_0, it]

    def recuperaSolucionHPA(self, nodo,lista, malla):
        lista.append(nodo)
        if nodo.puntPadreF == -1 :
            return lista
        else :
            return self.recuperaSolucion(malla[nodo.puntPadreF, nodo.puntPadreC], lista, malla)
