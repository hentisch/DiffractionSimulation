import numpy as np

""" This file contains several python functions to return a set of coordinates represnting a single form of unit cell
for use in a crystal lattice. This is returned as a 2d numpy matrix, with each element containg the (x, y, z) points 
of each particular atom """

def simple_cubic(side_length):
    points = np.zeros((8, 3))

    point_counter = 0
    for x in (0, side_length):
        for y in (0, side_length):
            for z in (0, side_length):
                print(x, y, z)
                points[point_counter] = np.array([x, y, z])
                point_counter += 1

    return points