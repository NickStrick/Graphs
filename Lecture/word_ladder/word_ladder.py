# Given two words (beginWord and endWord), and a dictionary's word list,
# return the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Sample:
# beginWord = "hit"
# endWord = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# beginWord = "sail"
# endWord = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None


'''
Words - vertex
letters different - edges (part)
shortest transformation sequence - path/bfs
Dictionary - list of vertexes
BginWord - starting vertex
EndWord - destination vertex
no duplicates - use a set()
same length - edges (part)
'''


f = open('words.txt', 'r')
# words = [x.lower() for x in f.readlines()]
words = f.read().split("\n")
word_set = set()
for word in words:
    word_set.add(word.lower())


# find/create all nodes/edges for words with one letter differece
# replaces entry in the adjacency list for that node
def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list("abcdefghijklmnopqrstuvqxyz"):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

# Queue class


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


def find_word_ladder(beginWord, endWord):
    # que = Queue()
    # visited = set()
    # que.enqueue([starting_vertex])

    # while que.size() > 0:
    #     path = que.dequeue()
    #     vertex = path[-1]
    #     if vertex not in visited:
    #         # Here is the point to do whatever we're trying to accomplish
    #         if vertex == destination_vertex:
    #             return path
    #         visited.add(vertex)
    #         for next_vert in self.vertices[vertex]:
    #             new_path = list(path)
    #             new_path.append(next_vert)
    #             que.enqueue(new_path)

    que = Queue()
    visited = set()
    que.enqueue([beginWord])

    while que.size() > 0:
        path = que.dequeue()
        vertex = path[-1]  # Vertex is our word
        if vertex not in visited:
            # Here's where we do the thing!
            if vertex == endWord:
                return path
            visited.add(vertex)
            for new_word in get_neighbors(vertex):
                new_path = list(path)
                new_path.append(new_word)
                que.enqueue(new_path)


print(find_word_ladder("sail", "boat"))
