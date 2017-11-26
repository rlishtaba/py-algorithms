from py_algorithms.graph import new_graph, topological_sort_f1


class TestTopologicalSort:
    def test_topological_sort(self):
        g = new_graph(directed=True)
        j = g.insert_vertex('J')
        k = g.insert_vertex('K')
        c = g.insert_vertex('C')
        p = g.insert_vertex('P')
        s = g.insert_vertex('S')
        g.insert_edge(j, s, None)
        g.insert_edge(k, p, None)
        g.insert_edge(c, p, None)
        g.insert_edge(p, s, None)

        t_sorted = topological_sort_f1(g)
        assert t_sorted == [c, k, p, j, s]
