#########
#Imports
#########

import math
import numpy as np
import pickle

#########
#Metodos
#########


def recuperaCamino(nodo):

    camino = [[nodo.fila, nodo.columna]]

    while (nodo.padre):
        nodo = nodo.padre
        camino.append([nodo.fila, nodo.columna])

    camino.reverse()

    return camino





























