import pickle

from AEstrella import *
from HPAEstrella import *
from JPS import *
from mapa import *
import cv2 as cv
import matplotlib.pyplot as plt

def calcularA(mapaIntroducido, fI, cIni, fF, cF, comp):
    startTime = time.time()
    aestrella = AEstrella(mapaIntroducido)
    listaSol, datos, coste, it = aestrella.findPath(fI, cIni, fF, cF)
    endTime = time.time() - startTime

    if listaSol != None:
        if comp==False:
            mapaEscribir = mapaIntroducido.matriz.__copy__()

            for i in listaSol:
                mapaEscribir[i[0], i[1]]="X"

            f= open("salidas\\solucionA.txt", "w")

            for i in range(0, 512):
                f.write(''.join(mapaEscribir[i,:]))
                f.write("\n")
            f.close()



            mapa2 = np.empty([512, 512], dtype=int)

            for i in range(0, 512):
                for j in range(0, 512):
                    if mapaEscribir[i,j]=='@':
                        mapa2[i,j]=0
                    elif mapaEscribir[i,j]=='.':
                        mapa2[i,j]=255
                    else:
                        mapa2[i,j] =ord(mapaEscribir[i,j])

            plt.imsave("salidas\\imagenA.jpg", mapa2, cmap='Greys')
            ventana=[datos, "salidas\\imagenA.jpg"]
            return ventana
        else:
            return len(listaSol), coste, it, endTime
    else:
        return None

def calcularHPA(source, fI, cIni, fF, cF, comp):
    print("Entra")
    mapa = Mapa("provisional", 512, 512, source.mapa)
    mapa.construyeNodos()
    mapaI = mapa.copy()
    mapaG = mapa.copy()

    startTime = time.time()
    dij = HPAEstrella(mapa, mapaI,mapaG, source)
    resultado = dij.findPath(fI, cIni, fF, cF)
    endTime = time.time() - startTime

    mapaEscribir = source.mapa.__copy__()
    if resultado != None:
        listaSol, datos, coste,it, tiempoInsertar = resultado
        if comp == False:
            for c in listaSol:
                mapaEscribir[c[0], c[1]]="X"

            f= open("salidas\\solucionHPA.txt", "w")

            for i in range(0, 512):
                f.write(''.join(mapaEscribir[i,:]))
                f.write("\n")
            f.close()



            mapa2 = np.empty([512, 512], dtype=int)

            for i in range(0, 512):
                for j in range(0, 512):
                    if mapaEscribir[i,j]=='@':
                        mapa2[i,j]=0
                    elif mapaEscribir[i,j]=='.':
                        mapa2[i,j]=255
                    else:
                        mapa2[i,j] =0
            plt.imsave("salidas\\imagenHPA.jpg", mapa2, cmap='Greys')
            return datos, "salidas\\imagenHPA.jpg"
        else:
            return len(listaSol), datos, coste,it,endTime, tiempoInsertar

def calcularJPS(mapaIntroducido, fI, cIni, fF, cF, comp):
    """mapa = Mapa("provisional", 512, 512, mapaIntroducido.matriz)
    mapa.construyeNodos()"""

    startTime = time.time()
    jps = JPS(mapaIntroducido)
    listaSol, datos, coste, it = jps.findPath(fI, cIni, fF, cF)
    endTime = time.time() - startTime
    if listaSol != None:
        if comp==False:
            mapaEscribir = mapaIntroducido.matriz.__copy__()

            for i in listaSol:
                mapaEscribir[i[0], i[1]]="X"

            f= open("salidas\\solucionJSP.txt", "w")

            for i in range(0, 512):
                f.write(''.join(mapaEscribir[i,:]))
                f.write("\n")
            f.close()

            mapa2 = np.empty([512, 512], dtype=int)

            for i in range(0, 512):
                for j in range(0, 512):
                    if mapaEscribir[i,j]=='@':
                        mapa2[i,j]=255
                    elif mapaEscribir[i,j]=='.':
                        mapa2[i,j]=0
                    else:
                        mapa2[i,j] =ord(mapaEscribir[i,j])

            #plt.imsave("salidas\\imagenJSP.jpg", mapa2, cmap='Greys')


            mapa2 = np.uint8(mapa2)

            mapa2 = cv.cvtColor(mapa2, cv.COLOR_GRAY2BGR)

            for i in range(1, len(listaSol)):
                #mapita.mapa[i.fila, i.columna]="X"
                mapa2 = cv.line(mapa2,(listaSol[i-1][1], listaSol[i-1][0]), (listaSol[i][1], listaSol[i][0]), color=(255, 255, 255), thickness=1)

            cv.imwrite("salidas\\imagenJSP.jpg", mapa2)
            ventana=[datos, "salidas\\imagenJSP.jpg"]
            return ventana
        else:
            return len(listaSol), coste, it, endTime
    else:
        return None

def creaPuntos(mapa, nPuntos, sep):
    j = open("Pruebas\\"+mapa[0:len(mapa)-4]+".scen", "rb")
    print("Pruebas\\"+mapa[0:len(mapa)-4]+".scen")
    lista=pickle.load(j)
    j.close()

    listaFinal=[]
    cont = 0

    while len(listaFinal)<nPuntos:
        print(len(listaFinal))
        coste = lista[cont][4]

        if sep-2 < coste and coste < sep+2:
            listaFinal.append(lista[cont])
            sep+=25
        cont+=1
    return listaFinal

def comparacionInsercion(pos, nPuntos, sep):
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
    print(mapa8.nombre)
    listaFinal = creaPuntos(mapa8.nombre, nPuntos, sep)

    print("Cargado puntos")

    for i in [mapa8, mapa16, mapa32]:
        tm=[]
        itm=[]
        for pos in listaFinal:
            filaS=pos[0]
            colS=pos[1]
            filaG=pos[2]
            colG=pos[3]

            expHPA, datosHPA, costeHPA,itHPA,endTimeHPA, tiempoInsertarHPA = calcularHPA(i, filaS, colS, filaG, colG, True)
            tm.append(tiempoInsertarHPA)
            itm.append(endTimeHPA)
        tiempos.append(sum(tm)/len(tm))
        its.append(sum(itm)/len(itm))


    total = []
    for i in range(len(tiempos)):
        total.append(tiempos[i])
        total.append(its[i])

    plt.bar(["8I","8B", "16I","16B", "32I", "32B"],total, align="center")
    plt.xlabel("Tamaño de clusters")
    plt.ylabel("Tiempo")
    plt.title("Tiempo / Tamaño Clusters")
    plt.legend(["I =Tiempo de insercion de SG, B =Tiempo total de búsqueda"])
    plt.savefig("salidas/cInseSGTiempo.png", dpi=300)


    """plt.bar(["8", "16", "32"],tiempos, align="center")
    plt.xlabel("Tamaño de clusters")
    plt.ylabel("Tiempo para añadir SG")
    plt.title("Tiempo / Tamaño Clusters")
    plt.savefig("salidas/cInseSGTiempo.png", dpi=300)

    plt.bar(["8", "16", "32"],its, align="center")
    plt.xlabel("Tamaño de clusters")
    plt.ylabel("Tiempo de búsqueda SG")
    plt.title("Nodos expandidos / Tamaño Clusters")
    plt.savefig("salidas/cInseSGNExp.png", dpi=300)"""

    return "salidas/cInseSGTiempo.png"

def comparacionHPAJPS(pos, nPuntos, sep):
    j = open("mapasTratados\\mapasBase.txt", "rb")
    lista=pickle.load(j)
    mapaA = lista[pos]
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

    listaFinal = creaPuntos(mapaA.nombre, nPuntos, sep)


    for a in listaFinal:
        print(a)
        filaS=a[0]
        colS=a[1]
        filaG=a[2]
        colG=a[3]

        resultadoA = calcularJPS(mapaA.copy(), filaS, colS, filaG, colG, True)
        if resultadoA!= None:
            expA, costeA, itA, endTimeA = resultadoA


            tiemposA.append(endTimeA)
            itsA.append(itA)
            dista.append(a[4])

            for i in [mapa8, mapa16, mapa32]:

                resultadoHPA = calcularHPA(i, filaS, colS, filaG, colG, True)

                if resultadoHPA!=None:
                    expHPA, datosHPA, costeHPA,itHPA,endTimeHPA, tiempoInsertarHPA = resultadoHPA
                    error = (abs(costeHPA-costeA)/costeA)*100
                    if i.tamCluster==4:
                        tiemposHPA4.append(endTimeHPA)
                        itsHPA4.append(itHPA)
                        costesHPA4.append(error)
                    elif i.tamCluster==8:
                        tiemposHPA8.append(endTimeHPA)
                        itsHPA8.append(itHPA)
                        costesHPA8.append(error)
                    elif i.tamCluster==16:
                        tiemposHPA16.append(endTimeHPA)
                        itsHPA16.append(itHPA)
                        costesHPA16.append(error)
                    else:
                        tiemposHPA32.append(endTimeHPA)
                        itsHPA32.append(itHPA)
                        costesHPA32.append(error)

    plt.plot(dista, tiemposA,  'o-', label="JPS" )
    plt.plot(dista, tiemposHPA8, "v-", label="HPA* TC:8")
    plt.plot(dista, tiemposHPA16, "*-", label="HPA* TC:16")
    plt.plot(dista, tiemposHPA32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Tiempo de CPU(segundos)")
    plt.title("Tiempo / Profundidad")
    plt.legend()
    plt.savefig("salidas/compHPAJPST.png", dpi=300)
    plt.close()

    plt.plot(dista, itsA,  'o-', label="JPS" )
    plt.plot(dista, itsHPA8, "v-", label="HPA* TC:8")
    plt.plot(dista, itsHPA16, "*-", label="HPA* TC:16")
    plt.plot(dista, itsHPA32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Nodos expandidos")
    plt.title("Nodos expandidos / Profundidad")
    plt.legend()
    plt.savefig("salidas/compHPAJPSEXP.png", dpi=300)
    plt.close()


    return "salidas/compHPAJPST.png", "salidas/compHPAJPSEXP.png"

def comparacionAHPA(pos, nPuntos, sep):
    j = open("mapasTratados\\mapasBase.txt", "rb")
    lista=pickle.load(j)
    mapaA = lista[pos]
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
    insercionHPA4 = []

    tiemposHPA8 = []
    itsHPA8=[]
    costesHPA8 = []
    insercionHPA8 = []

    tiemposHPA16 = []
    itsHPA16=[]
    costesHPA16 = []
    insercionHPA16 = []

    tiemposHPA32 = []
    itsHPA32=[]
    costesHPA32 = []
    insercionHPA32 = []

    listaFinal = creaPuntos(mapaA.nombre, nPuntos, sep)


    for pos in listaFinal:
        filaS=pos[0]
        colS=pos[1]
        filaG=pos[2]
        colG=pos[3]

        resultadoA = calcularA(mapaA.copy(), filaS, colS, filaG, colG, True)
        if resultadoA!= None:
            expA, costeA, itA, endTimeA = resultadoA


            tiemposA.append(endTimeA)
            itsA.append(itA)
            #dista.append(resultadoA[2])
            dista.append(pos[4])

            for i in [mapa8, mapa16, mapa32]:
            #for i in [mapa32]:

                resultadoHPA = calcularHPA(i, filaS, colS, filaG, colG, True)

                if resultadoHPA!=None:
                    expHPA, datosHPA, costeHPA,itHPA,endTimeHPA, tiempoInsertarHPA = resultadoHPA
                    error = (abs(costeHPA-costeA)/costeA)*100
                    if i.tamCluster==4:
                        tiemposHPA4.append(endTimeHPA)
                        itsHPA4.append(itHPA)
                        costesHPA4.append(error)
                        insercionHPA4.append(tiempoInsertarHPA)
                    elif i.tamCluster==8:
                        tiemposHPA8.append(endTimeHPA)
                        itsHPA8.append(itHPA)
                        costesHPA8.append(error)
                        insercionHPA8.append(tiempoInsertarHPA)
                    elif i.tamCluster==16:
                        tiemposHPA16.append(endTimeHPA)
                        itsHPA16.append(itHPA)
                        costesHPA16.append(error)
                        insercionHPA16.append(tiempoInsertarHPA)
                    else:
                        tiemposHPA32.append(endTimeHPA)
                        itsHPA32.append(itHPA)
                        costesHPA32.append(error)
                        insercionHPA32.append(tiempoInsertarHPA)

    plt.plot(dista, tiemposA,  'o-', label="A*" )
    #plt.plot(dista, tiemposHPA4 , "+-", label="HPA* TC:4")
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
    #plt.plot(dista, itsHPA4 , "+-", label="HPA* TC:4")
    plt.plot(dista, itsHPA8, "v-", label="HPA* TC:8")
    plt.plot(dista, itsHPA16, "*-", label="HPA* TC:16")
    plt.plot(dista, itsHPA32, "1-", label="HPA* TC:32")
    plt.xlabel("Profundidad de la solución")
    plt.ylabel("Nodos expandidos")
    plt.title("Nodos expandidos / Profundidad")
    plt.legend()
    plt.savefig("salidas/compAHPAEXP.png", dpi=300)
    plt.close()


    #plt.plot(dista ,costesHPA4 , "+-", label="HPA* TC:4")
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

def comparacionAJPS(pos, nPuntos, sep, prueba=1):
    j = open("mapasTratados\\mapasBase.txt", "rb")
    lista=pickle.load(j)
    j.close()
    mapa = lista[pos]


    tiemposA = []
    itsA=[]
    dista = []

    tiemposJPS = []
    itsJPS=[]
    distJPS = []

    listaFinal = creaPuntos(mapa.nombre, nPuntos, sep)
    for pos in listaFinal:
        print("Nueva prueba")
        filaS=pos[0]
        colS=pos[1]
        filaG=pos[2]
        colG=pos[3]

        resultadoA = calcularA(mapa.copy(), filaS, colS, filaG, colG, True)
        resultadoJPS = calcularJPS(mapa.copy(), filaS, colS, filaG, colG, True)

        if resultadoA!= None:
            nodosExpA, costeA, itA, tiempoA = resultadoA
            nodosExpJPS, costeJPS, itJPS, tiempoJPS = resultadoJPS
            tiemposA.append(tiempoA)
            itsA.append(itA)
            #dista.append(resultadoA[2])
            dista.append(pos[4])

            tiemposJPS.append(tiempoJPS)
            itsJPS.append(itJPS)
            #dista.append(resultadoJSP[2])
            distJPS.append(pos[4])

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

    return "salidas/compAJSPT"+str(prueba)+".png", "salidas/compAJSPEXP"+str(prueba)+".png"    #NO COMENTAR PARA QUE FUNCIONE EN LA INTERFAZ
