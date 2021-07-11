import pickle
import time
from random import random, randint
from Mapas import *
import cv2 as cv
import matplotlib.pyplot as plt
from Agente import *

from Nodos import *

def calcularA(mapaIntroducido, fI, cIni, fF, cF, agente, comp):

    mapa = mapaIntroducido.__copy__()


    inicial = NodoArbol(fI, cIni)
    final = NodoArbol(fF, cF)

    agente.inicial=inicial
    agente.objetivo=final
    agente.mapa = mapa.mapa

    resultado = agente.aEstrella()

    if resultado != None:
        if comp==False:
            listaSol = resultado[0]

            mapaEscribir = mapa.__copy__()

            for i in listaSol:
                mapaEscribir.mapa[i.fila, i.columna]="X"

            f= open("salidas\\solucionA.txt", "w")

            for i in range(0, 512):
                f.write(''.join(mapaEscribir.mapa[i,:]))
                f.write("\n")
            f.close()

            mapa2 = np.empty([mapaEscribir.dimensiones, mapaEscribir.dimensiones], dtype=int)

            for i in range(0, 512):
                for j in range(0, 512):
                    if mapaEscribir.mapa[i,j]=='@':
                        mapa2[i,j]=0
                    elif mapaEscribir.mapa[i,j]=='.':
                        mapa2[i,j]=255
                    else:
                        mapa2[i,j] =ord(mapaEscribir.mapa[i,j])

            plt.imsave("salidas\\imagenA.jpg", mapa2, cmap='Greys')
            ventana=[resultado[1], "salidas\\imagenA.jpg"]
            return ventana
        else:
            return [resultado[3], resultado[4], len(resultado[0]), resultado[2], resultado[5]]
    else:
        return None

def calcularHPA(mapaIntroducido, fI, cIni, fF, cF, comp):
    mapa = mapaIntroducido.__copy__()

    g = mapa.grafoAbstracto.__copy__()

    t_0 = time.time()

    numClustersPorFila = mapa.dimensiones//mapa.tamCluster
    cI = (fI // mapa.tamCluster)*numClustersPorFila+(cIni // mapa.tamCluster)
    cD = (fF // mapa.tamCluster)*numClustersPorFila+(cF // mapa.tamCluster)

    inicial = NodoGrafo("S", fI, cIni, cI)
    final = NodoGrafo("D", fF,cF, cD)

    I = []
    D = []

    for i in mapa.grafoAbstracto.get_vertices():
        if i.cluster == cI:
            I.append(i)
        elif i.cluster == cD:
            D.append(i)

    agente = Agente(m = mapa.mapa)


    agente.inicial = NodoArbol(inicial.fila, inicial.columna)
    resultadosI, it = agente.dijkstra(I, (inicial.fila//mapa.tamCluster)*mapa.tamCluster, (inicial.columna//mapa.tamCluster)*mapa.tamCluster, mapa.tamCluster)

    agente.inicial = NodoArbol(final.fila, final.columna)
    resultadosD, it = agente.dijkstra(D, (final.fila//mapa.tamCluster)*mapa.tamCluster, (final.columna//mapa.tamCluster)*mapa.tamCluster, mapa.tamCluster)

    if resultadosI!=None:
        for r in resultadosI:
            fila = r[0].fila
            columna = r[0].columna
            n = g.get_verticeComp(fila, columna).id
            g.add_edge(inicial, n, r[2], r[1])
            #g.add_edge(n, inicial, r[2], r[1])



    if resultadosD!=None:
        for r in resultadosD:
            fila = r[0].fila
            columna = r[0].columna
            n = g.get_verticeComp(fila, columna).id
            g.add_edge(final, n, r[2], r[1])
            #g.add_edge(n, final, r[2], r[1])


    f= open("salidas\\hpaPruebaGrafo.txt", "w")

    for i in g:
        f.write(i.__str__())
        f.write("\n")
    f.close()

    agente.inicial = NodoArbol(fila=inicial.fila, columna=inicial.columna)
    agente.objetivo = NodoArbol(fila=final.fila, columna=final.columna)
    resultado = agente.hpaEstrella(g)
    t_1 = time.time()
    if resultado != None:
        if comp == False:
            camino, datos, costeTotal, it = resultado


            for i in camino:
                mapa.mapa[i.fila, i.columna]='X'

            f= open("salidas\\solucionHPA.txt", "w")

            for i in range(0, 512):
                f.write(''.join(mapa.mapa[i,:]))
                f.write("\n")
            f.close()

            mapa2 = np.empty([mapa.dimensiones, mapa.dimensiones], dtype=int)

            for i in range(0, 512):
                for j in range(0, 512):
                    if mapa.mapa[i,j]=='@':
                        mapa2[i,j]=0
                    elif mapa.mapa[i,j]=='.':
                        mapa2[i,j]=255
                    else:
                        mapa2[i,j] =ord(mapa.mapa[i,j])

            plt.imsave("salidas\\imagenHPA.jpg", mapa2, cmap='Greys')
            ventana=[datos, "salidas\\imagenHPA.jpg"]

            return ventana
        else:
            return [t_1-t_0, resultado[3], len(resultado[0]), resultado[2]]
    else:
        return None

def calcularJSP(mapaIntroducido, fI, cIni, fF, cF, agente, comp):
    mapa = mapaIntroducido.__copy__()

    inicial = NodoArbol(fI, cIni)
    final = NodoArbol(fF, cF)

    agente.inicial=inicial
    agente.objetivo=final
    agente.mapa = mapa.mapa

    resultado = agente.JSP()

    if resultado != None:
        if comp==False:
            listaSol = resultado[0]

            mapaEscribir = mapa.__copy__()

            for i in listaSol:
                mapaEscribir.mapa[i.fila, i.columna]="X"

            f= open("salidas\\solucionJSP.txt", "w")

            for i in range(0, 512):
                f.write(''.join(mapaEscribir.mapa[i,:]))
                f.write("\n")
            f.close()

            mapa2 = np.empty([mapaEscribir.dimensiones, mapaEscribir.dimensiones], dtype=int)

            for i in range(0, 512):
                for j in range(0, 512):
                    if mapaEscribir.mapa[i,j]=='@':
                        mapa2[i,j]=255
                    elif mapaEscribir.mapa[i,j]=='.':
                        mapa2[i,j]=0
                    else:
                        mapa2[i,j] =ord(mapaEscribir.mapa[i,j])

            #plt.imsave("salidas\\imagenJSP.jpg", mapa2, cmap='Greys')


            mapa2 = np.uint8(mapa2)

            mapa2 = cv.cvtColor(mapa2, cv.COLOR_GRAY2BGR)

            for i in range(1, len(listaSol)):
                #mapita.mapa[i.fila, i.columna]="X"
                mapa2 = cv.line(mapa2,(listaSol[i-1].columna, listaSol[i-1].fila), (listaSol[i].columna, listaSol[i].fila), color=(255, 255, 255), thickness=1)

            cv.imwrite("salidas\\imagenJSP.jpg", mapa2)
            ventana=[resultado[1], "salidas\\imagenJSP.jpg"]
            return ventana
        else:
            #       Tiempo         Iteraciones  Nodos               Coste total
            return [resultado[3], resultado[4], len(resultado[0]), resultado[2]]
    else:
        print("salgp aqiu")
        return None

def comparacionInsercion(pos, nPuntos):
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

    tiempos = []
    its=[]

    listaInicio, listaFinal = creaPuntos(mapa4, nPuntos)
    for i in [mapa4, mapa8, mapa16, mapa32]:
        tm=[]
        itm=[]
        for pos in range(0, len(listaInicio)):
            S=listaInicio[pos]
            G=listaFinal[pos]

            filaS=S[0]
            colS=S[1]
            filaG=G[0]
            colG=G[1]

            t_0 = time.time()
            g = i.grafoAbstracto.__copy__()

            numClustersPorFila = i.dimensiones//i.tamCluster
            cI = (filaS // i.tamCluster)*numClustersPorFila+(colS // i.tamCluster)
            cD = (filaG // i.tamCluster)*numClustersPorFila+(colG // i.tamCluster)

            inicial = NodoGrafo("S", filaS, colS, cI)
            final = NodoGrafo("D", filaG,colG, cD)

            I = []
            D = []

            for k in i.grafoAbstracto.get_vertices():
                if k.cluster == cI:
                    I.append(k)
                elif k.cluster == cD:
                    D.append(k)

            agente = Agente(m = i.mapa)


            #print("Empieza dijkstra para I")
            agente.inicial = NodoArbol(inicial.fila, inicial.columna)
            resultadosI, it1 = agente.dijkstra(I, (inicial.fila//i.tamCluster)*i.tamCluster, (inicial.columna//i.tamCluster)*i.tamCluster, i.tamCluster)
            #print("Empieza dijkstra para D")

            agente.inicial = NodoArbol(final.fila, final.columna)
            resultadosD, it2 = agente.dijkstra(D, (final.fila//i.tamCluster)*i.tamCluster, (final.columna//i.tamCluster)*i.tamCluster, i.tamCluster)

            if resultadosI!=None:
                #print("resultados I")
                for r in resultadosI:
                    fila = r[0].fila
                    columna = r[0].columna
                    n = g.get_verticeComp(fila, columna).id
                    g.add_edge(inicial, n, r[2], r[1])



            if resultadosD!=None:
                #print("resultados D")
                for r in resultadosD:
                    fila = r[0].fila
                    columna = r[0].columna
                    n = g.get_verticeComp(fila, columna).id
                    g.add_edge(final, n, r[2], r[1])

            t_1 = time.time()

            tm.append(t_1-t_0)
            itm.append(it1+it2)
        ltm = len(tm)
        lit = len(itm)
        tiempos.append(sum(tm)/ltm)
        its.append(sum(itm)/lit)

    plt.bar(["4","8", "16", "32"],tiempos, align="center")
    plt.xlabel("Tamaño de clusters")
    plt.ylabel("Tiempo para añadir SG")
    plt.title("Tiempo / Tamaño Clusters")
    plt.savefig("salidas/cInseSGTiempo.png", dpi=300)

    plt.bar(["4","8", "16", "32"],its, align="center")
    plt.xlabel("Tamaño de clusters")
    plt.ylabel("Tiempo para añadir SG")
    plt.title("Nodos expandidos / Tamaño Clusters")
    plt.savefig("salidas/cInseSGNExp.png", dpi=300)

    return "salidas/cInseSGTiempo.png", "salidas/cInseSGNExp.png"

def creaPuntos(mapa, nPuntos):
    j = open("bancoPruebas\\"+mapa[0:len(mapa)-4]+".scen", "rb")
    lista=pickle.load(j)
    j.close()
    sep=25

    listaFinal=[]
    cont = 0
    while len(listaFinal)<nPuntos:
        coste = lista[cont][4]

        if sep-2 < coste and coste < sep+2:
            listaFinal.append(lista[cont])
            sep+=25
        cont+=1
    return listaFinal


def comparacionAHPA(pos, nPuntos):
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
    dista = []

    tiemposHPA4 = []
    itsHPA4=[]
    costesHPA4 = []

    tiemposHPA8 = []
    itsHPA8=[]
    costesHPA8 = []

    tiemposHPA16 = []
    itsHPA16=[]
    costesHPA16 = []

    tiemposHPA32 = []
    itsHPA32=[]
    costesHPA32 = []

    listaFinal = creaPuntos(mapa4.nombre, nPuntos)

    for pos in listaFinal:
        filaS=pos[0]
        colS=pos[1]
        filaG=pos[2]
        colG=pos[3]

        mapaA = Mapa(mapa4.nombre, mapa4.dimensiones, mapa4.mapa.__copy__())
        resultadoA = calcularA(mapaA, filaS, colS, filaG, colG, Agente(), True)
        print("Peto aqui")
        if resultadoA!= None:
            tiemposA.append(resultadoA[0])
            itsA.append(resultadoA[1])
            #dista.append(resultadoA[2])
            dista.append(pos[4])

            for i in [mapa4, mapa8, mapa16, mapa32]:

                resultadoHPA = calcularHPA(i, filaS, colS, filaG, colG, True)
                error = (abs(resultadoHPA[3]-resultadoA[3])/resultadoA[3])*100
                if resultadoHPA!=None:
                    if i.tamCluster==4:
                        tiemposHPA4.append(resultadoHPA[0])
                        itsHPA4.append(resultadoHPA[1])
                        costesHPA4.append(error)
                    elif i.tamCluster==8:
                        tiemposHPA8.append(resultadoHPA[0])
                        itsHPA8.append(resultadoHPA[1])
                        costesHPA8.append(error)
                    elif i.tamCluster==16:
                        tiemposHPA16.append(resultadoHPA[0])
                        itsHPA16.append(resultadoHPA[1])
                        costesHPA16.append(error)
                    else:
                        tiemposHPA32.append(resultadoHPA[0])
                        itsHPA32.append(resultadoHPA[1])
                        costesHPA32.append(error)

    plt.plot(dista, tiemposA,  'o-', label="A*" )
    plt.plot(dista, tiemposHPA4 , "+-", label="HPA* TC:4")
    plt.plot(dista, tiemposHPA8, "v-", label="HPA* TC:8")
    plt.plot(dista, tiemposHPA16, "*-", label="HPA* TC:16")
    plt.plot(dista, tiemposHPA32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Tiempo de CPU")
    plt.title("Tiempo / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAT.png", dpi=300)
    plt.close()

    plt.plot(dista, itsA,  'o-', label="A*" )
    plt.plot(dista, itsHPA4 , "+-", label="HPA* TC:4")
    plt.plot(dista, itsHPA8, "v-", label="HPA* TC:8")
    plt.plot(dista, itsHPA16, "*-", label="HPA* TC:16")
    plt.plot(dista, itsHPA32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Nodos expandidos")
    plt.title("Nodos expandidos / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAEXP.png", dpi=300)
    plt.close()


    plt.plot(dista ,costesHPA4 , "+-", label="HPA* TC:4")
    plt.plot(dista, costesHPA8, "v-", label="HPA* TC:8")
    plt.plot(dista, costesHPA16, "*-", label="HPA* TC:16")
    plt.plot(dista, costesHPA32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Porcentaje de error")
    plt.title("Porcentaje de error / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAErr.png", dpi=300)
    plt.close()

    return "salidas/compAHPAT.png", "salidas/compAHPAEXP.png", "salidas/compAHPAErr.png"

def comparacionAJSP(pos, nPuntos, prueba=1):
    j = open("mapasTratados\\mapasBase1.txt", "rb")
    lista=pickle.load(j)
    j.close()
    mapa = lista[pos]


    tiemposA = []
    itsA=[]
    dista = []

    tiemposJPS = []
    itsJPS=[]
    distJSP = []

    listaFinal = creaPuntos(mapa.nombre, nPuntos)
    for pos in listaFinal:
        print("Nueva prueba")
        filaS=pos[0]
        colS=pos[1]
        filaG=pos[2]
        colG=pos[3]


        mapaA = Mapa(mapa.nombre, mapa.dimensiones, mapa.mapa.__copy__())
        resultadoA = calcularA(mapaA, filaS, colS, filaG, colG, Agente(), True)
        resultadoJSP = calcularJSP(mapaA, filaS, colS, filaG, colG, Agente(), True)

        if resultadoA!= None:
            tiemposA.append(resultadoA[0])
            itsA.append(resultadoA[1])
            #dista.append(resultadoA[2])
            dista.append(pos[4])

            tiemposJPS.append(resultadoJSP[0])
            itsJPS.append(resultadoJSP[1])
            #dista.append(resultadoJSP[2])
            distJSP.append(pos[4])

    plt.plot(dista, tiemposA,  'o-', label="A*" )
    plt.plot(dista, tiemposJPS, "+-", label="JPS")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Tiempo de CPU")
    plt.title("Tiempo / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAJSPT"+str(prueba)+".png", dpi=300)
    plt.close()

    plt.plot(dista, itsA,  'o-', label="A*" )
    plt.plot(dista, itsJPS, "+-", label="JPS")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Nodos expandidos")
    plt.title("Nodos expandidos / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAJSPEXP"+str(prueba)+".png", dpi=300)
    plt.close()
    #Hay que descomentar para que funcione el comparador

    return "salidas/compAJSPT"+str(prueba)+".png", "salidas/compAJSPEXP"+str(prueba)+".png"    #NO COMENTAR PARA QUE FUNCIONE EN LA INTERFAZ
    #return tiemposA, tiemposJPS, dista
