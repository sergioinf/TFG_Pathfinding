import time
from ctypes import c_float
from ctypes import c_float, c_int32, cast, byref, POINTER
import numpy as np
import math
class NodoArbol:
    def __init__(self, fila, columna, padreF=-1, padreC=-1, estimacion=0, camino=0):
        self.f=estimacion
        self.g=camino
        self.fila=fila
        self.columna=columna
        self.puntPadreF=padreF
        self.puntPadreC=padreC

    def __str__(self):
        return str(self.fila)+":"+str(self.columna)

    def __repr__(self):
        return str(self)

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

    def __hash__(self):
        return hash(self.fila)+hash(self.columna)

    def h(self, fila, columna, objetivo):

        difColumnas = abs(columna-objetivo.columna)
        difFilas = abs(fila-objetivo.fila)

        minimo = min(difFilas, difColumnas)
        maximo = max(difFilas, difColumnas)


        #return y  #Euclidea
        return minimo*1414+(maximo-minimo)*1000         #Octil
        #return difColumnas+difFilas  #Manhattan

    def calculaSucesores(self, mapa, objetivo):
        sucesores=[]
        dimensiones = len(mapa)

        nuevog=self.g+1000
        #Arriba
        if self.fila-1>=0 and mapa[self.fila-1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna, self.fila, self.columna, self.h(self.fila-1, self.columna, objetivo)+nuevog, nuevog))
        #Derecha
        if self.columna+1<dimensiones and mapa[self.fila, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna+1, self.fila, self.columna, self.h(self.fila, self.columna+1, objetivo)+nuevog, nuevog))
        #Abajo
        if self.fila+1<dimensiones and mapa[self.fila+1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna, self.fila, self.columna, self.h(self.fila+1, self.columna, objetivo)+nuevog, nuevog))
        #Izquierda
        if self.columna-1>=0 and mapa[self.fila, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna-1, self.fila, self.columna, self.h(self.fila, self.columna-1, objetivo)+nuevog, nuevog))


        nuevog=self.g+1414

        #Arriba izquierda
        if self.fila-1>=0 and self.columna-1>=0 and mapa[self.fila-1, self.columna-1]=='.' and (mapa[self.fila-1,self.columna]=='.' or mapa[self.fila,self.columna-1]=='.'):
            sucesores.append(NodoArbol(self.fila-1, self.columna-1, self.fila, self.columna, self.h(self.fila-1, self.columna-1, objetivo)+nuevog, nuevog))
        #Arriba derecha
        if self.fila-1>=0 and self.columna+1<dimensiones and mapa[self.fila-1, self.columna+1]=='.' and (mapa[self.fila-1,self.columna]=='.' or mapa[self.fila,self.columna+1]=='.'):
            sucesores.append(NodoArbol(self.fila-1, self.columna+1, self.fila, self.columna, self.h(self.fila-1, self.columna+1, objetivo)+nuevog, nuevog))
        #Abajo derecha
        if self.fila+1<dimensiones and self.columna+1<dimensiones and mapa[self.fila+1, self.columna+1]=='.' and (mapa[self.fila+1,self.columna]=='.' or mapa[self.fila,self.columna+1]=='.'):
            sucesores.append(NodoArbol(self.fila+1, self.columna+1, self.fila, self.columna, self.h(self.fila+1, self.columna+1, objetivo)+nuevog, nuevog))
        #Abajo izquierda
        if self.fila+1<dimensiones and self.columna-1>=0 and mapa[self.fila+1, self.columna-1]=='.' and (mapa[self.fila+1,self.columna]=='.' or mapa[self.fila,self.columna-1]=='.'):
            sucesores.append(NodoArbol(self.fila+1, self.columna-1, self.fila, self.columna, self.h(self.fila+1, self.columna-1, objetivo)+nuevog, nuevog))


        return sucesores

    def calculaSucesoresJPS(self, mapa, objetivo):
        """ Las busquedas se haran en funcion de dirVert y dirHor
        @Si alguna de las dos es 0, significa que la busqueda se hara se forma recta, es decir, horizontal o vertical
        @Si dirVert es 1, significa que es hacia abajo, si es -1 es hacia arriba
        @Si dirHor es 1, significa que es hacia la derecha, si es -1 es hacia la izquierda

        dirVert -1 |
        dirHor -1  |- Mov Arriba, izquierda

        dirVert 1  |
        dirHor 1   |- Mov Abajo, derecha

        dirVert 1  |
        dirHor -1  |- Mov Abajo, izquierda

        dirVert -1 |
        dirHor 1   |- Mov Arriba, derecha
        """


        sucesores=[]

        ps = self.saltoLineaRecta(self.fila, self.columna, -1, 0, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))
        ps = self.saltoLineaRecta(self.fila, self.columna, 0,-1, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))
        ps = self.saltoLineaRecta(self.fila, self.columna, 1,0, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))
        ps = self.saltoLineaRecta(self.fila, self.columna, 0,1, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))


        ps = self.saltoDiagonal(self.fila, self.columna, -1,-1, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))
        ps = self.saltoDiagonal(self.fila, self.columna, -1,1, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))
        ps = self.saltoDiagonal(self.fila, self.columna, 1,1, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))
        ps = self.saltoDiagonal(self.fila, self.columna, 1, -1, objetivo, mapa)
        if ps!=None:
            newG = ps[2]+self.g
            sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+newG, camino=newG))

        return sucesores

    def saltoLineaRecta(self, filaI, columnaI, direccionY, direccionX, final, mapa):
        fila_Act = filaI
        col_Act = columnaI
        coste = 0

        while True:
            fila_Act+=direccionY
            col_Act+=direccionX
            coste+=1000

            if fila_Act < 0 or fila_Act>=len(mapa) or col_Act < 0 or col_Act>=len(mapa):
                return None
            elif mapa[fila_Act, col_Act]=='@':
                return None
            if fila_Act==final.fila and col_Act==final.columna:
                return (fila_Act, col_Act, coste)

            if direccionY==0:
                if col_Act+direccionX >= 0 and col_Act+direccionX<len(mapa) and fila_Act-1 >= 0 and fila_Act-1<len(mapa):
                        if mapa[fila_Act-1, col_Act]=='@' and mapa[fila_Act-1, col_Act+direccionX]=='.':
                            return (fila_Act, col_Act, coste)
                if col_Act+direccionX >= 0 and col_Act+direccionX<len(mapa) and fila_Act+1 >= 0 and fila_Act+1<len(mapa):
                        if mapa[fila_Act+1, col_Act]=='@' and mapa[fila_Act+1, col_Act+direccionX]=='.':
                            return (fila_Act, col_Act, coste)
            else:
                if fila_Act+direccionY >= 0 and fila_Act+direccionY<len(mapa) and col_Act-1 >= 0 and col_Act-1<len(mapa):
                        if mapa[fila_Act, col_Act-1]=='@' and mapa[fila_Act+direccionY, col_Act-1]=='.':
                            return (fila_Act, col_Act, coste)
                if fila_Act+direccionY >= 0 and fila_Act+direccionY<len(mapa) and col_Act+1 >= 0 and col_Act+1<len(mapa):
                        if mapa[fila_Act, col_Act+1]=='@' and mapa[fila_Act+direccionY, col_Act+1]=='.':
                            return (fila_Act, col_Act, coste)

    def saltoDiagonal(self, filaI, columnaI, direccionY, direccionX, final, mapa):
        fila_Act = filaI
        col_Act = columnaI
        coste = 0

        while True:
            fila_Act+=direccionY
            col_Act+=direccionX
            coste+=1414

            if fila_Act < 0 or fila_Act>=len(mapa) or col_Act < 0 or col_Act>=len(mapa):
                return None
            elif mapa[fila_Act, col_Act]=='@':
                return None
            if fila_Act==final.fila and col_Act==final.columna:
                return (fila_Act, col_Act, coste)

            if col_Act-direccionX > 0 and col_Act-direccionX<len(mapa) and fila_Act+direccionY > 0 and fila_Act+direccionY<len(mapa) and mapa[fila_Act, col_Act-direccionX]=='@' and mapa[fila_Act+direccionY, col_Act-direccionX]=='.':
                return (fila_Act, col_Act, coste)
            elif fila_Act-direccionY > 0 and fila_Act-direccionY<len(mapa) and col_Act+direccionX > 0 and col_Act+direccionX<len(mapa) and mapa[fila_Act-direccionY, col_Act]=='@' and mapa[fila_Act-direccionY, col_Act+direccionX]=='.':
                return (fila_Act, col_Act, coste)
            else:
                ps = self.saltoLineaRecta(fila_Act, col_Act, 0, direccionX, final, mapa)
                if ps!=None:
                    return (fila_Act, col_Act, coste)
                ps = self.saltoLineaRecta(fila_Act, col_Act, direccionY, 0, final, mapa)
                if ps!=None:
                    return (fila_Act, col_Act, coste)



    """def salto(self, filaI, colI, direccion, final, mapa, coste):
        fila=filaI+direccion[0]
        columna=colI+direccion[1]
        if fila < 0 or fila>=len(mapa) or columna < 0 or columna>=len(mapa):
            return None
        elif mapa[fila, columna]=='@':
            return None
        if fila==final.fila and columna==final.columna:
            return (fila, columna, coste)
        if self.existeForzado(fila, columna, mapa, direccion[0], direccion[1]):
            return (fila, columna, coste)
        if abs(direccion[0])+abs(direccion[1])==2:
            for dir in [(direccion[0], 0), (0, direccion[1])]:
                if self.salto(fila, columna, dir, final, mapa, coste+1414)!=None:
                    return (fila, columna, coste)
            if mapa[fila, columna+direccion[1]]=='@' and mapa[fila+direccion[0], columna]=='@':
                return None
            return self.salto(fila, columna, direccion, final, mapa, coste+1414)
        return self.salto(fila, columna, direccion, final, mapa, coste+1000)"""

    """def calculaSucesoresJPS2(self, mapa, objetivo):
        sucesores=[]

        vecinos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        #print(vecinos)
        for n in vecinos:
            if abs(n[0])+abs(n[1])==2:
                coste = 1414
            else:
                coste = 1000
            ps = self.salto(self.fila, self.columna, n, objetivo, mapa, self.g+coste)
            if ps!=None:
                sucesores.append(NodoArbol(ps[0], ps[1], self.fila,self.columna, estimacion=self.h(ps[0], ps[1], objetivo)+ps[2], camino=ps[2]))

        return sucesores"""

    """def existeForzado(self,fila, columna, mapa, dirVert, dirHor):
        #vecinos = []

        x1 = columna
        y1 = fila
        x0 = x1-dirHor
        y0 = y1-dirVert
        x2 = x1+dirHor
        y2 = y1+dirVert

        if dirVert==0 or dirHor==0:
            if dirVert==0:
                if mapa[y0-1, x1]=='@' and mapa[y0-1, x2]=='.':
                    return True
                if mapa[y0+1, x1]=='@' and mapa[y0+1, x2]=='.':
                    return True
            else:
                if mapa[y1, x0-1]=='@' and mapa[y2, x0-1]=='.':
                    return True
                if mapa[y1, x0+1]=='@' and mapa[y2, x0+1]=='.':
                    return True
        else:
            if mapa[y1, x0]=='@' and mapa[y2, x0]=='.':
                return True
            if mapa[y0, x1]=='@' and mapa[y0, x2]=='.':
                return True
        return False"""

    def calculaSucesoresDijkstra(self, mapa, fIC, cIC, tamCluster):
        sucesores=[]

        nuevog=self.g+1000
        #Arriba
        if self.fila-1>=fIC and mapa[self.fila-1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna, self.fila, self.columna, 0, nuevog))
        #Abajo
        if self.fila+1<fIC+tamCluster and mapa[self.fila+1, self.columna]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna, self.fila, self.columna, 0, nuevog))
        #Izquierda
        if self.columna-1>=cIC and mapa[self.fila, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna-1, self.fila, self.columna, 0, nuevog))
        #Derecha
        if self.columna+1<cIC+tamCluster and mapa[self.fila, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila, self.columna+1, self.fila, self.columna, 0, nuevog))

        nuevog=self.g+1414

        #Arriba izquierda
        if self.fila-1>=fIC and self.columna-1>=cIC and mapa[self.fila-1, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna-1, self.fila, self.columna, 0, nuevog))
        #Arriba derecha
        if self.fila-1>=fIC and self.columna+1<cIC+tamCluster and mapa[self.fila-1, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila-1, self.columna+1, self.fila, self.columna, 0, nuevog))
        #Abajo izquierda
        if self.fila+1<fIC+tamCluster and self.columna-1>=cIC and mapa[self.fila+1, self.columna-1]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna-1, self.fila, self.columna, 0, nuevog))
        #Abajo derecha
        if self.fila+1<fIC+tamCluster and self.columna+1<cIC+tamCluster and mapa[self.fila+1, self.columna+1]=='.':
            sucesores.append(NodoArbol(self.fila+1, self.columna+1, self.fila, self.columna, 0, nuevog))

        return sucesores

    def calculaSucesoresHPA(self,nActual, grafo, nodoObjetivo):
        v, sucesores = grafo.get_sucesores(nActual.fila, nActual.columna)
        A = []
        for i in sucesores:
            coste = i.get_weight(v)+nActual.g
            nodo = NodoArbol(i.id.fila, i.id.columna, nActual.fila, nActual.columna, self.h(i.id.fila, i.id.columna, nodoObjetivo)+coste, coste)
            A.append(nodo)
        return A

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
            #return self.nombre==other.nombre
            return self.fila==other.fila and self.columna==other.columna
        else:
            return False

    def __hash__(self):
        return hash(self.nombre)

    def __str__(self):
        return self.nombre+" Cluster: "+str(self.cluster)+" Fila: "+str(self.fila)+" Columna: "+str(self.columna)
        #return self.nombre

    def __repr__(self):
        return str(self)


class NodoLista:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x==other.x and self.y==other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.x<other.x
        else:
            return False


class NodoJPS:
    def __init__(self, fila, columna, forzado):
        self.fila = fila
        self.columna = columna
        self.forzado = forzado
