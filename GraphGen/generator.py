import networkx as nx;
import random;
import os;
import errno;

#https://github.com/hagberg/planarity
import planarity;

class Generator:
    export_location = './';

    def __init__(self, location):
        self.export_location = location;

    def generate(self):
        subgraphs = [];
        sg_count = random.choice(range(3,5));
        for i in range(sg_count):
            subgraphs.append(self.generateCycle(random.choice(range(5, 10))));
        graph = nx.compose_all(subgraphs);
        while not planarity.is_planar(graph):
            k_subgraph=planarity.kuratowski_subgraph(graph);
            graph.remove_edge(*next(iter(k_subgraph.edges)));
        self.export(graph, 'composition');
        for index, subgraph in enumerate(subgraphs):
            self.export(subgraph, str(index));
        return graph;

    def generateCycle(self, length):
        namelist = range(20);
        cycle = nx.Graph();
        prevNode = None;
        firstNode = None;
        for i in range(length):
            name = random.choice(namelist);
            namelist.remove(name);
            cycle.add_node(name);
            if i == 0:
                firstNode = name; #This looks retarded now but eventually we'll change node names
            if prevNode is not None:
                cycle.add_edge(prevNode, name);
            if i == length - 1:
                cycle.add_edge(firstNode, name);
            prevNode = name;
        return cycle;

    def export(self, graph, name):
        gv_graph = nx.nx_agraph.to_agraph(graph);        # convert to a graphviz graph
        gv_graph.layout();            # neato layout
        try:
            os.makedirs(self.export_location)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST:
                pass
            else:
                raise
        gv_graph.draw(self.export_location + name + ".png");
