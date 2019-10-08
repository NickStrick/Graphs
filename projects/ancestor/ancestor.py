from graph import Graph
from util import Stack
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    '''

    '''
    ancestor_graph = Graph()
    print(ancestors)
    for i in ancestors:
        ancestor_graph.add_vertex(i[0])
        ancestor_graph.add_vertex(i[1])
        print(i[0])
    for i in ancestors:
        # ancestor_graph.add_edge(i[0], i[1])
        ancestor_graph.add_edge(i[1], i[0])
    print(ancestor_graph.vertices)

    # def dfs(graph, starting_vertex, destination_vertex):

    if ancestor_graph.vertices[starting_node] == set():
        return -1
    stack = Stack()
    visited = set()
    stack.push([starting_node])
    farthest_path = [-1]
    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            if ancestor_graph.vertices[vertex] == set():
                if len(path) > len(farthest_path):
                    farthest_path = list(path)
                elif len(path) == len(farthest_path):
                    if path[-1] < farthest_path[-1]:
                        farthest_path = list(path)
            visited.add(vertex)
            for next_vert in ancestor_graph.vertices[vertex]:
                new_path = list(path)
                new_path.append(next_vert)
                stack.push(new_path)
    return farthest_path[-1]


print(earliest_ancestor(test_ancestors, 8))
