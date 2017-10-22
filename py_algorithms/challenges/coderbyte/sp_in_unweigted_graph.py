from typing import Union


class SPUnweightedCyclicGraph:
    """
    Have the function f(strArr) take strArr which will be an array of strings which
    models a non-looping Graph.The structure of the array will be as follows:
    The first element in the array will be the number of nodes N (points) in the
    array as a string. The next N elements will be the nodes which can be anything
    (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element,
    the rest of the elements in the array will be the connections between all of the nodes.
    They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.).
    Although, there may exist no connections at all.

    Input example: ["4", "A", "B", "C", "D", "A-B", "B-D", "B-C", "C-D"]
    Expected output: 'A-B-D'
    """

    def __call__(self, str_arr: str) -> Union[str, int]:
        nodes_count = int(str_arr[0])
        nodes = str_arr[1:nodes_count + 1]
        connections = [x.split('-') for x in str_arr[nodes_count + 1:]]

        _from = nodes[0]
        _to = nodes[len(nodes) - 1]
        _adj = self._make_adj_list(connections)

        traversal = Bfs(_adj, _from)
        path = traversal.path_to(_to)

        if not path:
            return -1
        return '-'.join(path)

    # Construct adjacency list, so it could be
    # consumed by DFS algorithm
    @staticmethod
    def _make_adj_list(connections):
        adj_list = {}
        for pair in connections:
            # assign an empty list if not exist yet
            for x in pair:
                if not adj_list.get(x, False):
                    adj_list[x] = []
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
        return adj_list


class Bfs:
    def __init__(self, adj, s):
        self.marked = {}
        self.dist_To = {}
        self.edge_to = {}
        self._bfs(adj, s)

    def path_to(self, v):
        if not self.marked.get(v, False):
            return False
        q = []
        x = v
        q.append(v)
        while not self.dist_To.get(x) == 0:
            x = self.edge_to[x]
            q.append(x)
        q.reverse()
        return q

    # Simple BFS algorithm, it is shortest way to find shortest path
    # on unweighted graph
    def _bfs(self, adj, s):
        q = []
        for v in adj.keys():
            self.dist_To[v] = float('infinity')
        self.dist_To[s] = 0
        self.marked[s] = True
        q.append(s)

        while not len(q) == 0:
            v = q.pop(0)
            for w in adj.get(v, []):
                if not self.marked.get(w, False):
                    self.edge_to[w] = v
                    self.dist_To[w] = self.dist_To[v] + 1
                    self.marked[w] = True
                    q.append(w)

    def __repr__(self):
        return "#<{} edge_to={} dist_To={}>".format(
            self.__class__.__name__, self.edge_to, self.dist_To)
