from py_algorithms.graph import new_graph, topological_sort_f1


class TestTopologicalSort:
    def test_topological_sort(self):
        dag = new_graph(directed=True)
        a = dag.insert_vertex('A')
        b = dag.insert_vertex('B')
        c = dag.insert_vertex('C')
        d = dag.insert_vertex('D')
        e = dag.insert_vertex('E')

        dag.insert_edge(a, e, None)
        dag.insert_edge(b, d, None)
        dag.insert_edge(c, d, None)
        dag.insert_edge(d, e, None)

        topological_sort_f1(dag)

        t_sorted = topological_sort_f1(dag)
        print(t_sorted)
        assert t_sorted == [c, b, d, a, e]
