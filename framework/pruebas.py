from TratadorMapas import *
import pickle
import numpy as np
from PIL import Image
from Nodos import NodoArbol
from Agente import Agente
from Nodos import *
import matplotlib.pyplot as plt
from Grafo import *
from controlador  import *
def main():

    s = calcularHPA()
    print(s[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
