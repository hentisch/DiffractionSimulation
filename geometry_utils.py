import numpy as np
import math

def midpoint_formula(point_a:'tuple[int, int]', point_b:'tuple[int, int]') -> 'tuple[int, int]':
    """ An implementation of the midpoint formula in 2d.
    
    Parameters
    ---------- 
    point_a, point_b: tuple of int (x, y)
        The two 2d points to find the midpoint between.
        
    Returns
    -------
    tuple of int (x, y)
        The midpoint between the two points.
    """
    
    a = (point_a[0] + point_a[1])
    b = (point_b[0] + point_b[1])
    return a/2, b/2

def shift_points(points:np.array, x_shift:int, y_shift:float, z_shift:float) -> None:
    """ Shifts a numpy matrix of 3d points in space.

    Parameters
    ----------
    x_shift : float
        The number of units to shift in the x dimension.
    y_shift : float
        The number of units to shift in the y dimension.
    z_shift : float
        The number of units to shift in the z dimension.
    
    Returns
    -------
    None
    """
    points[:,0] += x_shift
    points[:,1] += y_shift
    points[:,2] += z_shift

def angle_between_points(point_a:tuple, point_b:tuple):
    """Returns the angle between two points in cartesian space

    Parameters
    ----------
    point_a, point_b : tuple of int (x, y)
        The points to find the angle between.

    Returns
    -------
    float
        The angle between 'point_a', and 'point_b', in radians.
    """    
    
    adjacent_len = point_b[0] - point_a[0]
    hypotenuse_len = math.dist(point_a, point_b)
    return np.arccos(adjacent_len/hypotenuse_len)

def get_slope(line:'tuple(tuple, tuple)') -> float:
    """ Return the slope of a line

    Parameters
    ----------
    line : tuple matrix of int ((x, y), (x, y))
        A line to compute the slope of.

    Returns
    -------
    float
        The slope of the passed line.
    """    

    rise = line[1][1] - line[0][1]
    run = line[1][0] - line[0][0]
    if run == 0:
        return np.inf
    
    return rise/run

def angle_between_lines(line_a, line_b):
    """Returns the angle between two lines

    Parameters
    ----------
    line_a, line_b : tuple matrix of int ((x, y), (x, y))
        The lines to find the angle between.
    
    Returns
    -------
    float
        The angle, in radians, between the two lines.
    """    
    difference_in_angles = np.arctan(get_slope(line_a) - get_slope(line_b))
    return np.pi - abs(difference_in_angles)

def get_xy_tuple(coordinates:np.array) -> tuple:
    """Return the x, y coordinates of a np.array of x, y, and z points

    Parameters
    ----------
    coordinates : np.array
        The 3d coordinates to get the x, y coordinates from

    Returns
    -------
    tuple of float (x, y)
        The x, y coordinates of the passed 3d coordinates
    """    
    return (coordinates[0], coordinates[1])