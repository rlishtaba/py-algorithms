from typing import List
from typing import Tuple
from typing import Union


class WeightedPath:
    INF = float('infinity')

    @staticmethod
    def make_lists(vertices: List[str],
                   triplets: List[Tuple[str, str, int]]) -> Tuple[dict, dict]:
        adj = {}
        edges = {}
        for v in vertices:
            adj[v] = {}
            edges[v] = {}
            for w in vertices:
                adj[v][w] = WeightedPath.INF
                edges[v][w] = {}
        for t in triplets:
            adj[t[0]][t[1]] = int(t[2])
            adj[t[1]][t[0]] = int(t[2])
            # graph will have cycles.
            edges[t[0]][t[1]] = [t[0], t[1], int(t[2])]
            edges[t[1]][t[0]] = [t[1], t[0], int(t[2])]
        return adj, edges

    @classmethod
    def path(cls, s: str, t: str, edge_to: dict,
             distances: dict) -> List[str]:
        if not (distances[s][t] < cls.INF):
            return []
        paths = []
        e = edge_to[s][t]
        while e:
            paths.append(e)
            # graph is cyclic, should stop on cycle
            if e[0] == s:
                break
            e = edge_to[s][e[0]]
        return paths

    @classmethod
    def fw_traverse(cls, vertices: List[str],
                    triplets: List[Tuple[str, str, int]]) -> Tuple[dict, dict]:
        """
        Floyd-Warshall traversal. Can handle negative weights,
        Dijkstra's algorithm works only with positive weights.
        """
        distances, edge_to = cls.make_lists(vertices, triplets)
        nodes = distances.keys()
        for i in nodes:
            for v in nodes:
                if not edge_to[v][i]:
                    continue
                for w in nodes:
                    if distances[v][w] > distances[v][i] + distances[i][w]:
                        distances[v][w] = distances[v][i] + distances[i][w]
                        edge_to[v][w] = edge_to[i][w]
        return edge_to, distances

    def __call__(self, str_arr: List[str]) -> Union[str, int]:
        node_len = int(str_arr[0])
        vertices = str_arr[1:node_len + 1]
        triplets = [x.split('|') for x in str_arr[node_len + 1:]]
        edges, distances = self.fw_traverse(vertices, triplets)
        # compute shortest paths using Floyd - Warshall algorithm.
        sp = self.path(vertices[0], vertices[node_len - 1], edges, distances)
        # if list is empty - no path
        if len(sp) == 0:
            return -1
        else:
            xs = [vertices[node_len - 1]]
            xs += [x[0] for x in sp]
            xs.reverse()
            return "-".join(xs)
