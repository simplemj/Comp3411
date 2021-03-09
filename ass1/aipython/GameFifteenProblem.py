from aipython.searchProblem import *
import numpy as np

class GameFifteenProblem(Search_problem):

    def __init__(self, start, goal):
        start = np.array(start)
        goal = np.array(goal)
        self.start = start
        self.goal = goal
        return

    def start_node(self):
        """Returns the start node"""

        return self.start

    def is_goal(self, node):
        """Returns True if the node is the goal, otherwise False"""
        np_node = np.array(node)
        np_goal = np.array(self.goal)
        if (np_node != np_goal).any():
            return False
        else:
            return True

    def neighbors(self, node):
        """Returns a list of the arcs for the neighbors of node, for example:
        return [Arc(node, to_neighbor_node1, cost1), Arc(node, to_neighbor_node2, cost2)]"""
        res = []
        np_node = np.array(node)
        zero_point_tuple = np.where(np_node == 0)
        x = int(zero_point_tuple[0])
        y = int(zero_point_tuple[1])
        if x - 1 in range(4):
            top = np_node.copy()
            top[x][y] = top[x - 1][y]
            top[x - 1][y] = 0
            top = top.tolist()
            tmp = Arc(node, top)
            res.append(tmp)
        if x + 1 in range(4):
            down = np_node.copy()
            down[x][y] = down[x + 1][y]
            down[x + 1][y] = 0
            down = down.tolist()
            tmp = Arc(node, down)
            res.append(tmp)
        if y - 1 in range(4):
            left = np_node.copy()
            left[x][y] = left[x][y - 1]
            left[x][y - 1] = 0
            left = left.tolist()
            tmp = Arc(node, left)
            res.append(tmp)
        if y + 1 in range(4):
            right = np_node.copy()
            right[x][y] = right[x][y + 1]
            right[x][y + 1] = 0
            right = right.tolist()
            tmp = Arc(node, right)
            res.append(tmp)
        return res

    def heuristic(self, node):
        """Returns the heuristic value of the node
        based on the Manhattan distance"""
        res = 0
        np_node = np.array(node)
        for i in range(4):
            for j in range(4):
                tmp = self.goal[i][j]
                if tmp != 0:
                    point = np.where(np_node == tmp)
                    x = int(point[0])
                    y = int(point[1])
                    distance = abs(x - i) + abs(y - j)
                    res += distance
        return res