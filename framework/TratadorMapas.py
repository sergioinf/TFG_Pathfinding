import pickle

from Mapa import *
import numpy as np
import os

def main():
    directory = "mapas"
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    listaMapas = []
    for i in range(1, number_of_files+1):
        listaMapas.append(leerMapa("BGMAP ("+str(i)+").map"))

    f = open("mapas\\mapas.txt", "wb")
    pickle.dump(listaMapas, f)
    f.close()


def leerMapa(nombreFichero):
    fichero = open("mapas\\"+nombreFichero)
    leido = fichero.readlines()

    longitud =  len(leido)-4
    mapa = np.empty([longitud, longitud], dtype=str)

    for i in range(4,longitud):
        mapa[i-4,:] = list(leido[i][0:512])

    return Mapa(nombreFichero, longitud, mapa)



if __name__ == '__main__':
    main()
