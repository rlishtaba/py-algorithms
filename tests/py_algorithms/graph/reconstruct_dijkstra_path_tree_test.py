from py_algorithms.graph import new_dijkstra_shortest_path
from py_algorithms.graph import new_undirected_graph
from py_algorithms.graph import reconstruct_dijkstra_path_tree


class TestReconstructDijkstraPathTree:
    def test_apply(self):
        graph = new_undirected_graph()
        a = graph.insert_vertex('A')
        b = graph.insert_vertex('B')
        c = graph.insert_vertex('C')
        d = graph.insert_vertex('D')
        e = graph.insert_vertex('E')

        graph.insert_edge(a, e, 10)
        graph.insert_edge(b, d, 2)
        graph.insert_edge(c, d, 3)
        graph.insert_edge(d, e, 12)

        paths = new_dijkstra_shortest_path(graph, c)

        assert paths[c] == 0
        assert paths[d] == 3
        assert paths[b] == 5
        assert paths[e] == 15
        assert paths[a] == 25

        path_tree = reconstruct_dijkstra_path_tree(graph, c, paths)

        p = a
        stack = []
        while p != c:
            stack.append(p)
            p = path_tree[p].opposite(p)
        stack.append(p)

        assert stack == [a, e, d, c]
