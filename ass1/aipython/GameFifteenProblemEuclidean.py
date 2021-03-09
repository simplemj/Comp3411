from aipython import GameFifteenProblem
import numpy as np

class GameFifteenProblemEuclidean(GameFifteenProblem):
    def __init__(self, start, goal):
        (super().__init__(start, goal))

    def heuristic(self, node):
        """Returns the heuristic value of the node
        based on the Euclidean distance"""
        res = 0
        np_node = np.array(node)
        for i in range(4):
            for j in range(4):
                tmp = self.goal[i][j]
                if tmp != 0:
                    point = np.where(np_node == tmp)
                    x = int(point[0])
                    y = int(point[1])
                    distance = np.sqrt(np.square(x - i) + np.square(y - j))
                    res += distance
        return res
