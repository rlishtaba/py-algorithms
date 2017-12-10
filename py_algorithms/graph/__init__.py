__all__ = [
    'Graph',
    'Vertex',
    'directed_graph',
    'new_undirected_graph',
    'new_topological_sort_f1',
    'new_dijkstra_shortest_path',
    'reconstruct_dijkstra_path_tree',
]

from typing import List, Callable, Dict

from .adt.graph import Graph
from .adt.vertex import Vertex
from .adt.edge import Edge
from .topological_sort import TopologicalSort
from .dijkstra_shortest_path import DijkstraShortestPath
from .reconstruct_dijkstra_path_tree import ReconstructDijkstraPathTree


def new_directed_graph() -> Graph:
    return Graph(directed=True)


def new_undirected_graph() -> Graph:
    return Graph(directed=False)


def new_topological_sort() -> Callable[[Graph], List[Vertex]]:
    return TopologicalSort()


def new_dijkstra_shortest_path(graph, source):
    return DijkstraShortestPath.apply(graph, source)


def reconstruct_dijkstra_path_tree(
        graph: Graph, source: Vertex, dst: Dict[Vertex, int]) -> Dict[Vertex, Edge]:
    return ReconstructDijkstraPathTree.apply(graph, source, dst)


topological_sort_f1 = new_topological_sort()
