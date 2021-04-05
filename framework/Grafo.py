from Nodos import *
from Agente import *


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self, v = {}, n = 0):
        self.vert_dict = v
        self.num_vertices = n

    def __iter__(self):
        return iter(self.vert_dict.values())

    def __copy__(self):
        return Graph(self.vert_dict, self.num_vertices)

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def get_dict(self):
        return self.vert_dict

    def añadirConexionesIntraClusters(self, agente):
        vertices = self.get_vertices()
        aux = 1

        lista = []
        for i in vertices:
            lista.append(i)

        for i in lista:
            for j in lista[aux:len(lista)]:
                if i.cluster == j.cluster:
                    agente.inicial=NodoArbol(i.fila, i.columna)
                    agente.objetivo=NodoArbol(j.fila, j.columna)
                    sol = agente.aEstrella()
                    if sol!=None:
                        self.add_edge(i, j, sol[2])
            aux+=1

