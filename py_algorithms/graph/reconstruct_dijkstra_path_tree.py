from typing import Dict

from .adt.edge import Edge
from .adt.graph import Graph
from .adt.vertex import Vertex


class ReconstructDijkstraPathTree:
    @classmethod
    def apply(cls, graph: Graph, source: Vertex, dst: Dict[Vertex, int]) -> Dict[Vertex, Edge]:
        tree = {}

        for v in dst:
            if v is not source:
                for e in graph.incident_edges(v, False):
                    u = e.opposite(v)
                    w = e.element()
                    if dst[v] == dst[u] + w:
                        tree[v] = e
        return tree
