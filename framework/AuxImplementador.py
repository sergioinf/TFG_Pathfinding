from TratadorMapas import *
import pickle
import numpy as np
from PIL import Image
from Nodos import NodoArbol
from Agente import Agente
from Mapas import *
from Nodos import *
from Grafo import *
import matplotlib.pyplot as plt
import sys


def main():
    sys.setrecursionlimit(30000)
    mapa = crearMapa()
    lista =[mapa]
    c = open("mapasTratados\\mapaPrueba.txt", "wb")
    pickle.dump(lista, c)
    c.close()


    j = open("mapasTratados\\mapaPrueba.txt", "rb")
    lista=pickle.load(j)
    mapa = lista[0]
    j.close()

    g = mapa.grafoAbstracto.__copy__()

    #Pintar conexiones predefinidas
    """for i in g:
        for j in i.get_connections():
            camino = i.get_camino(j)
            if camino != None:
                pass
                #print(camino)
                for c in camino:
                    mapa.mapa[c.fila, c.columna]='X'

    f= open("salidas\\caminoHPA.txt", "w")

    for i in range(0, 512):
        f.write(''.join(mapa.mapa[i,:]))
        f.write("\n")
    f.close()"""

    numClustersPorFila = mapa.dimensiones//mapa.tamCluster
    cI = (197 // mapa.tamCluster)*numClustersPorFila+(319 // mapa.tamCluster)
    cD = (201 // mapa.tamCluster)*numClustersPorFila+(87 // mapa.tamCluster)

    inicial = NodoGrafo("S", 197, 319, cI)
    final = NodoGrafo("D", 201,87, cD)

    I = []
    D = []

    for i in mapa.grafoAbstracto.get_vertices():
        if i.cluster == cI:
            I.append(i)
        elif i.cluster == cD:
            D.append(i)

    agente = Agente(m = mapa.mapa)

    print("Empieza dijkstra para I")
    agente.inicial = NodoArbol(inicial.fila, inicial.columna)
    resultadosI = agente.dijkstra(I, (inicial.fila//mapa.tamCluster)*mapa.tamCluster, (inicial.columna//mapa.tamCluster)*mapa.tamCluster, mapa.tamCluster)
    print("Empieza dijkstra para D")
    agente.inicial = NodoArbol(final.fila, final.columna)
    resultadosD = agente.dijkstra(D, (final.fila//mapa.tamCluster)*mapa.tamCluster, (final.columna//mapa.tamCluster)*mapa.tamCluster, mapa.tamCluster)


    if resultadosI!=None:
        print("resultados I")
        for r in resultadosI:
            fila = r[0].fila
            columna = r[0].columna
            """print(fila)
            print(columna)
            print("")"""
            n = g.get_verticeComp(fila, columna).id
            g.add_edge(inicial, n, r[2], r[1])
            #g.add_edge(n, inicial, r[2], r[1])



    if resultadosD!=None:
        print("resultados D")
        for r in resultadosD:
            fila = r[0].fila
            columna = r[0].columna
            n = g.get_verticeComp(fila, columna).id
            g.add_edge(final, n, r[2], r[1])
            #g.add_edge(n, final, r[2], r[1])




    f= open("salidas\\hpaPruebaGrafo.txt", "w")

    for i in g:
        f.write(i.__str__())
        f.write("\n")
    f.close()

    agente.inicial = NodoArbol(fila=inicial.fila, columna=inicial.columna)
    agente.objetivo = NodoArbol(fila=final.fila, columna=final.columna)
    camino, datos, costeTotal = agente.hpaEstrella(g)


    for i in camino:
        mapa.mapa[i.fila, i.columna]='X'

    f= open("salidas\\caminoHPA.txt", "w")

    for i in range(0, 512):
        f.write(''.join(mapa.mapa[i,:]))
        f.write("\n")
    f.close()





def crearMapa():
    mapa = leerMapa()
    tamaños = divisores(len(mapa))
    tamañoCluster = tamaños[5]
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
    grafo = Graph()

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

    return MapaHPA("BGMAP (4).map", len(mapa), mapa, grafo, tamañoCluster, clusters)

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

def leerMapa():
    fichero = open("mapas\\BGMAP (4).map")
    #fichero = open("mapas\\mapaPrueba.map")
    leido = fichero.readlines()

    longitud =  len(leido)
    mapa = np.empty([longitud-4, longitud-4], dtype=str)

    j=0
    for i in range(4,longitud):
        mapa[j,:] = list(leido[i][0:512])
        j+=1

    return mapa

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
                resultados = agente.dijkstra(c, (inicio.fila//tamCluster)*tamCluster, (inicio.columna//tamCluster)*tamCluster, tamCluster)
                if resultados!=None:
                    for r in resultados:
                        grafo.add_edge(inicio, r[0], r[2], r[1])
        return grafo

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
