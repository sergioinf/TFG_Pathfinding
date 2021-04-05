
import numpy as np
from Nodos import NodoArbol

class Agente:
    def __init__(self, i=None, o=None, m=None):
        self.inicial=i
        self.objetivo=o
        self.mapa = m

    def esFinal(self, nodo):
        if nodo.fila==self.objetivo.fila and nodo.columna == self.objetivo.columna:
            return True
        else:
            return False

    def recuperaSolucion(self, nodo, lista, malla):
        lista.append(nodo)
        if nodo.puntPadreF == -1 :
            return lista
        else :
            return self.recuperaSolucion(malla[nodo.puntPadreF, nodo.puntPadreC], lista, malla)

    def aEstrella(self):
        longitud = len(self.mapa)
        malla = np.empty([longitud, longitud], dtype=NodoArbol)
        abiertos = [self.inicial]
        it=0
        exito=False

        while len(abiertos)>0 :
            it+=1
            nActual = abiertos.pop()
            malla[nActual.fila, nActual.columna]=nActual

            if self.esFinal(nActual) :
                exito = True
                break

            sucesores = nActual.calculaSucesores(self.mapa, self.objetivo)

            for n2 in sucesores :
                if malla[n2.fila, n2.columna]==None and abiertos.count(n2)==0 :
                    #n2.puntPadreF=nActual.fila
                    #n2.puntPadreC=nActual.columna
                    #n2.g=nActual.g+nActual.costeArco(n2)
                    #n2.f=n2.g+n2.h(n2.fila, n2.columna, self.objetivo)
                    abiertos.append(n2)
                elif malla[n2.fila, n2.columna]!=None:
                    n2viejo = malla[n2.fila, n2.columna]
                    if n2.g<n2viejo.g:
                        malla[n2.fila, n2.columna]=None
                        abiertos.append(n2)
                else:
                    indice = abiertos.index(n2)
                    n2viejo = abiertos.pop(indice)
                    if n2.g<n2viejo.g:
                        abiertos.append(n2)
                    else:
                        abiertos.append(n2viejo)

            abiertos.sort(reverse = True)

        if exito==False :
            return None
        else :
            listaSol = self.recuperaSolucion(nActual, [], malla)
            datos ="Nodos expandidos: "+str(it)+"\n"+"Longitud de la solución: "+str(len(listaSol))+"\n"+"Coste de la solución: "+ str(nActual.g)+"\n"

            #print("Nodos expandidos: "+str(it))
            #print("Longitud de la solución: "+str(len(listaSol)))
            #print("Coste de la solución: "+ str(nActual.g))
            return [listaSol, datos, nActual.g]

    def hpaEstrealla(self):
        return 0
