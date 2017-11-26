__all__ = [
    'Graph',
    'Vertex',
    'new_graph'
    'topological_sort_f1'
]

from typing import List, Callable

from .adt.graph import Graph
from .adt.vertex import Vertex
from .topological_sort import TopologicalSort


def new_graph(directed: bool = False) -> Graph:
    return Graph(directed)


def new_topological_sort() -> Callable[[Graph], List[Vertex]]:
    return TopologicalSort()


topological_sort_f1 = new_topological_sort()
