import pickle
from PIL import Image
import TratadorMapas
import matplotlib.pyplot as plt
from Agente import *

from NodoArbol import *

def calcular():

    j = open("mapas\\mapasBase.txt", "rb")
    listamapas=pickle.load(j)
    j.close()

    mapa = listamapas[3]
    inicial = NodoArbol(197, 319)
    final = NodoArbol(201,87)
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

    mapa2 = np.empty([mapa.dimensiones, mapa.dimensiones], dtype=int)

    for i in range(0, 512):
        for j in range(0, 512):
            if mapa.mapa[i,j]=='@':
                mapa2[i,j]=0
            elif mapa.mapa[i,j]=='.':
                mapa2[i,j]=255
            else:
                mapa2[i,j] =ord(mapa.mapa[i,j])

    plt.imsave("prueba.jpg", mapa2, cmap='Greys')
    ventana=[resultado[1], "prueba.jpg"]

    return ventana
