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

        vecinos = self.calculaSucesores(mapa, objetivo)
        #print(vecinos)
        for n in vecinos:
            dir = (n.fila-self.fila, n.columna-self.columna)
            if abs(dir[0])+abs(dir[1])==2:
                coste = 1414
            else:
                coste = 1000
            ps = self.salto(self, dir, objetivo, mapa, self.g+coste)
            #print(ps)
            if ps!=None:
                sucesores.append(NodoArbol(ps.fila, ps.columna, self.fila,self.columna, estimacion=self.h(ps.fila, ps.columna, objetivo)+ps.g, camino=ps.g))

        return sucesores

    def salto(self, x, direccion, final, mapa, coste):
        n = NodoArbol(x.fila+direccion[0], x.columna+direccion[1], camino=coste)
        if n.fila < 0 or n.fila>=len(mapa) or n.columna < 0 or n.columna>=len(mapa):
            return None
        elif mapa[n.fila, n.columna]=='@':
            return None
        if n.fila==final.fila and n.columna==final.columna:
            return n
        if self.existeForzado(n.fila, n.columna, mapa, direccion[0], direccion[1]):
            return n
        if abs(direccion[0])+abs(direccion[1])==2:
            for dir in [(direccion[0], 0), (0, direccion[1])]:
                if self.salto(n, dir, final, mapa, coste+1414) != None:
                    return n
        if mapa[x.fila, x.columna+direccion[1]]=='@' and mapa[x.fila+direccion[0], x.columna]=='@':
            return None
        else:
            if abs(direccion[0])+abs(direccion[1])==2:
                return self.salto(n, direccion, final, mapa, coste+1414)
            else:
                return self.salto(n, direccion, final, mapa, coste+1000)

    def existeForzado(self,fila, columna, mapa, dirVert, dirHor):
        #vecinos = []

        x1 = columna
        y1 = fila
        x0 = x1-dirHor
        y0 = y1-dirVert
        x2 = x1+dirHor
        y2 = y1+dirVert
        dimensiones = len(mapa)

        if dirVert==0 or dirHor==0:
            if dirVert==0:
                if x2>0 and x2<dimensiones and y0-1>0 and y0-1<dimensiones and x1>0 and x1<dimensiones and mapa[y0-1, x1]=='@' and mapa[y0-1, x2]=='.':
                    #vecinos.append(NodoJPS(y0-1, x2, True))
                    return True
                if x2>0 and x2<dimensiones and y0+1>0 and y0+1<dimensiones and x1>0 and x1<dimensiones and mapa[y0+1, x1]=='@' and mapa[y0+1, x2]=='.':
                    #vecinos.append(NodoJPS(y0+1, x2, True))
                    return True
                """if x2>0 and x2<len(mapa) and y0>0 and y0<len(mapa) and mapa[y0, x2]=='.':
                    vecinos.append(NodoJPS(y0, x2, False))"""
            else:
                if y2>0 and y2<dimensiones and x0-1>0 and x0-1<dimensiones and y1>0 and y1<dimensiones and mapa[y1, x0-1]=='@' and mapa[y2, x0-1]=='.':
                    #vecinos.append(NodoJPS(y2, x0-1, True))
                    return True
                if y2>0 and y2<dimensiones and x0+1>0 and x0+1<dimensiones and y1>0 and y1<dimensiones and mapa[y1, x0+1]=='@' and mapa[y2, x0+1]=='.':
                    #vecinos.append(NodoJPS(y2, x0+1, True))
                    return True
                """if y2>0 and y2<len(mapa) and x0>0 and x0<len(mapa) and mapa[y2, x0]=='.':
                    vecinos.append(NodoJPS(y2, x0, False))"""
        else:
            if y2>0 and y2<dimensiones and x0>0 and x0<dimensiones and y1>0 and y1<dimensiones and mapa[y1, x0]=='@' and mapa[y2, x0]=='.':
                #vecinos.append(NodoArbol(y2, x0, True))
                return True
            if x2>0 and x2<dimensiones and y0>0 and y0<dimensiones and x1>0 and x1<dimensiones and mapa[y0, x1]=='@' and mapa[y0, x2]=='.':
                #vecinos.append(NodoArbol(y0, x2, True))
                return True
            """if y1>0 and y1<len(mapa) and x2>0 and x2<len(mapa) and mapa[y1, x2]=='.':
                vecinos.append(NodoArbol(y1, x2, False))
            if y2>0 and y2<len(mapa) and x1>0 and x1<len(mapa) and mapa[y2, x1]=='.':
                vecinos.append(NodoArbol(y2, x1, False))
            if x2>0 and x2<len(mapa) and y2>0 and y2<len(mapa) and mapa[y2, x2]=='.':
                vecinos.append(NodoArbol(y2, x2, False))"""

        return False

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
