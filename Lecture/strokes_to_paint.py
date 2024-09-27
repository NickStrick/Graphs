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

    def bft(self, starting_node, explored):
        # path of things connected to that starting point
        que = Queue()
        que.enqueue([starting_node])
        visited = set()

        while que.size() > 0:
            path = que.dequeue()
            v = path[-1]
            # for every node add it to explored
            visited.add(v)
            explored.add(v)

            for neighbor in self.verticies[v]:
                if neighbor not in visited:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    que.enqueue(path_copy)


def strokesRequired(picture):

    graph = Graph()

    for y in range(len(picture)):
        x_arr = list(picture[y])
        for x in range(len(x_arr)):
            # print(y,x, x_arr[x])
            graph.add_vertex((y, x, x_arr[x]))

    for i in graph.verticies:
        y = i[0]
        x = i[1]
        value = i[2]
        if ((y + 1), x, value) in graph.verticies:
            graph.add_edges(i, ((y + 1), x, value))
        # if ((y - 1), x, value) in graph.verticies:
        #     graph.add_edges(i, ((y - 1), x, value))
        if (y, (x + 1), value) in graph.verticies:
            graph.add_edges(i, (y, (x+1), value))
        # if (y, (x - 1), value) in graph.verticies:
        #     graph.add_edges(i, (y, (x-1), value))

    print(graph.verticies)
    explored = set()
    strokes = 0
    for i in graph.verticies:
        if i not in explored:
            strokes += 1
            graph.bft(i, explored)
    return strokes
