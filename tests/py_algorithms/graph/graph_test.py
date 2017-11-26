from py_algorithms.graph import new_graph


class TestGraphApi:
    def test_graph_constructor(self):
        g = new_graph()
        v1 = g.insert_vertex("A")
        v2 = g.insert_vertex("B")
        v3 = g.insert_vertex("C")
        g.insert_edge(v1, v2, 1)
        g.insert_edge(v1, v3, 2)
        assert g.degree(v1) == 2
