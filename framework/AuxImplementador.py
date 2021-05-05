import time
from random import random, randint
from controlador import *
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
    pos=3
    nPuntos=10
    j = open("mapasTratados\\mapasHPA4.txt", "rb")
    lista=pickle.load(j)
    mapa4 = lista[pos]
    j.close()
    j = open("mapasTratados\\mapasHPA8.txt", "rb")
    lista=pickle.load(j)
    mapa8 = lista[pos]
    j.close()
    j = open("mapasTratados\\mapasHPA16.txt", "rb")
    lista=pickle.load(j)
    mapa16 = lista[pos]
    j.close()
    j = open("mapasTratados\\mapasHPA32.txt", "rb")
    lista=pickle.load(j)
    mapa32 = lista[pos]
    j.close()
    print("Cargo los mapas")

    tiemposA = []
    itsA=[]

    tiemposHPA4 = []
    itsHPA4=[]

    tiemposHPA8 = []
    itsHPA8=[]

    tiemposHPA16 = []
    itsHPA16=[]

    tiemposHPA32 = []
    itsHPA32=[]

    listaInicio, listaFinal = creaPuntos(mapa4, nPuntos)
    cont=0
    for pos in range(0, len(listaInicio)):
        print(cont)
        cont+=1
        S=listaInicio[pos]
        G=listaFinal[pos]

        filaS=S[0]
        colS=S[1]
        filaG=G[0]
        colG=G[1]
        mapaA = Mapa(mapa4.nombre, mapa4.dimensiones, mapa4.mapa.__copy__())
        resultadoA = calcularA(mapaA, filaS, colS, filaG, colG, Agente(), True)
        if resultadoA!= None:
            tiemposA.append(NodoLista(resultadoA[2],resultadoA[0]))
            itsA.append(NodoLista(resultadoA[2],resultadoA[1]))

        for i in [mapa4, mapa8, mapa16, mapa32]:
            resultadoHPA = calcularHPA(i, filaS, colS, filaG, colG, True)

            if resultadoHPA!=None:
                if i.tamCluster==4:
                    tiemposHPA4.append(NodoLista(resultadoHPA[2], resultadoHPA[0]))
                    itsHPA4.append(NodoLista(resultadoHPA[2], resultadoHPA[1]))
                elif i.tamCluster==8:
                    tiemposHPA8.append(NodoLista(resultadoHPA[2], resultadoHPA[0]))
                    itsHPA8.append(NodoLista(resultadoHPA[2], resultadoHPA[1]))
                elif i.tamCluster==16:
                    tiemposHPA16.append(NodoLista(resultadoHPA[2], resultadoHPA[0]))
                    itsHPA16.append(NodoLista(resultadoHPA[2], resultadoHPA[1]))
                else:
                    tiemposHPA32.append(NodoLista(resultadoHPA[2], resultadoHPA[0]))
                    itsHPA32.append(NodoLista(resultadoHPA[2], resultadoHPA[1]))
    tiemposHPA32.sort()
    tiemposHPA16.sort()
    tiemposHPA8.sort()
    tiemposHPA4.sort()
    tiemposA.sort()

    itsHPA32.sort()
    itsHPA16.sort()
    itsHPA8.sort()
    itsHPA4.sort()
    itsA.sort()

    t32 = []
    t16= []
    t8= []
    t4= []
    tA= []
    it32= []
    it16= []
    it8= []
    it4= []
    itA= []
    dista = []
    dist32= []
    dist16= []
    dist8= []
    dist4= []
    for i in range(0,len(tiemposHPA32)):
        t32.append(tiemposHPA32[i].y)
        dist32.append(tiemposHPA32[i].x)
        it32.append(itsHPA32[i].y)
    for i in range(0,len(tiemposHPA16)):
        dist16.append(tiemposHPA16[i].x)
        t16.append(tiemposHPA16[i].y)
        it16.append(itsHPA16[i].y)
    for i in range(0,len(tiemposHPA8)):
        dist8.append(tiemposHPA8[i].x)
        t8.append(tiemposHPA8[i].y)
        it8.append(itsHPA8[i].y)
    for i in range(0,len(tiemposHPA4)):
        dist4.append(tiemposHPA4[i].x)
        t4.append(tiemposHPA4[i].y)
        it4.append(itsHPA4[i].y)
    for i in range(0,len(tiemposA)):
        tA.append(tiemposA[i].y)
        itA.append(itsA[i].y)
        dista.append(itsA[i].x)



    plt.plot(dista,tA,  'o-', label="A*" )
    plt.plot(dist4 ,t4 , "+-", label="HPA* TC:4")
    plt.plot(dist8, t8, "v-", label="HPA* TC:8")
    plt.plot(dist16, t16, "*-", label="HPA* TC:16")
    plt.plot(dist32, t32, "1-", label="HPA* TC:32")
    plt.xlabel("Distancia de la solución")
    plt.ylabel("Tiempo de CPU")
    plt.title("Tiempo / Distancia")
    plt.legend()
    plt.savefig("salidas/compAHPAT.png", dpi=300)
    plt.close()

    plt.plot(dista,itA,  'o-', label="A*" )
    plt.plot(dist4 ,it4 , "+-", label="HPA* TC:4")
    plt.plot(dist8, it8, "v-", label="HPA* TC:8")
    plt.plot(dist16, it16, "*-", label="HPA* TC:16")
    plt.plot(dist32, it32, "1-", label="HPA* TC:32")
    plt.xlabel("Distancia de la solución")
    plt.ylabel("Nodos expandidos")
    plt.title("Nodos expandidos / Distancia")
    plt.legend()
    plt.savefig("salidas/compAHPAEXP.png", dpi=300)
    plt.show()

    return "salidas/compAHPAT.png", "salidas/compAHPAEXP.png"




def creaPuntos(mapa, nPuntos):
    listaInicio =[]
    listaFinal = []

    while len(listaFinal)<nPuntos:
        filaI = randint(0, mapa.dimensiones-1)
        colI = randint(0, mapa.dimensiones-1)

        filaF = randint(0, mapa.dimensiones-1)
        colF = randint(0, mapa.dimensiones-1)

        if mapa.mapa[filaI, colI]=='.' and mapa.mapa[filaF, colF]=='.':
            listaInicio.append((filaI, colI))
            listaFinal.append((filaF, colF))
    return listaInicio, listaFinal




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
