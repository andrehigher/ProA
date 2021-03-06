""" A Python Class
A simple Python util class to do essential stuffs.
"""
import operator
import json
import networkx as nx
from collections import defaultdict

class Util():
    
    def read_file(self, file, graph, directed = True):
        """ A method to read the file and append to the
            graph the properly vertex and edges.
        """
        g = graph.get_graph()

        # g.add_edge('Morgan_Freeman','Male',relation='gender')
        # graph.set_relation('Morgan_Freeman','Male','gender')
        # g.add_edge('Morgan_Freeman','Actor',relation='profession')
        # graph.set_relation('Morgan_Freeman','Actor','profession')
        # g.add_edge('Male','Chris_Rock',relation='gender')
        # graph.set_relation('Male','Chris_Rock','gender')
        # g.add_edge('Chris_Rock','Oscar',relation='hosted')
        # graph.set_relation('Chris_Rock','Oscar','hosted')
        # g.add_edge('Actor','Tom_Hanks',relation='profession')
        # graph.set_relation('Actor','Tom_Hanks','profession')
        # g.add_edge('Actor','Sean_Penn',relation='profession')
        # graph.set_relation('Actor','Sean_Penn','profession')
        # g.add_edge('Actor','Leo_DiCaprio',relation='profession')
        # graph.set_relation('Actor','Leo_DiCaprio','profession')
        # g.add_edge('Tom_Hanks','Oscar',relation='won_award')
        # graph.set_relation('Tom_Hanks','Oscar','won_award')
        # g.add_edge('Sean_Penn','Oscar',relation='won_award')
        # graph.set_relation('Sean_Penn','Oscar','won_award')
        # g.add_edge('Leo_DiCaprio','Oscar',relation='won_award')
        # graph.set_relation('Leo_DiCaprio','Oscar','won_award')
        with open(file, 'r') as f:
            for line in f:
                line2 = line.split('\t')
                line2[2] = line2[2][:-1]
                if directed == True:
                    g.add_edge(line2[0],line2[2],relation=line2[1])
                    graph.set_relation(line2[0],line2[2],line2[1])
                else:
                    g.add_edge(line2[0],line2[2])

    def generate_edges_probabilities(self, store):
        """ A method to Generate dictionary for 
            edges distribution probability.
        """
        sorted_store = sorted(store.items(), key=operator.itemgetter(1))
        with open('file.txt', 'w') as file:
            file.write(json.dumps(sorted_store))

    def generate_edges_distribution(self, graph, store):
        g = graph.get_graph()
        relations = nx.get_edge_attributes(g,'relation')

        for node in g.nodes():
            for neighbor in g.neighbors(node):
                try:
                    currentRelation = relations[(node, neighbor)]
                    for neighbor_neighbor in g.neighbors(neighbor):
                        store[currentRelation]['adjacent_edges'][relations[(neighbor, neighbor_neighbor)]] += 1
                except KeyError as e:
                    pass
        for s in store:
            print(s, store[s]['count'])