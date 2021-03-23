import pickle

import TratadorMapas

from Agente import *

from NodoArbol import *

def calcular():

    j = open("mapas.txt", "rb")
    listamapas=pickle.load(j)
    j.close()

    mapa = listamapas[3]
    inicial = NodoArbol(109, 177, -1, -1, 0, 0)
    final = NodoArbol(62,153, -1, -1, 0, 0)
    agente = Agente(inicial, final, mapa.mapa)

    #return agente.aEstrella()
    resultado = agente.aEstrella()
    listaSol = resultado[0]

    for i in listaSol:
        mapa.mapa[i.fila, i.columna]="X"

    f= open("solucion.txt", "w")

    for i in range(0, 512):
        f.write(''.join(mapa.mapa[i,:]))
        f.write("\n")
    f.close()

    return resultado[1]
