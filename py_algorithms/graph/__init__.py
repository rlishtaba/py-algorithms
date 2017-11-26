__all__ = [
    'Graph',
    'new_graph'
]

from .adt.graph import Graph


def new_graph(directed: bool = False) -> Graph:
    return Graph(directed)
