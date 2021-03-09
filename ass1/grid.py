import sys
sys.path.insert(0, "aipython")
from aipython.searchGeneric import *
from aipython.GameFifteenProblem import GameFifteenProblem
from aipython.BreadthFirstSearcher import BreadthFirstSearcher
from aipython.UniformCostSearcher import UniformCostSearcher
from aipython.IterativeDeepeningSearcher import IterativeDeepeningSearcher
from aipython.IterativeDeepeningAStarSearcher import IterativeDeepeningAStarSearcher
import numpy as np
from aipython.cspSearch import *
from aipython.cspProblem import *
constraints = []
grid = [[9, 5, 0, 8, 2, 7, 3, 0, 0],
        [0, 8, 0, 1, 4, 0, 0, 5, 0],
        [0, 1, 0, 5, 9, 0, 0, 0, 0],
        [8, 3, 0, 0, 0, 0, 0, 7, 5],
        [1, 6, 9, 7, 5, 2, 4, 3, 0],
        [0, 7, 0, 0, 8, 0, 0, 6, 0],
        [0, 9, 1, 0, 6, 0, 8, 4, 0],
        [7, 0, 8, 0, 3, 1, 0, 6, 6],
        [6, 2, 0, 4, 7, 8, 0, 9, 0]]


def check_rules(point,np_grid):
    x = int(point[0])
    y = int(point[1])
    np_grid_3_3 = [np_grid[x//3*3+i][y//3*3+j] for i in range(3) for j in range(3)]
    res = set(range(1,10)) - set(np_grid_3_3) - set(np_grid[x]) - set(list(zip(*np_grid))[y])

    return list(res)





def create_constraint(array):
    for i in range(len(array)):
        j = i + 1
        while j < len(array):
            tmp = Constraint([array[i],array[j]],ne)
            constraints.append(tmp)
            j += 1

def ne(a,b):
    return a != b

def check_x():
    for i in range(9):
        column_array = np.where(np_grid[i] == 0)
        tuple_array = []
        for j in column_array[0]:
            tmp = (i, j)
            tuple_array.append(tmp)
        create_constraint(tuple_array)

def check_y():
    for i in range(9):
        column_array = np.where(np_grid[...,i] == 0)
        tuple_array = []
        for j in column_array[0]:
            tmp = (i, j)
            tuple_array.append(tmp)
        create_constraint(tuple_array)


def check_3_3():
    for i in range(3):
        for j in range(3):
            array = []
            for point in point_array:
                if (i*3 <= point[0] < (i+1)*3) and (j*3 <= point[1] < (j+1)*3):
                    array.append(point)
            create_constraint(array)

def grid_to_csp(grid):
    np_grid = np.array(grid)
    zero_point = np.where(np_grid == 0)
    x_array = zero_point[0]
    y_array = zero_point[1]
    point_array = []
    for i in range(len(x_array)):
        point = (x_array[i], y_array[i])
        point_array.append(point)
    domains = {point_array[i]:check_rules(point_array[i],np_grid) for i in range(len(point_array))}
    constraints = []
    for i in range(9):
        column_array = np.where(np_grid[i] == 0)
        tuple_array = []
        for j in column_array[0]:
            tmp = (i, j)
            tuple_array.append(tmp)
        for i in range(len(tuple_array)):
            j = i + 1
            while j < len(tuple_array):
                tmp = Constraint([tuple_array[i], tuple_array[j]], ne)
                constraints.append(tmp)
                j += 1

    for i in range(3):
        for j in range(3):
            array = []
            for point in point_array:
                if (i*3 <= point[0] < (i+1)*3) and (j*3 <= point[1] < (j+1)*3):
                    array.append(point)
            for i in range(len(array)):
                j = i + 1
                while j < len(array):
                    tmp = Constraint([array[i], array[j]], ne)
                    constraints.append(tmp)
                    j += 1

    for i in range(9):
        row_array = np.where(np_grid[...,i] == 0)
        tuple_array = []
        for j in row_array[0]:
            tmp = (j, i)
            tuple_array.append(tmp)
        for i in range(len(tuple_array)):
            j = i + 1
            while j < len(tuple_array):
                tmp = Constraint([tuple_array[i], tuple_array[j]], ne)
                constraints.append(tmp)
                j += 1

    return CSP(domains, constraints)

csp = grid_to_csp(grid)
path = Searcher(Search_from_CSP(csp)).search()
if path is not None:
    print(path.end())
else:
    print("No solution")




