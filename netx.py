import networkx as nx
from random import choices
from itertools import product
from matplotlib import pyplot

class Grapher:

    def generate_n(self, n):
        G = nx.Graph()
        G.add_nodes_from(range(0,n))
        return G
    
    def build_connected(self, G):
        for x in choices(product(range(0,len(G))),k=len(G)*len(G)):
            G.add_edge(x)
            if nx.is_connected(G) :
                break
        return G

    def sample_graphs(self, samples, size):
        sampleset = []
        for _ in range(0,samples) :
            G = self.generate_n(size)
            if nx.is_connected(self.build_connected(G)) :
                sampleset += len(G.edges)
        return sampleset

graph = Grapher()
samplemat = []
for i in range(0, stop=100, step=5):
    ss = graph.sample_graphs(30,i)
    samplemat += ss
sm = map(sum(),samplemat)
f = pyplot.figure()
pyplot.plot(range(0,stop=100,step=5),sm)
pyplot.show()
