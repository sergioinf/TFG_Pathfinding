
import numpy as np

class NodoArbol:
    def __init__(self, fila, columna, padreF, padreC, estimacion, camino):
        self.f=estimacion
        self.g=camino
        self.cerrado=False
        self.fila=fila
        self.columna=columna
        self.puntPadreF=padreF
        self.puntPadreC=padreC

    def __str__(self):
        return str(self.fila)+", "+str(self.columna)

    def __lt__(self, other):
        if self.f==other.f:
            return self.g<other.g
        else:
            return self.f<other.f

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fila==other.fila and self.columna==other.columna
        else:
            return False

    def h(self, fila, columna, objetivo):

        difColumnas = abs(columna-objetivo.columna)
        difFilas = abs(fila-objetivo.fila)

        minimo = min(difFilas, difColumnas)
        maximo = max(difFilas, difColumnas)

        return np.sqrt((difColumnas**2)+(difFilas**2))  #Euclidea
        #return minimo*1414+(maximo-minimo)*1000         #Octil
        #return difColumnas+difFilas  #Manhattan

    def calculaSucesores(self, mapa, objetivo):
        sucesores=[]
        dimensiones = len(mapa)

        #Arriba
        if self.fila-1>=0 and mapa[self.fila-1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1000))
        #Abajo
        if self.fila+1<dimensiones and mapa[self.fila+1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1000))
        #Izquierda
        if self.columna-1>=0 and mapa[self.fila, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna-1, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1000))
        #Derecha
        if self.columna+1<dimensiones and mapa[self.fila, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna+1, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1000))

        #Arriba izquierda
        if self.fila-1>=0 and self.columna-1>=0 and mapa[self.fila-1, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna-1, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1414))
        #Arriba derecha
        if self.fila-1>=0 and self.columna+1<dimensiones and mapa[self.fila-1, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna+1, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1414))
        #Abajo izquierda
        if self.fila+1<dimensiones and self.columna-1>=0 and mapa[self.fila+1, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna-1, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1414))
        #Abajo derecha
        if self.fila+1<dimensiones and self.columna+1<dimensiones and mapa[self.fila+1, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna+1, self.fila, self.columna, self.h(self.fila, self.columna, objetivo), self.g+1414))

        return sucesores

    def costeArco(self, nDestino):
        movX=abs(self.fila-nDestino.fila)
        movY=abs(self.columna-nDestino.columna)

        if movX+movY==2:
            return 1414
        else:
            return 1000
