class Vertex:
    def __init__(self, node=(int, int)):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0, camino = []):
        self.adjacent[neighbor] = (weight, camino)

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor][0]

    def get_camino(self, neighbor):
        return self.adjacent[neighbor][1]

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

    def get_verticeComp(self, fila, columna):
        for i in self.vert_dict.keys():
            if i[0]==fila and i[1]==columna: return self.get_vertex(i)
        return None

    def add_edge(self, frm, to, cost = 0, camino = []):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost, camino)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost, camino.reverse())

    def get_vertices(self):
        return self.vert_dict.keys()

    def get_dict(self):
        return self.vert_dict

    def get_sucesores(self, fila, columna):
        v = self.get_verticeComp(fila, columna)
        return v, v.get_connections()
