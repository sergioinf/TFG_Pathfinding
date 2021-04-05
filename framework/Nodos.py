
import numpy as np

class NodoArbol:
    def __init__(self, fila, columna, padreF=-1, padreC=-1, estimacion=0, camino=0):
        self.f=estimacion
        self.g=camino
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

        #return np.sqrt((difColumnas**2)+(difFilas**2))  #Euclidea
        return minimo*1414+(maximo-minimo)*1000         #Octil
        #return difColumnas+difFilas  #Manhattan

    def calculaSucesores(self, mapa, objetivo):
        sucesores=[]
        dimensiones = len(mapa)

        nuevog=self.g+1000
        #Arriba
        if self.fila-1>=0 and mapa[self.fila-1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna, self.fila, self.columna, self.h(self.fila-1, self.columna, objetivo)+nuevog, nuevog))
        #Abajo
        if self.fila+1<dimensiones and mapa[self.fila+1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna, self.fila, self.columna, self.h(self.fila+1, self.columna, objetivo)+nuevog, nuevog))
        #Izquierda
        if self.columna-1>=0 and mapa[self.fila, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna-1, self.fila, self.columna, self.h(self.fila, self.columna-1, objetivo)+nuevog, nuevog))
        #Derecha
        if self.columna+1<dimensiones and mapa[self.fila, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna+1, self.fila, self.columna, self.h(self.fila, self.columna+1, objetivo)+nuevog, nuevog))

        nuevog=self.g+1414

        #Arriba izquierda
        if self.fila-1>=0 and self.columna-1>=0 and mapa[self.fila-1, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna-1, self.fila, self.columna, self.h(self.fila-1, self.columna-1, objetivo)+nuevog, nuevog))
        #Arriba derecha
        if self.fila-1>=0 and self.columna+1<dimensiones and mapa[self.fila-1, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna+1, self.fila, self.columna, self.h(self.fila-1, self.columna+1, objetivo)+nuevog, nuevog))
        #Abajo izquierda
        if self.fila+1<dimensiones and self.columna-1>=0 and mapa[self.fila+1, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna-1, self.fila, self.columna, self.h(self.fila+1, self.columna-1, objetivo)+nuevog, nuevog))
        #Abajo derecha
        if self.fila+1<dimensiones and self.columna+1<dimensiones and mapa[self.fila+1, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna+1, self.fila, self.columna, self.h(self.fila+1, self.columna+1, objetivo)+nuevog, nuevog))

        return sucesores

    def costeArco(self, nDestino):
        movX=abs(self.fila-nDestino.fila)
        movY=abs(self.columna-nDestino.columna)

        if movX+movY==2:
            return 1414
        else:
            return 1000


class NodoGrafo:
    def __init__(self, nombre, fila=None, columna = None, cluster = 0):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.cluster = cluster

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.nombre==other.nombre
        else:
            return False

    def __hash__(self):
        return hash(self.nombre)

    def __str__(self):
        return self.nombre+" Cluster: "+str(self.cluster)+" Fila: "+str(self.fila)+" Columna: "+str(self.columna)

    def __repr__(self):
        return str(self)

    def añadirConexion(self, arco):
        self.listaSucesores.append(arco)

    def eliminarConexion(self, arco):
        pass
