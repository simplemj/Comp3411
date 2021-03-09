from aipython.searchGeneric import *
from aipython.searchProblem import *

class UniformCostSearcher(Searcher):
    """ Initializes the forontier """
    def initialize_frontier(self):
        self.frontier = FrontierPQ()

    """ Returns True if there are no more nodes to expand """
    def empty_frontier(self):
        return self.frontier.empty()

    """ Adds the path to the forontier """
    def add_to_frontier(self, path):
        value = path.cost
        self.frontier.add(path, value)