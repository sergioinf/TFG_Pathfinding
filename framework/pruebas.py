import time
from random import random, randint

from TratadorMapas import *
import pickle
import numpy as np
from PIL import Image
from Nodos import NodoArbol
from Agente import Agente
from Mapas import *
from Nodos import *
from Grafo import *
import matplotlib.pyplot as plt
import sys

def main():
    x = np.arange(10.)
    y =[4,8,3,7,9,4,3,67,9,0]

    x2=[12,0,23,7,9,14,3,6,4,8]
    x2.sort()
    y2=[4,8,0,3,7,13,6,9,4,5]

    plt.plot(x, y, 'o-', label="uno")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend()
    #savefig("salidas/grafica.png", dpi=300)
    plt.show()

    plt.plot(x2, y2, "+-", label="dos")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend()
    #savefig("salidas/grafica.png", dpi=300)
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
