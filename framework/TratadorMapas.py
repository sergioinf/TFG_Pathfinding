import pickle
import threading

from Grafo import *
from Mapas import *
import numpy as np
import os
import sys

def main():

    directory = "mapas"
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    listaMapas = []
    listaMapasHPA = []
    for i in range(1, 5):

        nombre = "BGMAP ("+str(i)+").map"
        mapa = leerMapa(nombre)
        l = len(mapa)

        print(nombre)
        grafo = Graph({}, 0)
        listaMapas.append(Mapa(nombre, l, mapa))
        listaMapasHPA.append(crearMapaHPA(nombre, mapa, grafo))

    f = open("mapasTratados\\mapasBase1.txt", "wb")
    pickle.dump(listaMapas, f)
    f.close()

    c = open("mapasTratados\\mapasHPA4.txt", "wb")
    pickle.dump(listaMapasHPA, c)
    c.close()
    print("Leidos los mapas de la carpeta mapas")


def leerMapa(nombreFichero):
    fichero = open("mapas\\"+nombreFichero)
    leido = fichero.readlines()
    fichero.close()

    longitud =  len(leido)
    mapa = np.empty([longitud-4, longitud-4], dtype=str)

    j=0
    for i in range(4,longitud):
        mapa[j,:] = list(leido[i][0:512])
        j+=1

    return mapa


def crearMapaHPA(nombre, m, grafo):

    mapa = m.copy()
    tamaños = divisores(len(mapa))
    tamañoCluster = tamaños[2]  #32 es el tamaño de cluster con la pos 5
    pGrande = 12

    clusters = []
    numClustersPorFila = len(mapa) // tamañoCluster
    for i in range(0, numClustersPorFila):
        for j in range(0, numClustersPorFila):
            clusters.append((i * tamañoCluster, j * tamañoCluster))

    mapaPintar = np.empty([len(mapa), len(mapa)], dtype=int)
    for i in range(0, len(mapaPintar)):
        for j in range(0, len(mapaPintar)):
            mapaPintar[i,j] = 0

    indice = 1

    for i in clusters:
        if i[1] + tamañoCluster < len(mapa):

            clusterActual = (i[0] // tamañoCluster)*numClustersPorFila+(i[1] // tamañoCluster)
            ##Conexiones horizontales
            mapaPintar, indice, grafo= calculaPuertas2(mapa, mapaPintar, tamañoCluster, indice, pGrande, i[0], i[1], grafo, clusterActual, False)
            ##Conexiones verticales
            mapaPintar = np.transpose(mapaPintar)
            mapa = np.transpose(mapa)
            clusterActual = (i[1] // tamañoCluster)*numClustersPorFila+(i[0] // tamañoCluster)

            mapaPintar, indice, grafo= calculaPuertas2(mapa, mapaPintar, tamañoCluster, indice, pGrande, i[0], i[1], grafo, clusterActual, True)
            mapaPintar = np.transpose(mapaPintar)
            mapa = np.transpose(mapa)


    agente = Agente(m=mapa)
    print("Encontrado todas las puertas y creado el agente")
    añadirConexionesIntraClusters(agente, grafo, numClustersPorFila, tamañoCluster)
    print("Creadas las conexiones dentro de los clusters")

    return MapaHPA(nombre, len(mapa), mapa, grafo, tamañoCluster, clusters)

def divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def añadirAlGrafo(grafo, fil, col, n1, n2, clusterActual, traspuesta, clustersPorFila):

    g = grafo.__copy__()

    if traspuesta:
        Nodo = NodoGrafo('N'+str(n1),col, fil, cluster=clusterActual)

        Nodo2 = NodoGrafo('N'+str(n2),col+1, fil, cluster=clusterActual+clustersPorFila)
    else:
        Nodo = NodoGrafo('N'+str(n1),fil, col, cluster=clusterActual)

        Nodo2 = NodoGrafo('N'+str(n2),fil, col+1, cluster=clusterActual+1)

    a1 = NodoArbol(Nodo.fila, Nodo.columna)
    a2 = NodoArbol(Nodo2.fila, Nodo2.columna)

    g.add_edge(Nodo, Nodo2, 1000, [a1, a2])

    return g

def calculaPuertas2(mapa, mapaPintar, tamañoCluster, indice, pGrande, i0, i1, grafo, clusterActual, traspuesta):
    c = 0
    for j in range(i0, i0 + tamañoCluster):

        columna = i1 + tamañoCluster - 1
        if mapa[j,columna] == '.' and mapa[j,columna + 1] == '.':
            c += 1
            if j==(i0 + tamañoCluster-1):
                if c>=pGrande:
                    if mapaPintar[j,columna] == 0:
                        mapaPintar[j,columna] = indice
                        indice += 1
                    if mapaPintar[j,columna+1] == 0:
                        mapaPintar[j,columna+1] = indice
                        indice += 1
                    if mapaPintar[j-c+1,columna] == 0:
                        mapaPintar[j - c+1,columna] = indice
                        indice += 1
                    if mapaPintar[j-c+1,columna + 1] == 0:
                        mapaPintar[j - c+1,columna + 1] = indice
                        indice += 1


                    fil = j
                    grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

                    fil = j-c+1
                    grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

                    c = 0
                else:
                    dif = c//2
                    if mapaPintar[j-dif,columna] == 0:
                        mapaPintar[j-dif,columna] = indice
                        indice += 1
                    if mapaPintar[j-dif,columna + 1] == 0:
                        mapaPintar[j-dif,columna + 1] = indice
                        indice += 1

                    #Añadiendo en el grafo
                    fil = j-dif
                    grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

                    c = 0
        else:
            if c>=pGrande:
                if mapaPintar[j-1,columna] == 0:
                    mapaPintar[j - 1,columna] = indice
                    indice += 1
                if mapaPintar[j-1,columna+1] == 0:
                    mapaPintar[j - 1,columna+1] = indice
                    indice += 1
                if mapaPintar[j-c,columna] == 0:
                    mapaPintar[j - c,columna] = indice
                    indice += 1
                if mapaPintar[j-c,columna + 1] == 0:
                    mapaPintar[j - c,columna + 1] = indice
                    indice += 1


                fil = j-1
                grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

                fil = j-c
                grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

                c = 0
            elif c>0 and c<pGrande:
                dif = c//2
                if mapaPintar[j - 1-dif,columna] == 0:
                    mapaPintar[j - 1-dif,columna] = indice
                    indice += 1
                if mapaPintar[j - 1-dif,columna + 1] == 0:
                    mapaPintar[j - 1-dif,columna + 1] = indice
                    indice += 1

                #Añadiendo en el grafo
                fil = j - 1-dif
                grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

                c = 0

    return mapaPintar, indice, grafo

def añadirConexionesIntraClusters(agente, grafo, numClusters, tamCluster):
        vertices = grafo.get_vertices()
        clusters = []

        for i in range(0, numClusters**2):
            clusters.append([])

        for i in vertices:
            clusters[i.cluster-1].append(i)

        """for c in clusters:
            print(c)"""

        for c in clusters:
            while len(c)>1:
                inicio = c.pop()
                agente.inicial=NodoArbol(inicio.fila, inicio.columna)
                resultados, it = agente.dijkstra(c, (inicio.fila//tamCluster)*tamCluster, (inicio.columna//tamCluster)*tamCluster, tamCluster)
                if resultados!=None:
                    for r in resultados:
                        grafo.add_edge(inicio, r[0], r[2], r[1])
        return grafo

if __name__ == '__main__':
    sys.setrecursionlimit(300000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=main)
    thread.start()
