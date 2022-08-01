import numpy as np
import math

from array_utils import exclude_indices, get_indices, fill_skipping
from utils import rgb_to_mayavi

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

index_by_dimension = {'x':0, 'y':1, 'z':2}
""" A dictionary giving the index of each dimension in a 3d coordinate
(x, y, z) """

def rotate_point(point:np.array, rotation_angle:float, center_point:np.array) -> tuple:
    """Returns a 'point', rotated 'rotation_angle' around 'center_point'.

    Parameters
    ----------
    point : np.array
        The point to rotate.
    rotation_angle : float
        The strength of the rotation. Note that this does not correspond 
        to a specific orientation, but rather a rotation to apply. (So, 
        rotating a point by 0.5pi 2 times is the same as rotating it by 
        pi).
    center_point : np.array
        The point to rotate 'point' around.

    Returns
    -------
    tuple
        The rotated point.

    Notes
    -----
    This function is an implementation of the equation:

    x1 = (x0 - xc)cos(θ) - (y0 - yc)sin(θ) + xc
    y1 = (x0 - xc)sin(θ) + (y0 - yc)cos(θ) + yc

    Where x1 and y1 are the coordinates of  the rotated point,
    theta is the angle of rotation, and xc and yc are the coordinates
    of the center point
    
    """    
    sin_angle = np.sin(rotation_angle)
    cos_angle = np.cos(rotation_angle)

    new_x = (point[0] - center_point[0]) * cos_angle - (point[1] - center_point[1]) * sin_angle + center_point[0]
    new_y = (point[1] - center_point[1]) * cos_angle + (point[0] - center_point[0]) * sin_angle + center_point[1]

    return new_x, new_y

def rotate_3d_point(point:np.array, angle:float, center_point:np.array, dimension:str):
    x, y = exclude_indices(point, (index_by_dimension[dimension],))
    c_x, c_y = exclude_indices(center_point, (index_by_dimension[dimension],))
    x_y = rotate_point((x, y), angle, (c_x, c_y))

    new_point = fill_skipping(point, x_y, (index_by_dimension[dimension],))

    return new_point

def rotate_3d_points(points:np.array, angle:float, dimension:str, center_point:np.array) -> np.array:
    """Returns a copy of 'points', rotated by 'angle' on the 'dimension'
    axis

    Parameters
    ----------
    points : np.array
        A matrix of points to be rotated. This should be a np.array of 
        (x, y, z) np.arrays.
    angle : float
        The magnitude of rotation. This needs to be a radian value.
        value.
    dimension : {"x", "y", "z"}
        The dimension on which 'points' will be rotated.
    center_point : np.array
        The point to rotate each point around

    Returns
    -------
    np.array
        a copy of 'points', rotated by 'angle' on the 'dimension' axis

    Notes
    -----
    This function is based on the following equation, which rotates a 2d
    point (x, y) in cartesian space:
    
    x' = x*cos(a) - y*sin(a)
    y' = y*cos(a) + x*sin(a)
    
    Where a is the magnitude of the rotation.
    """    

    """ First we need to convert the 3d points into the points relevant
    for the rotation around our desired axis. For this, we just remove
    the point which represents the passed dimension """

    rotated_points = np.zeros(points.shape)
    for i, point in enumerate(points):
        rotated_points[i] = rotate_3d_point(point, angle, center_point, dimension)
    
    return rotated_points

def rotate_by_euler(points:np.array, angles:tuple, center_point:tuple):

    new_points = np.copy(points)
    dimensions = ('x', 'y', 'z')
    for i, angle in enumerate(angles):
        new_points = rotate_3d_points(new_points, angle, dimensions[i], center_point)
    
    return new_points


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

def angle_between_3d_points(point_a:tuple, point_b:tuple):

    angle = np.zeros((1, 3))
    for i, axis in enumerate(point_a):
        angle[i] = angle_between_points(axis, point_b[i])
    
    return angle

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
    
"""     point_a_np = np.array(line_a)
    point_b_np = np.array(line_b)

    point_a_mag = math.dist(*line_a)
    point_b_mag = math.dist(*line_b)

    dot_product = np.dot(point_a_np[1], point_b_np[1])
    dot_product /= point_a_mag
    dot_product /= point_b_mag

    return np.arccos(dot_product) """

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

def get_3d_cos_wave(len:float, num_points:int, amplitude:float, wavelength:float):
    from mayavi import mlab
    x_points = np.linspace(0, len, num_points)
    all_points = np.zeros((num_points, 3))

    all_points[:,0] = np.full((num_points,), 0)
    all_points[:,1] = x_points
    all_points[:,2] = np.sin(((2*np.pi)/wavelength) * x_points) * amplitude

    rotated_points = rotate_3d_points(all_points, np.pi*0.5, 'y', (0, 0, 0))

    mlab.plot3d(all_points[:,0], all_points[:,1], all_points[:,2], color=rgb_to_mayavi(255, 255, 0))
    mlab.plot3d(rotated_points[:,0], rotated_points[:,1], rotated_points[:,2], color=rgb_to_mayavi(0, 0, 255))

    mlab.show() 