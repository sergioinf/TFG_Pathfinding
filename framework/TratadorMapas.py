import pickle

from Mapa import *
import numpy as np
import os

def main():
    directory = "mapas"
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

    listaMapas = []
    for i in range(1, number_of_files):
        listaMapas.append(leerMapa("BGMAP ("+str(i)+").map"))

    f= open("prueba.txt", "w")

    for i in range(0, 512):
        f.write(''.join(listaMapas[0].mapa[i,:]))
        f.write("\n")
    f.close()

    f = open("mapas\\mapasBase.txt", "wb")
    pickle.dump(listaMapas, f)
    f.close()


def leerMapa(nombreFichero):
    fichero = open("mapas\\"+nombreFichero)
    leido = fichero.readlines()

    longitud =  len(leido)
    mapa = np.empty([longitud-4, longitud-4], dtype=str)

    j=0
    for i in range(4,longitud):
        mapa[j,:] = list(leido[i][0:512])
        j+=1

    return Mapa(nombreFichero, longitud-4, mapa)



if __name__ == '__main__':
    main()
