from typing import Any, Iterator
from typing import List
from typing import Set
from typing import Union

from .edge import Edge
from .vertex import Vertex


class Graph:
    def __init__(self, directed: bool = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self) -> bool:
        return self._incoming is not self._outgoing

    def vertex_count(self) -> int:
        return len(self._outgoing)

    def vertices(self) -> List[Vertex]:
        return list(self._outgoing.keys())

    def edge_count(self) -> int:
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self) -> Set[Edge]:
        result = set()
        for sub_map in self._outgoing.values():
            result.update(sub_map.values())
        return result

    def get_edge(self, u, v) -> Union[None, Edge]:
        return self._outgoing[u].get(v)

    def degree(self, v: Vertex, outgoing: bool = True) -> int:
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self,
                       v: Vertex,
                       outgoing: bool = True) -> Iterator[Edge]:
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, element: Any = None) -> Vertex:
        v = Vertex(element)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, origin: Vertex, destination: Vertex,
                    element: Any) -> Edge:
        e = Edge(origin, destination, element)
        self._outgoing[origin][destination] = e
        self._incoming[destination][origin] = e
        return e
