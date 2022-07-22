import numpy as np

from geometry_utils import midpoint_formula, get_xy_tuple

def simple_cubic(side_length:int) -> np.array:
    """Returns the points of a simple cubic unit cell, with the passed
    side length

    Parameters
    ----------
    side_length : int
        The side length of the unit cell

    Returns
    -------
    np.array of np.array
        A matrix of the points making up the unit cell
    """    
    points = np.zeros((8, 3))

    point_counter = 0
    for x in (0, side_length):
        for y in (0, side_length):
            for z in (0, side_length):
                points[point_counter] = np.array([x, y, z])
                point_counter += 1

    return points

def body_centered_cubic(side_length:int):
    """Returns the points of a body centered cubic unit cell, with the passed
    side length

    Parameters
    ----------
    side_length : int
        The side length of the unit cell

    Returns
    -------
    np.array of np.array
        A matrix of the points making up the unit cell
    """    
    points = np.zeros((9, 3))

    points[:8] = simple_cubic(side_length)

    points[8] = np.array((side_length/2, side_length/2, side_length/2))

    return points

def face_centered_cubic(side_length:int):
    """ This method will return the points (with their origin at 0,0) that make up
    a simple cubic unit cell"""

    points = np.zeros((14, 3))

    points[:8] = simple_cubic(side_length)

    points_arr_ind = 8

    #The square points represent the four corner points you would get from a square with the 
    #passed side-length

    square_points = ((0, 0), (side_length, 0), (side_length, side_length), (0, side_length))
    z_midpoint = side_length/2 #This represents the height of a point centered on the face
    #of a cube

    for i, point in enumerate(square_points):
        points[points_arr_ind] = np.array(midpoint_formula(get_xy_tuple(point), get_xy_tuple(square_points[(i + 1) % len(square_points)])) + (z_midpoint,))
        points_arr_ind += 1
    
    points[12] = (side_length/2, side_length/2, 0)
    points[13] = (side_length/2, side_length/2, 1)
    
    return points