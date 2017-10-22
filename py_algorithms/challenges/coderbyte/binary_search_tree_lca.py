import ast


class BinarySearchTreeLca:
    def __call__(self, str_arr: str) -> str:
        tree_nodes = ast.literal_eval(str_arr[0])
        _left = int(str_arr[1])
        _right = int(str_arr[2])
        _max = max(_left, _right)
        _min = min(_left, _right)
        _low = min(tree_nodes.index(_min), tree_nodes.index(_max))
        xs = []
        for x in tree_nodes[0:_low + 1]:
            if x <= _max:
                xs.append(x)
        return max(xs)
