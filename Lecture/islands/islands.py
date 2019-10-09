"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

build grah - 

for each node find all neighbors n/s/e/w

"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.verticies:
            self.verticies[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist")

    def bft(self, starting_node):
        # path of things connected to that starting point
        que = Queue()
        que.enqueue([starting_node])
        visited = {}

        while que.size() > 0:
            path = que.dequeue()
            v = path[-1]

            # if node not in explored, loop through all neighbor nodes and put them in explored,
            # add one to number of islands
            return v

            for neighbor in self.verticies[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                que.enqueue(path_copy)


def island_counter(islands):
    graph = Graph()

    for row in islands:
        for i in row:
            if i == 1:
                graph.add_vertex((row, i))

    for i in graph.verticies:
        row = i[0]
        column = i[1]
        if ((row + 1), column) in graph.verticies:
            graph.add_edges(i, ((row + 1), column))
            # print('south')
        if ((row - 1), column) in graph.verticies:
            graph.add_edges(i, ((row - 1), column))
            # print('north')
        if (row, (column + 1)) in graph.verticies:
            graph.add_edges(i, (row, (column+1)))
            # print('east')
        if (row, (column - 1)) in graph.verticies:
            graph.add_edges(i, (row, (column-1)))
            # print('west')

    print(graph.verticies)

    explored = set()
    islands = 0
    for i in graph.verticies:
        if i not in explored:
            islands += 1
            explored += (graph.bft(i))


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands)
