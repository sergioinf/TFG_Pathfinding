from TratadorMapas import *
import pickle
import numpy as np
from PIL import Image
from Nodos import NodoArbol
from Agente import Agente
from Nodos import *
import matplotlib.pyplot as plt
from Grafo import *
def main():

    lista = ['a', 'b', 'c', 'd','e','f', 'g', 'h','i','j','k']
    aux = 1
    for j in lista:
        print(j)
        for i in lista[aux:len(lista)]:
            print(i)
        print("Siguiente:")

        aux+=1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




