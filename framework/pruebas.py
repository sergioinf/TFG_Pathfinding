import heapq
import math
import pickle
from Agente import *
from Nodos import *
import matplotlib.pyplot as plt
import controlador
from ctypes import c_float, c_int32, cast, byref, POINTER
def main():

    j = open("mapasTratados\\mapasHPA32.txt", "rb")
    lista=pickle.load(j)
    mapa32 = lista[3]
    j.close()
    print("Cargo los mapas")
    mapaEscribir = mapa32.mapa.__copy__()
    grafo = mapa32.grafoAbstracto





    lista = grafo.get_vertices()
    for i in lista:
        for j in grafo.vert_dict[i].get_connections():
            sig = grafo.vert_dict[j.id]
            camino = grafo.vert_dict[i].get_camino(sig)
            print(camino)
            if camino==None:
                camino = sig.get_camino(grafo.vert_dict[i])
            if camino != None:
                for c in camino:
                    mapaEscribir[c.fila, c.columna]="X"
    for i in grafo.get_vertices():
        fila = i.fila
        col = i.columna
        mapaEscribir[fila, col]="S"
    f= open("salidas\\pruebaConector.txt", "w")
    for i in range(0, 512):
        f.write(''.join(mapaEscribir[i,:]))
        f.write("\n")
    f.close()



if __name__ == '__main__':
    main()
