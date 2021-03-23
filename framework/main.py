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

    f= open("solucion.txt", "w")

    for i in range(0, 512):
        f.write(''.join(mapa.mapa[i,:]))
        f.write("\n")
    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




