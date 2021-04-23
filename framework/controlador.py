import pickle
from PIL import Image
import TratadorMapas
import matplotlib.pyplot as plt
from Agente import *

from Nodos import *

def calcularA():

    j = open("mapasTratados\\mapasBase1.txt", "rb")
    listamapas=pickle.load(j)
    j.close()

    mapa = listamapas[0]
    inicial = NodoArbol(197, 319)
    final = NodoArbol(201,87)
    agente = Agente(inicial, final, mapa.mapa)

    #return agente.aEstrella()
    resultado = agente.aEstrella()
    listaSol = resultado[0]

    for i in listaSol:
        mapa.mapa[i.fila, i.columna]="X"

    f= open("salidas\\solucionA.txt", "w")

    for i in range(0, 512):
        f.write(''.join(mapa.mapa[i,:]))
        f.write("\n")
    f.close()

    mapa2 = np.empty([mapa.dimensiones, mapa.dimensiones], dtype=int)

    for i in range(0, 512):
        for j in range(0, 512):
            if mapa.mapa[i,j]=='@':
                mapa2[i,j]=0
            elif mapa.mapa[i,j]=='.':
                mapa2[i,j]=255
            else:
                mapa2[i,j] =ord(mapa.mapa[i,j])

    plt.imsave("salidas\\imagenA.jpg", mapa2, cmap='Greys')
    ventana=[resultado[1], "salidas\\imagenA.jpg"]

    return ventana


def calcularHPA():
    j = open("mapasTratados\\mapasHPA1.txt", "rb")
    lista=pickle.load(j)
    mapa = lista[0]
    j.close()

    g = mapa.grafoAbstracto.__copy__()

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

    f= open("salidas\\solucionHPA.txt", "w")

    for i in range(0, 512):
        f.write(''.join(mapa.mapa[i,:]))
        f.write("\n")
    f.close()

    mapa2 = np.empty([mapa.dimensiones, mapa.dimensiones], dtype=int)

    for i in range(0, 512):
        for j in range(0, 512):
            if mapa.mapa[i,j]=='@':
                mapa2[i,j]=0
            elif mapa.mapa[i,j]=='.':
                mapa2[i,j]=255
            else:
                mapa2[i,j] =ord(mapa.mapa[i,j])

    plt.imsave("salidas\\imagenHPA.jpg", mapa2, cmap='Greys')
    ventana=[datos, "salidas\\imagenHPA.jpg"]

    return ventana
