from math import dist
import numpy as np
import copy

def midpoint_formula(point_a:'tuple[int, int]', point_b:'tuple[int, int]') -> 'tuple[int, int]':
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

def graph_function(func, min, max, num_samples) -> None:
    import matplotlib.pyplot as plt

    x_values = np.linspace(min, max, num=num_samples)

    y_values = np.zeros(num_samples)

    for i, x in enumerate(x_values):
        y_values[i] = func(x)
        # print(func(x))
    
    plt.plot(x_values, y_values)

    plt.show()

def angle_between_points(point_a:tuple, point_b:tuple):
    """ This function will return the angle between
    two points on the cartesian plane """

    adjacent_len = point_b[0] - point_a[0]
    hypotenuse_len = dist(point_a, point_b)
    return np.arccos(adjacent_len/hypotenuse_len)


def num_differences(arr_a, arr_b):
    """ This function will return the number of values
    which are different between two equally sized arrays """

    assert len(arr_a) == len(arr_b), "Both arrays need to be the same shape"

    one_difference = 0
    for i, e in enumerate(arr_a):
        if e != arr_b[i]:
            one_difference += 1
        return one_difference

def get_different_index(arr_a, arr_b, check_single_difference=False) -> int:
    if check_single_difference:
        num_diff = num_differences(arr_a, arr_b)
        assert num_diff == 1, f"There are a total of {num_diff} indices different between the two arrays, there should only be one"
        return
    
    for i, e in arr_a:
        if arr_b[i] != e:
            return i

def get_indices_tuple(arr, indices:list) -> list:
    elements = []
    for index in indices:
        elements.append(arr[index])
    return elements