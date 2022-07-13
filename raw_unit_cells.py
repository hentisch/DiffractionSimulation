import numpy as np

from utils import midpoint_formula

""" This file contains several python functions to return a set of coordinates representing a single form of unit cell
for use in a crystal lattice. This is returned as a 2d numpy matrix, with each element contains the (x, y, z) points 
of each particular atom """

def simple_cubic(side_length:int):
    points = np.zeros((8, 3))

    point_counter = 0
    for x in (0, side_length):
        for y in (0, side_length):
            for z in (0, side_length):
                points[point_counter] = np.array([x, y, z])
                point_counter += 1

    return points

def body_centered_cubic(side_length:int):
    points = np.zeros((9, 3))

    points[:8] = simple_cubic(side_length)

    points[8] = np.array((side_length/2, side_length/2, side_length/2))

    return points

def get_xy_tuple(coordinates:np.array):
    """ Returns a tuple of the x and y coordinates of the passed 3d point """
    return (coordinates[0], coordinates[1])

def face_centered_cubic(side_length:int):
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