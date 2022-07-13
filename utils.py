import itertools
import numpy as np
import copy

def midpoint_formula(point_a:tuple[int, int], point_b:tuple[int, int]) -> tuple[int, int]:
    a = (point_a[0] + point_a[1])
    b = (point_b[0] + point_b[1])
    return a/2, b/2

def shift_points(points:np.array, x_shift:float, y_shift:float, z_shift:float):
    points[:,0] += x_shift
    points[:,1] += y_shift
    points[:,2] += z_shift

def swap_indices(arr:np.array, index_a:int, index_b:int):
    temp = copy.copy(arr[index_a])
    arr[index_a] = arr[index_b]
    arr[index_b] = temp

def flatten_matrix(matrix:list):
    items = []
    for row in matrix:
        for element in row:
            items.append(element)
    return items