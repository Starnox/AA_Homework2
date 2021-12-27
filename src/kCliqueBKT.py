import pprint
import sys
import itertools
from collections import defaultdict

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """
        return node1 in self._graph and node2 in self._graph[node1]
    
    def get_nodes(self):
        return self._graph.keys()

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
    

if __name__ == '__main__':
    # k the dimension of the clique
    # n is the number of nodes and m the number of edges

    inputFile = sys.argv[1]

    with open(inputFile, 'r') as f:
        k = int(f.readline())
        n = int(f.readline())
        m = int(f.readline())
    
        # quick verification if we don't even have k * (k-1) / 2 edges then it's
        # impossible to have a k-Clique
        if m < (k * (k-1) / 2):
            print(False)
            quit()

        connections = []
        for _ in range (m):
            for line in f: # read rest of lines
                (a,b) = ([int(x) for x in line.split()])
                connections.append((a-1,b-1))
        
        graph = Graph(connections)

        '''
        Solve kClique decision problem using an exponential algorithm 
        using a straightforward approach: it iterates through all all subsets
        of length k and checks if all the nodes in the subset are connected to each other 
        '''
        for subset in list(itertools.combinations(graph.get_nodes(), k)):
            # check in O(n^2) if the every node in the subset is connected to every other node
            valid = True
            for i in range(k-1):
                for j in range(i+1, k):
                    # if is not connected
                    if graph.is_connected(subset[i], subset[j]) == False:
                        valid = False
                        break
                
                if valid == False:
                    break

            # if valid is still true then we found a valid k-Clique
            if valid:
                print(True)
                quit()

        # if by the end we haven't found anything we print false
        print(False)

