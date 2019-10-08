"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("cant create edge, vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        # add first node to stack

        que = Queue()
        visited = set()
        que.enqueue(starting_vertex)
        # while: queue not empty
        # pop node out of queue
        # if not visited
        # 	mark as visited
        # 	get adjacent edges and add to list
        # go to top of loop
        while que.size() > 0:
            vertex = que.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    que.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        # while: stackue not empty
        # pop node out of stackue
        # if not visited
        # 	mark as visited
        # 	get adjacent edges and add to list
        # go to top of loop
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    # default argument in a function is only evaluated during defenition, this set works once but not if you call it again
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        vertex = starting_vertex
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for next_vert in self.vertices[vertex]:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        que = Queue()
        visited = set()
        que.enqueue(starting_vertex)
        # while: queue not empty
        # pop node out of queue
        # if not visited
        # 	mark as visited
        # 	get adjacent edges and add to list
        # go to top of loop
        curr_path = []
        last_path = []
        while que.size() > 0:
            vertex = que.dequeue()
            # curr_path = last_path[0:len(last_path)]
            # curr_path.append(vertex)
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    # print(curr_path)
                    return True

                for next_vert in self.vertices[vertex]:
                    que.enqueue(next_vert)
        return False

    def dfs(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        vertex = starting_vertex
        if vertex not in visited:
            visited.add(vertex)
            # print(vertex)
            if vertex == destination_vertex:
                return True
            else:
                for next_vert in self.vertices[vertex]:
                    self.dfs(next_vert, destination_vertex, visited)
                return False


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft')
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
        
    '''
    print('bft')
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft_recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
