import GraphGen;
import networkx as nx;

while True:
    print "#######################################################################"
    print "NEW CYCLE"
    g = GraphGen.Generator("img/one/");
    graph = g.generate();
    while not nx.is_biconnected(graph):
        graph = g.generate();
    e = GraphGen.Embeddor();
    start_node = next(iter(graph.nodes));
    e.hopcroft_tarjan(graph, start_node)
    e.st_number(graph, start_node)

