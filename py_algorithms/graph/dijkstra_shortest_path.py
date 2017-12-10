from typing import Dict

from ..data_structures import new_priority_queue
from .adt.graph import Graph
from .adt.vertex import Vertex
from py_algorithms.data_structures import PriorityQueue


class DijkstraShortestPath:
    @classmethod
    def apply(cls, graph: Graph, source: Vertex) -> Dict[Vertex, int]:
        distances = {}
        visited = {}
        pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == -1)

        for v in graph.vertices():
            if v is source:
                distances[v] = 0
            else:
                distances[v] = float('inf')
            pq.push(v, distances[v])

        while pq.size > 0:
            u = pq.pop()
            visited[u] = distances[u]

            for e in graph.incident_edges(u):
                v = e.opposite(u)

                if v not in visited:
                    # perform edge relaxation
                    w = e.element()
                    if distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        pq = cls._rebuild_pq(pq, distances)

        return visited

    @staticmethod
    def _rebuild_pq(pq: PriorityQueue, dst: Dict[Vertex, int]) -> PriorityQueue:
        tmp = []
        while pq.size > 0:
            tmp.append(pq.pop())

        for v in tmp:
            pq.push(v, dst[v])

        return pq
