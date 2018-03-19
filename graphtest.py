import GraphGen;

g = GraphGen.Generator("img/one/");
graph = g.generate();
e = GraphGen.Embeddor();
start_node = next(iter(graph.nodes));
e.hopcroft_tarjan(graph, start_node)
e.st_number(graph, start_node)
