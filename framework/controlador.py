import pickle
import time
from random import random, randint
from Mapas import *
from PIL import Image
import TratadorMapas
import matplotlib.pyplot as plt
from Agente import *

from Nodos import *

def calcularA(mapaIntroducido, fI, cIni, fF, cF, agente, comp):

    """j = open("mapasTratados\\mapasBase1.txt", "rb")
    listamapas=pickle.load(j)
    j.close()

    mapa = listamapas[3]"""
    mapa = mapaIntroducido.__copy__()

    """inicial = NodoArbol(197, 319)
    final = NodoArbol(201,87)"""

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
            return [resultado[3], resultado[4], len(resultado[0]), resultado[2]]
    else:
        return None

def calcularHPA(mapaIntroducido, fI, cIni, fF, cF, comp):
    """j = open("mapasTratados\\mapasHPA32.txt", "rb")
    lista=pickle.load(j)
    mapa = lista[3]
    j.close()"""
    mapa = mapaIntroducido.__copy__()

    g = mapa.grafoAbstracto.__copy__()

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


    print("Empieza dijkstra para I")
    agente.inicial = NodoArbol(inicial.fila, inicial.columna)
    resultadosI, it = agente.dijkstra(I, (inicial.fila//mapa.tamCluster)*mapa.tamCluster, (inicial.columna//mapa.tamCluster)*mapa.tamCluster, mapa.tamCluster)
    print("Empieza dijkstra para D")
    agente.inicial = NodoArbol(final.fila, final.columna)
    resultadosD, it = agente.dijkstra(D, (final.fila//mapa.tamCluster)*mapa.tamCluster, (final.columna//mapa.tamCluster)*mapa.tamCluster, mapa.tamCluster)

    if resultadosI!=None:
        print("resultados I")
        for r in resultadosI:
            fila = r[0].fila
            columna = r[0].columna
            """print(fila)
            print(columna)
            print("")"""
            n = g.get_verticeComp(fila, columna).id
            g.add_edge(inicial, n, r[2], r[1])
            #g.add_edge(n, inicial, r[2], r[1])



    if resultadosD!=None:
        print("resultados D")
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
    if resultado != None:
        if comp == False:
            camino, datos, costeTotal, t, it = resultado


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
            return [resultado[3], resultado[4], len(resultado[0]), resultado[2]]
    else:
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
    listaInicio =[]
    listaFinal = []
    sep=25

    while len(listaFinal)<nPuntos:
        filaI = randint(0, mapa.dimensiones-1)
        colI = randint(0, mapa.dimensiones-1)

        filaF = randint(0, mapa.dimensiones-1)
        colF = randint(0, mapa.dimensiones-1)

        if mapa.mapa[filaI, colI]=='.' and mapa.mapa[filaF, colF]=='.' and sep-5 < abs(colI-colF)+abs(filaI-filaF) and abs(colI-colF)+abs(filaI-filaF)< sep+5:
            listaInicio.append((filaI, colI))
            listaFinal.append((filaF, colF))
            sep+=25
    return listaInicio, listaFinal

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
        print("funciono en A")
        if resultadoA!= None:
            tiemposA.append(NodoLista(resultadoA[2],resultadoA[0]))
            itsA.append(NodoLista(resultadoA[2],resultadoA[1]))

            for i in [mapa4, mapa8, mapa16, mapa32]:
                print("funciono antes de calcular hpa")
                resultadoHPA = calcularHPA(i, filaS, colS, filaG, colG, True)
                print("funciono tras hpa")
                error = (abs(resultadoHPA[3]-resultadoA[3])/resultadoA[3])*100
                if resultadoHPA!=None:
                    if i.tamCluster==4:
                        tiemposHPA4.append(NodoLista(resultadoA[2], resultadoHPA[0]))
                        itsHPA4.append(NodoLista(resultadoA[2], resultadoHPA[1]))
                        costesHPA4.append(NodoLista(resultadoA[2], error))
                    elif i.tamCluster==8:
                        tiemposHPA8.append(NodoLista(resultadoA[2], resultadoHPA[0]))
                        itsHPA8.append(NodoLista(resultadoA[2], resultadoHPA[1]))
                        costesHPA8.append(NodoLista(resultadoA[2], error))
                    elif i.tamCluster==16:
                        tiemposHPA16.append(NodoLista(resultadoA[2], resultadoHPA[0]))
                        itsHPA16.append(NodoLista(resultadoA[2], resultadoHPA[1]))
                        costesHPA16.append(NodoLista(resultadoA[2], error))
                    else:
                        tiemposHPA32.append(NodoLista(resultadoA[2], resultadoHPA[0]))
                        itsHPA32.append(NodoLista(resultadoA[2], resultadoHPA[1]))
                        costesHPA32.append(NodoLista(resultadoA[2], error))
                print("funciono tras añadir las medidas")

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

    costesHPA4.sort()
    costesHPA8.sort()
    costesHPA16.sort()
    costesHPA32.sort()

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
    """dist32= []
    dist16= []
    dist8= []
    dist4= []"""
    c32= []
    c16= []
    c8= []
    c4= []
    for i in range(0,len(tiemposHPA32)):
        t32.append(tiemposHPA32[i].y)
        #dist32.append(tiemposHPA32[i].x)
        it32.append(itsHPA32[i].y)
        c32.append(costesHPA32[i].y)
    for i in range(0,len(tiemposHPA16)):
        #dist16.append(tiemposHPA16[i].x)
        t16.append(tiemposHPA16[i].y)
        it16.append(itsHPA16[i].y)
        c16.append(costesHPA16[i].y)
    for i in range(0,len(tiemposHPA8)):
        #dist8.append(tiemposHPA8[i].x)
        t8.append(tiemposHPA8[i].y)
        it8.append(itsHPA8[i].y)
        c8.append(costesHPA8[i].y)
    for i in range(0,len(tiemposHPA4)):
        #dist4.append(tiemposHPA4[i].x)
        t4.append(tiemposHPA4[i].y)
        it4.append(itsHPA4[i].y)
        c4.append(costesHPA4[i].y)
    for i in range(0,len(tiemposA)):
        tA.append(tiemposA[i].y)
        itA.append(itsA[i].y)
        dista.append(itsA[i].x)



    plt.plot(dista,tA,  'o-', label="A*" )
    plt.plot(dista ,t4 , "+-", label="HPA* TC:4")
    plt.plot(dista, t8, "v-", label="HPA* TC:8")
    plt.plot(dista, t16, "*-", label="HPA* TC:16")
    plt.plot(dista, t32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Tiempo de CPU")
    plt.title("Tiempo / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAT.png", dpi=300)
    plt.close()

    plt.plot(dista,itA,  'o-', label="A*" )
    plt.plot(dista ,it4 , "+-", label="HPA* TC:4")
    plt.plot(dista, it8, "v-", label="HPA* TC:8")
    plt.plot(dista, it16, "*-", label="HPA* TC:16")
    plt.plot(dista, it32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Nodos expandidos")
    plt.title("Nodos expandidos / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAEXP.png", dpi=300)
    plt.close()


    plt.plot(dista ,c4 , "+-", label="HPA* TC:4")
    plt.plot(dista, c8, "v-", label="HPA* TC:8")
    plt.plot(dista, c16, "*-", label="HPA* TC:16")
    plt.plot(dista, c32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Porcentaje de error")
    plt.title("Porcentaje de error / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAErr.png", dpi=300)
    plt.close()

    return "salidas/compAHPAT.png", "salidas/compAHPAEXP.png"
