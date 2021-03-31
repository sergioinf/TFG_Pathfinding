from TratadorMapas import *
import pickle
import numpy as np
from PIL import Image
from NodoArbol import NodoArbol
from Agente import Agente
from Mapa import *
import matplotlib.pyplot as plt

def main():
    j = open("mapas\\mapasBase.txt", "rb")
    listamapas=pickle.load(j)
    j.close()

    #mapa = listamapas[3]

    #tamaños = divisores(512)
    #tamañoCluster = tamaños[7]

    tamañoCluster = 3
    pGrande=3
    mapa = [['.  ','.  ','@  ','.  ','.  ','.  ','.  ','.  ','.  '],
            ['.  ','.  ','@  ','.  ','@  ','@  ','.  ','.  ','.  '],
            ['.  ','.  ','@  ','.  ','@  ','.  ','.  ','.  ','.  '],
            ['.  ','.  ','@  ','  .','@  ','@  ','@  ','@  ','@  '],
            ['.  ','.  ','@  ','.  ','.  ','.  ','.  ','.  ','.  '],
            ['.  ','.  ','.  ','.  ','.  ','.  ','.  ','@  ','.  '],
            ['.  ','.  ','.  ','.  ','@  ','@  ','.  ','@  ','.  '],
            ['.  ','.  ','.  ','.  ','.  ','@  ','.  ','@  ','.  '],
            ['.  ','.  ','.  ','.  ','.  ','.  ','.  ','@  ','.  ']]


           #[['.  ','.  ','@  ','.  ','.  ','N1 ','N2 ','.  ','.  '],
            #['.  ','.  ','@  ','.  ','@  ','@  ','.  ','.  ','.  '],
            #['.  ','.  ','@  ','.  ','@  ','N3 ','N4 ','.  ','.  '],
            #['.  ','.  ','@  ','  .','@  ','@  ','@  ','@  ','@  '],
            #['.  ','.  ','@  ','.  ','.  ','.  ','.  ','.  ','.  '],
            #['.  ','.  ','N7 ','N8 ','.  ','N5 ','N6 ','@  ','.  '],
            #['.  ','.  ','N11','N12','@  ','@  ','.  ','@  ','.  '],
            #['.  ','.  ','.  ','.  ','.  ','@  ','.  ','@  ','.  '],
            #['.  ','.  ','N13','N14','.  ','N9 ','N10','@  ','.  ']]

            #['.  ' '.  ' '@  '|'.  ' '.  ' 'N2 '|'N3 ' '.  ' '.  ']
            #['.  ' '.  ' '@  '|'.  ' '@  ' '@  '|'.  ' '.  ' '.  ']
            #['.  ' 'N0 ' '@  '|'.  ' '@  ' 'N4 '|'N5 ' '.  ' '.  ']
            #-------------------------------------------------------
            #['.  ' 'N1 ' '@  '|'  .' '@  ' '@  '|'@  ' '@  ' '@  ']
            #['.  ' '.  ' '@  '|'.  ' '.  ' 'N11'|'N12' '.  ' '.  ']
            #['N8 ' '.  ' 'N6 '|'N10' '.  ' '.  '|'N18' '@  ' 'N20']
            #-------------------------------------------------------
            #['N9 ' '.  ' 'N7 '|'N13' '@  ' '@  '|'N19' '@  ' 'N21']
            #['.  ' '.  ' '.  '|'.  ' '.  ' '@  '|'.  ' '@  ' '.  ']
            #['.  ' '.  ' 'N14'|'N15' '.  ' 'N16'|'N17' '@  ' '.  ']

    clusters = []
    numClusters= len(mapa)//tamañoCluster
    for i in range(0,numClusters):
        for j in range(0, numClusters):
            clusters.append((i*tamañoCluster,j*tamañoCluster))

    print(clusters)

    mapaPintar = mapa.copy()


    print()

    indice=0
    for i in clusters:
        print(mapaPintar)
        print()
        c = 0
        for j in range(i[0], i[0]+tamañoCluster):

            if i[1]+tamañoCluster==len(mapaPintar):
                break

            columna = i[1]+tamañoCluster-1

            if mapa[j][columna]=='.  ' and mapa[j][columna+1]=='.  ':
                c+=1
            else:
                if c==1:
                    if mapaPintar[j-1][columna]=='.  ':
                        mapaPintar[j-1][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-1][columna+1]=='.  ':
                        mapaPintar[j-1][columna+1]='N'+str(indice)
                        indice+=1
                    c=0

            if c==tamañoCluster:
                if mapaPintar[j][columna]=='.  ':
                    mapaPintar[j][columna]='N'+str(indice)
                    indice+=1
                if mapaPintar[j][columna+1]=='.  ':
                    mapaPintar[j][columna+1]='N'+str(indice)
                    indice+=1
                if mapaPintar[j-c+1][columna]=='.  ':
                    mapaPintar[j-c+1][columna]='N'+str(indice)
                    indice+=1
                if mapaPintar[j-c+1][columna+1]=='.  ':
                    mapaPintar[j-c+1][columna+1]='N'+str(indice)
                    indice+=1
            elif j%tamañoCluster+1==tamañoCluster and c!=0:
                if c>=pGrande:
                    if mapaPintar[j][columna]=='.  ':
                        mapaPintar[j][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j][columna+1]=='.  ':
                        mapaPintar[j][columna+1]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-c+1][columna]=='.  ':
                        mapaPintar[j-c+1][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-c+1][columna+1]=='.  ':
                        mapaPintar[j-c+1][columna+1]='N'+str(indice)
                        indice+=1
                else:
                    if mapaPintar[j-(c//2)][columna]=='.  ':
                        mapaPintar[j-(c//2)][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-(c//2)][columna+1]=='.  ':
                        mapaPintar[j-(c//2)][columna+1]='N'+str(indice)
                        indice+=1
        print(mapaPintar)
        print()
##Columnas
        c = 0
        mapaPintar=np.transpose(mapaPintar)
        mapa=np.transpose(mapa)
        for j in range(i[0], i[0]+tamañoCluster):

            if i[1]+tamañoCluster==len(mapaPintar):
                break

            columna = i[1]+tamañoCluster-1

            if mapa[j][columna]=='.  ' and mapa[j][columna+1]=='.  ':
                c+=1
            else:
                if c==1:
                    if mapaPintar[j-1][columna]=='.  ':
                        mapaPintar[j-1][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-1][columna+1]=='.  ':
                        mapaPintar[j-1][columna+1]='N'+str(indice)
                        indice+=1
                    c=0

            if c==tamañoCluster:
                if mapaPintar[j][columna]=='.  ':
                    mapaPintar[j][columna]='N'+str(indice)
                    indice+=1
                if mapaPintar[j][columna+1]=='.  ':
                    mapaPintar[j][columna+1]='N'+str(indice)
                    indice+=1
                if mapaPintar[j-c+1][columna]=='.  ':
                    mapaPintar[j-c+1][columna]='N'+str(indice)
                    indice+=1
                if mapaPintar[j-c+1][columna+1]=='.  ':
                    mapaPintar[j-c+1][columna+1]='N'+str(indice)
                    indice+=1
            elif j%tamañoCluster+1==tamañoCluster and c!=0:
                if c>=pGrande:
                    if mapaPintar[j][columna]=='.  ':
                        mapaPintar[j][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j][columna+1]=='.  ':
                        mapaPintar[j][columna+1]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-c+1][columna]=='.  ':
                        mapaPintar[j-c+1][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-c+1][columna+1]=='.  ':
                        mapaPintar[j-c+1][columna+1]='N'+str(indice)
                        indice+=1
                else:
                    if mapaPintar[j-(c//2)][columna]=='.  ':
                        mapaPintar[j-(c//2)][columna]='N'+str(indice)
                        indice+=1
                    if mapaPintar[j-(c//2)][columna+1]=='.  ':
                        mapaPintar[j-(c//2)][columna+1]='N'+str(indice)
                        indice+=1
        mapaPintar=np.transpose(mapaPintar)
        mapa=np.transpose(mapa)


    print(mapaPintar[0])
    print(mapaPintar[1])
    print(mapaPintar[2])
    print(mapaPintar[3])
    print(mapaPintar[4])
    print(mapaPintar[5])
    print(mapaPintar[6])
    print(mapaPintar[7])
    print(mapaPintar[8])









def divisores(n):
    divisores=[]
    for i in range (1, n):
        if n%i==0:
            divisores.append(i)
    return divisores




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/




