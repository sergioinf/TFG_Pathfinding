import pickle
import threading

from Dijkstra import Dijkstra
from Grafo import *
from mapa import *
import numpy as np
import os
import sys

def mapas():

    directory = "mapas"
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    numMapas = number_of_files

    listaMapas = []
    listaMapasHPA = []
    #for i in range(1, numMapas+1):
    for i in range(1,11):
        nombre = "BGMAP ("+str(i)+").map"
        mapa = leerMapa(nombre)
        l = len(mapa)

        print(nombre)
        grafo = Graph({}, 0)
        mapaA = Mapa(nombre, l, l, mapa)
        mapaA.construyeNodos()
        listaMapas.append(mapaA)
        #listaMapasHPA.append(crearMapaHPA(nombre, mapa, grafo))

    f = open("mapasTratados\\mapasBase.txt", "wb")
    pickle.dump(listaMapas, f)
    f.close()

    """c = open("mapasTratados\\mapaPrueba.txt", "wb")
    pickle.dump(listaMapasHPA, c)
    c.close()"""
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
    tamañoCluster = tamaños[5]  #32 es el tamaño de cluster con la pos 5
    pGrande = 12

    clusters = []
    numClustersPorFila = len(mapa) // tamañoCluster

    for i in range(0, numClustersPorFila):
        for j in range(0, numClustersPorFila):
            clusters.append((i * tamañoCluster, j * tamañoCluster))


    estructuraClusters =[]
    for i in range(numClustersPorFila**2):
        estructuraClusters.append(set())

    mapaPintar = np.empty([len(mapa), len(mapa)], dtype=int)
    for i in range(0, len(mapaPintar)):
        for j in range(0, len(mapaPintar)):
            mapaPintar[i,j] = 0

    indice = 1

    for i in clusters:
        if i[1] + tamañoCluster < len(mapa):

            clusterActual = (i[0] // tamañoCluster)*numClustersPorFila+(i[1] // tamañoCluster)
            ##Conexiones horizontales
            mapaPintar, indice, grafo,estructuraClusters= calculaPuertas2(mapa, mapaPintar, tamañoCluster, indice, pGrande, i[0], i[1], grafo, clusterActual, False, estructuraClusters)
            ##Conexiones verticales
            mapaPintar = np.transpose(mapaPintar)
            mapa = np.transpose(mapa)
            clusterActual = (i[1] // tamañoCluster)*numClustersPorFila+(i[0] // tamañoCluster)
            mapaPintar, indice, grafo,estructuraClusters= calculaPuertas2(mapa, mapaPintar, tamañoCluster, indice, pGrande, i[0], i[1], grafo, clusterActual, True, estructuraClusters)
            mapaPintar = np.transpose(mapaPintar)
            mapa = np.transpose(mapa)


    print("Encontrado todas las puertas y creado el agente")
    añadirConexionesIntraClusters(grafo, numClustersPorFila, tamañoCluster, estructuraClusters, mapa)
    print("Creadas las conexiones dentro de los clusters")

    return MapaHPA(nombre, len(mapa), mapa, grafo, tamañoCluster, clusters, estructuraClusters)

def divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def añadirAlGrafo(grafo, fil, col, n1, n2, clusterActual, traspuesta, clustersPorFila, estructuraClusters):

    g = grafo.__copy__()

    if traspuesta:
        Nodo = (col, fil)
        clusterFrm = clusterActual

        Nodo2 = (col+1, fil)
        clusterTo = clusterActual+clustersPorFila
    else:
        Nodo = (fil, col)
        clusterFrm = clusterActual

        Nodo2 = (fil, col+1)
        clusterTo = clusterActual+1

    lista = estructuraClusters[clusterFrm]
    lista.add(Nodo)
    estructuraClusters[clusterFrm] = lista



    lista2 = estructuraClusters[clusterTo]
    lista2.add(Nodo2)
    estructuraClusters[clusterTo] = lista2


    g.add_edge(Nodo, Nodo2, 1000, [Nodo, Nodo2])

    return g, estructuraClusters

def calculaPuertas2(mapa, mapaPintar, tamañoCluster, indice, pGrande, i0, i1, grafo, clusterActual, traspuesta, estructuraClusters):
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
                    grafo, estructuraClusters = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster, estructuraClusters)

                    fil = j-c+1
                    grafo, estructuraClusters = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster, estructuraClusters)

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
                    grafo, estructuraClusters = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster, estructuraClusters)

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
                grafo, estructuraClusters = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster, estructuraClusters)

                fil = j-c
                grafo, estructuraClusters = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster, estructuraClusters)

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
                grafo, estructuraClusters = añadirAlGrafo(grafo, fil, columna, mapaPintar[fil,columna], mapaPintar[fil,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster, estructuraClusters)

                c = 0

    return mapaPintar, indice, grafo, estructuraClusters

def añadirConexionesIntraClusters(grafo, numClusters, tamCluster, conexiones, mapa):
        estructuraClusters=[]

        for i in conexiones:
            estructuraClusters.append(i.copy())
        for i in range(len(estructuraClusters)):
            print(i)

            dentroClusters = estructuraClusters[i]

            while len(dentroClusters)>1:
                malla = Mapa("provisional", 512, 512, mapa)
                malla.construyeNodos()
                dijkstra = Dijkstra(malla)
                inicio = dentroClusters.pop()
                camino = dijkstra.findPath(inicio[0], inicio[1], dentroClusters, (inicio[0]//tamCluster)*tamCluster, (inicio[1]//tamCluster)*tamCluster, tamCluster)
                if camino != None:
                    for r in camino:
                        grafo.add_edge(inicio, r[2], r[1], r[0])
        return grafo, conexiones

if __name__ == '__main__':
    sys.setrecursionlimit(300000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=mapas)
    thread.start()
