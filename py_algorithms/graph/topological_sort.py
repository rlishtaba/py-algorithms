from typing import List

from .adt.graph import Graph

from .adt.vertex import Vertex


class TopologicalSort:
    """
    Representing topological sort for a given DAG ADT
    """

    def __call__(self, graph: Graph) -> List[Vertex]:
        degrees = {}
        queue = []
        in_order = []

        for u in graph.vertices():
            degrees[u] = graph.degree(u, outgoing=False)
            if degrees[u] == 0:
                queue.append(u)

        while len(queue) > 0:
            u = queue.pop()
            in_order.append(u)
            for edge in graph.incident_edges(u):
                v = edge.opposite(u)
                degrees[v] -= 1
                if degrees[v] == 0:
                    queue.append(v)

        return in_order
