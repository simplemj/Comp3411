from aipython.GameFifteenProblem import GameFifteenProblem
import numpy as np

class GameFifteenProblemInversions(GameFifteenProblem):
    def __init__(self, start, goal):
        (super().__init__(start, goal))

    def heuristic(self, node):
        """Returns the heuristic value of the node
        based on the sum of the inversion number of a permutation"""
        res = 0
        np_node = np.array(node)
        np_flatten = np_node.flatten()
        node_list = np_flatten.tolist()
        for i in range(16):
            j = i
            for j in range(j, 16):
                if node_list[j] != 0 and node_list[i] > node_list[j]:
                    res += 1

        return res
