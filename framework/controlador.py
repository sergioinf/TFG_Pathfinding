
from TratadorMapas import TratadorMapas
from Agente import *

from NodoArbol import NodoArbol

def calcular():
    tratador=TratadorMapas()
    mapa = tratador.leerMapa("")
    inicial = NodoArbol(109, 177, -1, -1, 0, 0)
    final = NodoArbol(62,153, -1, -1, 0, 0)
    agente = Agente(inicial, final, mapa)

    return agente.aEstrella()
