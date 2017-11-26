__all__ = [
    'Graph',
    'Vertex',
    'directed_graph'
    'new_undirected_graph'
    'new_topological_sort_f1'
]

from typing import List, Callable

from .adt.graph import Graph
from .adt.vertex import Vertex
from .topological_sort import TopologicalSort


def new_directed_graph() -> Graph:
    return Graph(directed=True)


def new_undirected_graph() -> Graph:
    return Graph(directed=False)


def new_topological_sort() -> Callable[[Graph], List[Vertex]]:
    return TopologicalSort()


topological_sort_f1 = new_topological_sort()
