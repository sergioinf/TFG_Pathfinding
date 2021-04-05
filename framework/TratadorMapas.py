import pickle

from Mapas import *
import numpy as np
import os


def main():
    directory = "mapas"
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    listaMapas = []
    listaMapasHPA = []
    for i in range(1, number_of_files):

        nombre = "BGMAP ("+str(i)+").map"
        mapa = leerMapa(nombre)
        l = len(mapa)

        print(nombre)
        listaMapas.append(Mapa(nombre, l, mapa))
        listaMapasHPA.append(crearMapaHPA(nombre, l, mapa))

    f = open("mapasTratados\\mapasBase.txt", "wb")
    pickle.dump(listaMapas, f)
    f.close()

    c = open("mapasTratados\\mapasHPA.txt", "wb")
    pickle.dump(listaMapasHPA, c)
    c.close()


def leerMapa(nombreFichero):
    fichero = open("mapas\\"+nombreFichero)
    leido = fichero.readlines()

    longitud =  len(leido)
    mapa = np.empty([longitud-4, longitud-4], dtype=str)

    j=0
    for i in range(4,longitud):
        mapa[j,:] = list(leido[i][0:512])
        j+=1

    return mapa


def crearMapaHPA(nombre, l, mapa):

    tamaños = divisores(l)
    tamañoCluster = tamaños[7]
    pGrande = 3

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
    grafo = Graph()

    for i in clusters:
        if i[1] + tamañoCluster < len(mapa):

            clusterActual = (i[0] // tamañoCluster)*numClustersPorFila+(i[1] // tamañoCluster)
            ##Conexiones horizontales
            mapaPintar, indice, grafo= calculaPuertas(mapa, mapaPintar, tamañoCluster, indice, pGrande, i[0], i[1], grafo, clusterActual, False)
            ##Conexiones verticales
            mapaPintar = np.transpose(mapaPintar)
            mapa = np.transpose(mapa)
            clusterActual = (i[1] // tamañoCluster)*numClustersPorFila+(i[0] // tamañoCluster)

            mapaPintar, indice, grafo= calculaPuertas(mapa, mapaPintar, tamañoCluster, indice, pGrande, i[0], i[1], grafo, clusterActual, True)
            mapaPintar = np.transpose(mapaPintar)
            mapa = np.transpose(mapa)


    agente = Agente(m=mapa)

    añadirConexionesIntraClusters(agente, grafo)

    return MapaHPA(nombre, l, mapa, grafo, tamañoCluster, len(clusters))

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

    esta1 = g.get_vertex(Nodo)!= None
    esta2 = g.get_vertex(Nodo2)!=None

    #print(Nodo.cluster)
    #print(Nodo2.cluster)
    if esta1 and esta2:
        g.add_edge(Nodo, Nodo2, 1)
    elif esta1:
        g.add_vertex(Nodo2)
        g.add_edge(Nodo, Nodo2, 1)
    elif esta2:
        g.add_vertex(Nodo)
        g.add_edge(Nodo, Nodo2, 1)
    else:
        g.add_vertex(Nodo)
        g.add_vertex(Nodo2)
        g.add_edge(Nodo, Nodo2, 1)
    return g

def calculaPuertas(mapa, mapaPintar, tamañoCluster, indice, pGrande, i0, i1, grafo, clusterActual, traspuesta):
    c = 0
    for j in range(i0, i0 + tamañoCluster):
        if i1 + tamañoCluster == len(mapaPintar):
            break

        columna = i1 + tamañoCluster - 1
        if mapa[j,columna] == '.' and mapa[j,columna + 1] == '.':
            c += 1
        else:
            if c == 1:
                if mapaPintar[j - 1,columna] == 0:
                    mapaPintar[j - 1,columna] = indice
                    indice += 1
                if mapaPintar[j - 1,columna + 1] == 0:
                    mapaPintar[j - 1,columna + 1] = indice
                    indice += 1
                c = 0
                #Añadiendo en el grafo

                fil = j-1
                grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[j - 1,columna], mapaPintar[j - 1,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

        if c == tamañoCluster:
            if mapaPintar[j,columna] == 0:
                mapaPintar[j,columna] = indice
                indice += 1
            if mapaPintar[j,columna + 1] == 0:
                mapaPintar[j,columna + 1] = indice
                indice += 1
            if mapaPintar[j - c + 1,columna] == 0:
                mapaPintar[j - c + 1,columna] = indice
                indice += 1
            if mapaPintar[j - c + 1,columna + 1] == 0:
                mapaPintar[j - c + 1,columna + 1] = indice
                indice += 1


            #Añadiendo en el grafo
            fil = j
            grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[j,columna], mapaPintar[j,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

             #Añadiendo en el grafo
            fil = j - c + 1
            grafo =añadirAlGrafo(grafo, fil, columna, mapaPintar[j - c + 1,columna], mapaPintar[j - c + 1,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

        elif j % tamañoCluster + 1 == tamañoCluster and c != 0:
            if c >= pGrande:
                if mapaPintar[j,columna] == 0:
                    mapaPintar[j,columna] = indice
                    indice += 1
                if mapaPintar[j,columna + 1] == 0:
                    mapaPintar[j,columna + 1] = indice
                    indice += 1
                if mapaPintar[j - c + 1,columna] == 0:
                    mapaPintar[j - c + 1,columna] = indice
                    indice += 1
                if mapaPintar[j - c + 1,columna + 1] == 0:
                    mapaPintar[j - c + 1,columna + 1] = indice
                    indice += 1


                #Añadiendo en el grafo
                fil = j
                grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[j,columna], mapaPintar[j,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)


                 #Añadiendo en el grafo
                fil = j - c + 1
                grafo =añadirAlGrafo(grafo, fil, columna, mapaPintar[j - c + 1,columna], mapaPintar[j - c + 1,columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)

            else:
                if mapaPintar[j - (c // 2),columna] == 0:
                    mapaPintar[j - (c // 2),columna] = indice
                    indice += 1
                if mapaPintar[j - (c // 2),columna + 1] == 0:
                    mapaPintar[j - (c // 2),columna + 1] = indice
                    indice += 1

                #Añadiendo en el grafo
                fil = j - (c // 2)
                grafo = añadirAlGrafo(grafo, fil, columna, mapaPintar[j - (c // 2),columna], mapaPintar[j - (c // 2),columna + 1], clusterActual, traspuesta, len(mapa)//tamañoCluster)


    return mapaPintar, indice, grafo

def leerMapa():
    fichero = open("mapas\\BGMAP (1).map")
    leido = fichero.readlines()

    longitud =  len(leido)
    mapa = np.empty([longitud-4, longitud-4], dtype=str)

    j=0
    for i in range(4,longitud):
        mapa[j,:] = list(leido[i][0:512])
        j+=1

    return mapa

def añadirConexionesIntraClusters(agente, grafo):
        vertices = grafo.get_vertices()
        aux = 1

        lista = []
        for i in vertices:
            lista.append(i)

        for i in lista:
            for j in lista[aux:len(lista)]:
                print(aux)
                if i.cluster == j.cluster:
                    agente.inicial=NodoArbol(i.fila, i.columna)
                    agente.objetivo=NodoArbol(j.fila, j.columna)
                    sol = agente.aEstrella()
                    if sol!=None:
                        grafo.add_edge(i, j, sol[2])
            aux+=1


if __name__ == '__main__':
    main()
