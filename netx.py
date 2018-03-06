import networkx as nx
from random import choice
from itertools import permutations
from matplotlib import pyplot

class Grapher:

    def generate_n(self, n):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(range(0,n))
    
    def build_connected(self):
        prod = list(permutations(range(0,len(self.graph)),2))
        while not nx.is_connected(self.graph) :
            (x,y) = choice(prod)
            self.graph.add_edge(x,y)

    def sample_graphs(self, samples, size):
        sampleset = 0
        for _ in range(0,samples) :
            self.generate_n(size)
            self.build_connected()
            sampleset += len(self.graph.edges)
        return sampleset/samples


def main():
    graph = Grapher()
    samplemat = []
    for i in range(5, 100, 5):
        samplemat.append(graph.sample_graphs(30,i))
    f = pyplot.figure()
    pyplot.plot(range(5, 100, 5),samplemat)
    pyplot.savefig('graphsampling.pdf')
    pyplot.close(f)

main()
