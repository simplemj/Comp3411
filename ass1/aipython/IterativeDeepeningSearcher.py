from aipython.searchGeneric import *
from aipython.searchProblem import *


class IterativeDeepeningSearcher(Searcher):

    def __init__(self, problem):
        super().__init__(problem)

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
        depth = -1
        while True:
            depth += 1
            while not self.empty_frontier():
                path = self.frontier.pop()
                self.num_expanded += 1
                if self.problem.is_goal(path.end()):
                    self.display(1, self.num_expanded, "paths have been expanded and",
                                 len(self.frontier), "paths remain in the frontier")
                    self.solution = path
                    return path
                if path.cost > depth:
                    continue
                for neighs in reversed(list(self.problem.neighbors(path.end()))):
                    self.add_to_frontier(Path(path, neighs))
            self.initialize_frontier()
            self.add_to_frontier(Path(self.problem.start_node()))



