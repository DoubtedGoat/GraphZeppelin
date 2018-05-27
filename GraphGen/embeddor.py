import networkx as nx;

class Embeddor:
    def st_number(self, graph, start_node):
        nx.set_node_attributes(graph, False, 'old');
        nx.set_edge_attributes(graph, False, 'old');
        # S and T represent the special nodes in our graph - the start
        #   and end of the bipoloar orientation - our ST numbering flows
        #   from S to T
        s = -1;
        t = -1;
        for node in graph.nodes:
            if graph.nodes[node]['dfi'] == 1:
                t = node;
            if graph.nodes[node]['dfi'] == 2:
                s = node;

        # Our starting node = edge are Old already
        graph.nodes[t]['old'] = True;
        graph.nodes[t]['old'] = True;
        graph.add_edge(t, s, key=0, old=True);
        stack = [];
        stack.append(t);
        stack.append(s);
        current_number = 1;
        while len(stack) > 0:
            print "Current Stack:";
            print stack;
            node = stack.pop();
            path = self.pathfinder(graph, start_node);
            # If there's no path we apply the next number and move down the node_stack
            #   Otherwise we push all nodes in the current path onto the stack
            if path == None:
                graph.nodes[node]["ST_number"] = current_number;
                current_number = current_number + 1;
                continue;
            print "Stack Add Breakdown";
            print node;
            print path;
            print "-------";
            while (len(path) > 0):
                edge = path.pop();
                print edge;
                stack.append(edge[1]);
                if len(path) == 0:
                    stack.append(edge[0]);
                    if edge[0] != node:
                        raise Exception("Expected last node on path to be current active node!");

    # PATHFINDER algorithm from Computing An ST-Numbering (Even + Tarjan)
    # This code is _disgusting_. Revisit and clean it up a bit
    def pathfinder(self, graph, node):
        # Condition 1 - 'new' cycle edge {node,neighbor} where
        #   neighbor is an ancestor of node
        selected_edge = -1;
        for edge in graph.edges(node):
            if (not graph.get_edge_data(*edge)['old']) and (not graph.get_edge_data(*edge)['tree_edge']):
                if self.is_ancestor(graph, edge[0], edge[1]):
                    selected_edge = edge;
        if selected_edge != -1:
            graph.add_edge(selected_edge[0], selected_edge[1], key=0, old=True);
            return [selected_edge];

        # Condition 2 - If there is a 'new' tree edge
        for edge in graph.edges(node):
            if (not graph.get_edge_data(*edge)['old']) and graph.get_edge_data(*edge)['tree_edge']:
                selected_edge = edge;
        if selected_edge != -1:
            graph.add_edge(selected_edge[0], selected_edge[1], key=0, old=True);
            path = [selected_edge];
            while graph.nodes[selected_edge[1]]['old'] == False:
                v = selected_edge[0];
                w = selected_edge[1];
                graph.nodes[w]['old'] = True;
                # We have edge {v, w}. Find a new edge with {w, x} where
                #  Lowpoint(w) = DFI(x) OR Lowpoint(x) = Lowpoint(w)
                new_edge = -1;
                for edge in graph.edges(w):
                    x = edge[0] if edge[0] != w else edge[1];
                    if ((graph.nodes[x]['dfi'] == graph.nodes[w]['lowpoint']) or
                        (graph.nodes[x]['lowpoint'] == graph.nodes[w]['lowpoint'])):
                        new_edge = [w, x];
                if new_edge == -1:
                    raise Exception('Should have found a node in PATHFINDER case 2!!');
                selected_edge = new_edge;
                path.append(selected_edge);
            return path;

        # Condition 3 - 'new' cycle edge {node, neighbor} where
        #   node is an ancestor of neighbor. (Inverse of Case 1)
        for edge in graph.edges(node):
            if (not graph.get_edge_data(*edge)['old']) and (not graph.get_edge_data(*edge)['tree_edge']):
                if self.is_ancestor(graph, edge[1], edge[0]):
                    selected_edge = edge;
        if selected_edge != -1:
            graph.add_edge(selected_edge[0], selected_edge[1], key=0, old=True);
            path = [selected_edge];
            while graph.nodes[selected_edge[1]]['old'] == False:
                v = selected_edge[0];
                w = selected_edge[1];
                graph.nodes[w]['old'] = True;
                # We have edge {v, w}. Find a new edge with {w, x} where
                #  x is the parent of w
                new_edge = -1;
                for edge in graph.edges(w):
                    x = edge[0] if edge[0] != w else edge[1];
                    if (graph.nodes[w]['dfs_parent'] == x):
                        new_edge = [w, x];
                if new_edge == -1:
                    raise Exception('Should have found a node in PATHFINDER case 3!!');
                selected_edge = new_edge;
                path.append(selected_edge);
            return path;

            return None;

    def is_ancestor(self, graph, base, check):
        if graph.nodes[base]['dfs_parent'] == 0:
            return False;
        if graph.nodes[base]['dfs_parent'] == check:
            return True;
        return self.is_ancestor(graph, graph.nodes[base]['dfs_parent'], check);

    # Recursive function for Hopcroft Tarjan algorithm for setting depth and lowpoint
    #   values during a DFS.
    # https://wiki.algo.informatik.tu-darmstadt.de/Hopcroft-Tarjan
    def hopcroft_tarjan(self, graph, start_node):
        nodes = [];
        nx.set_node_attributes(graph, False, 'visited');
        nx.set_edge_attributes(graph, False, 'tree_edge');
        self.visit_node(graph, start_node, nodes, 1, 1);

    def visit_node(self, graph, start_node, node_stack, depth, dfi):
        if not graph.nodes[start_node]['visited']:
            graph.nodes[start_node]['dfs_parent'] = node_stack[-1] if (len(node_stack) > 0) else 0;
            graph.nodes[start_node]['visited'] = True;
            graph.nodes[start_node]['dfi'] = dfi;
            dfi += 1 ;
            graph.nodes[start_node]['depth'] = depth;
            graph.nodes[start_node]['lowpoint'] = depth;
        next_node = -1;
        for node in graph.neighbors(start_node):
            if graph.nodes[node]['visited']:
                graph.nodes[start_node]['lowpoint'] = min(graph.nodes[node]['depth'], graph.nodes[start_node]['lowpoint']);
            else:
                next_node = node;

        # If we have no unvisited neighbors, go back up the stack and leave our
        #  dfi number unchanged
        if next_node == -1:
            if not node_stack:
                return;
            next_node = node_stack.pop();
            graph.nodes[next_node]['lowpoint'] = min(graph.nodes[next_node]['lowpoint'], graph.nodes[start_node]['lowpoint']);
            self.visit_node(graph, next_node, node_stack, depth - 1, dfi);
        else:
            graph.add_edge(start_node, next_node, key=0, tree_edge=True);
            node_stack.append(start_node);
            self.visit_node(graph, next_node, node_stack, depth + 1, dfi)
