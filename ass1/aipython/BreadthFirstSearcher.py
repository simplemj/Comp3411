from aipython.searchGeneric import *
from aipython.searchProblem import *

class BreadthFirstSearcher(Searcher):

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

    """returns (next) path from the problem's start node
        to a goal node. """

    def search(self):
        while not self.empty_frontier():
            if len(self.frontier) > 1000000:
                return print("Out of Memory")
            path = self.frontier.pop(0)
            self.num_expanded += 1
            for neighs in self.problem.neighbors(path.end()):
                if self.problem.is_goal(neighs.to_node):
                    self.display(1, self.num_expanded, "paths have been expanded and",
                                 len(self.frontier), "paths remain in the frontier")
                    path = Path(path, neighs)
                    self.solution = path
                    return path
                self.add_to_frontier(Path(path, neighs))

