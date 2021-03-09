import sys
sys.path.insert(0, "aipython")
from aipython.searchGeneric import *
from aipython.GameFifteenProblem import GameFifteenProblem
from aipython.BreadthFirstSearcher import BreadthFirstSearcher
from aipython.UniformCostSearcher import UniformCostSearcher
from aipython.IterativeDeepeningSearcher import IterativeDeepeningSearcher
from aipython.IterativeDeepeningAStarSearcher import IterativeDeepeningAStarSearcher
goal = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]]

start = [[1, 2, 3, 4],
         [9, 5, 6, 7],
         [10, 11, 8, 0],
         [13, 14, 15, 12]]

start14 = [[1, 2, 8, 3],
           [5, 6, 7, 4],
           [9, 15, 14, 11],
           [13, 10, 12, 0]]

# optimal path cost: 17
start17 = [[1, 3, 6, 4],
           [5, 2, 8, 14],
           [9, 15, 7, 0],
           [13, 10, 12, 11]]

# optimal path cost: 23
start23 = [[1, 3, 6, 4],
           [5, 8, 15, 14],
           [9, 2, 7, 0],
           [13, 10, 12, 11]]

# optimal path cost: 10
start10 = [[2, 3, 7, 4],
           [1, 6, 11, 8],
           [5, 10, 0, 12],
           [9, 13, 14, 15]]

# optimal path cost: 24
start24 = [[2, 7, 11, 4],
           [6, 3, 12, 0],
           [1, 5, 15, 8],
           [9, 10, 13, 14]]

# optimal path cost: 30
start30 = [[2, 7, 11, 4],
           [6, 3, 12, 0],
           [1, 5, 15, 14],
           [9, 10, 8, 13]]

# optimal path cost: 36
start36 = [[7, 11, 12, 4],
           [2, 3, 14, 1],
           [6, 5, 13, 8],
           [9, 10, 15, 0]]

# optimal path cost: 41
start41 = [[7, 11, 12, 4],
           [2, 3, 8, 14],
           [10, 0, 5, 1],
           [6, 9, 13, 15]]

start37_1 = [[7, 11, 12, 4],
             [2, 3, 14, 1],
             [6, 5, 13, 0],
             [9, 10, 15, 8]]

start37_2 = [[7, 11, 12, 4],
             [2, 3, 8, 14],
             [6, 0, 1, 15],
             [9, 5, 10, 13]]
# your code
puzzle = GameFifteenProblem(start30, goal)
#searcher = AStarSearcher(puzzle)
#searcher = BreadthFirstSearcher(puzzle)
#searcher = IterativeDeepeningSearcher(puzzle)
searcher = UniformCostSearcher(puzzle)
#searcher = IterativeDeepeningAStarSearcher(puzzle)
solution = searcher.search()
print('Cost: ',  solution.cost)

