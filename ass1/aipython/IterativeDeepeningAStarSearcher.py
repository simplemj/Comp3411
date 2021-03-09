from aipython.searchGeneric import *
from aipython.searchProblem import *
import time
class IterativeDeepeningAStarSearcher(Searcher):
    """ Initializes the forontier """

    def initialize_frontier(self):
        self.frontier = []

    """ Returns True if there are no more nodes to expand """

    def empty_frontier(self):
        return self.frontier == []

    """ Adds the path to the forontier """

    def add_to_frontier(self, path):
        self.frontier.append(path)

    def search(self):
        start_time = time.time()
        thredshold = self.problem.heuristic(self.problem.start_node())
        while True:
            if time.time() - start_time > 300:
                return "Out of Time"
            min_value = float("inf")
            while not self.empty_frontier():
                path = self.frontier.pop()
                self.num_expanded += 1
                if self.problem.is_goal(path.end()):
                    self.display(1, self.num_expanded, "paths have been expanded and",
                                 len(self.frontier), "paths remain in the frontier")
                    self.solution = path
                    return path
                fn = path.cost + self.problem.heuristic(path.end())
                if fn > thredshold:
                    if fn < min_value:
                        min_value = fn
                    continue
                for neighs in reversed(list(self.problem.neighbors(path.end()))):
                    self.add_to_frontier(Path(path, neighs))

            thredshold = min_value
            self.initialize_frontier()
            self.add_to_frontier(Path(self.problem.start_node()))
