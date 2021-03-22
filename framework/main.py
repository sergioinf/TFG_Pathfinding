from TratadorMapas import TratadorMapas
import pickle
import numpy as np
from NodoArbol import NodoArbol
from Agente import Agente
from Mapa import *

def main():

    tratador=TratadorMapas()
    #mapa = tratador.leerMapa("")
    map = Mapa("BaldursGate1", 512, mapa)


    f = open("guardar.txt", "wb")
    pickle.dump(map, f)
    f.close()

    j = open("guardar.txt", "rb")
    objeto=pickle.load(j)
    n=objeto.nombre
    d=objeto.dimensiones
    m=objeto.mapa

    j.close()

    print(n)
    print(d)
    print(m)
    for i in range(0, 512):
        print(m[i,:])

    """
    inicial = NodoArbol(109, 177, -1, -1, 0, 0)
    final = NodoArbol(62,153, -1, -1, 0, 0)
    agente = Agente(inicial, final, mapa)

    listaSol = agente.aEstrella()

    for i in listaSol:
        mapa[i.fila, i.columna]="X"

    f= open("mapas\\", "w")

    for i in range(0, 512):
        f.write(''.join(mapa[i,:]))
        f.write("\n")
    f.close()
    """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




