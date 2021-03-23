from TratadorMapas import *
import pickle
import numpy as np
from NodoArbol import NodoArbol
from Agente import Agente
from Mapa import *

def main():
    j = open("mapas.txt", "rb")
    listamapas=pickle.load(j)
    j.close()
    mapa = listamapas[3]

    inicial = NodoArbol(109, 177, -1, -1, 0, 0)
    final = NodoArbol(96,133, -1, -1, 0, 0)

    agente = Agente(inicial, final, mapa.mapa)

    agente.aEstrella()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




