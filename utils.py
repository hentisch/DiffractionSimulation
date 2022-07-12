import numpy as np

def midpoint_formula(point_a:tuple[int, int], point_b:tuple[int, int]) -> tuple[int, int]:
    a = (point_a[0] + point_a[1])
    b = (point_b[0] + point_b[1])
    return a/2, b/2

def shift_points(points:np.array, x_shift:float, y_shift:float, z_shift:float):
    points[:,0] += x_shift
    points[:,1] += y_shift
    points[:,2] += z_shift