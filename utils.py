import itertools
import numpy as np
import copy

def midpoint_formula(point_a:tuple[int, int], point_b:tuple[int, int]) -> tuple[int, int]:
    """ An implementation of the midpoint formula in 2d """
    a = (point_a[0] + point_a[1])
    b = (point_b[0] + point_b[1])
    return a/2, b/2

def shift_points(points:np.array, x_shift:float, y_shift:float, z_shift:float):
    """ Shift's the passed matrix of points in 3d space (x, y, z) by each numeric value"""
    points[:,0] += x_shift
    points[:,1] += y_shift
    points[:,2] += z_shift

def swap_indices(arr:np.array, index_a:int, index_b:int):
    """ Swaps the values of the two indices in a passed array """
    temp = copy.copy(arr[index_a])
    arr[index_a] = arr[index_b]
    arr[index_b] = temp

def flatten_matrix(matrix:list):
    """ Flattens a matrix into a single array. Note that this will
    not work for higher order tensors """
    items = []
    for row in matrix:
        for element in row:
            items.append(element)
    return items

def rgb_to_mayavi(r, g, b):
    """ Converts from a standard r,g,b color with each 
    color a single byte to an rgb color with each color a 
    float between 0 and 1 """
    return r/255, g/255, b/255