import enum
from math import dist
import numpy as np

import raw_unit_cells
from utils import flatten_matrix, shift_points, swap_indices
class UnitCell:
    """ An class which represents a unit cell for a crystal lattice. 
    This contains plenty of static methods which will give you a certain type of lattice"""

    def __init__(self, points:np.array, side_length, edge_points:np.array = None, x_size=None, y_size=None, z_size=None) -> None:
        self.all_points = points
        if x_size != None and y_size != None and z_size != None:
            self.size = (x_size, y_size, z_size)
        else:
            self.size = (side_length, side_length, side_length)

        self.x_size = self.size[0]
        self.y_size = self.size[1]
        self.z_size = self.size[2]

        self.num_points = len(points)

        self.edge_points = edge_points
        self.num_edge_points = len(edge_points)
        #These edge points will be the points through lines will be drawn

    def get_point_copy(self):
        return np.copy(self.all_points)

    def cube_from_function(unit_cell_function, side_length, edge_points=None):
        """ This function will create a unit cell object from the 
        passed function, with the given side length. """
        return UnitCell(unit_cell_function(side_length), side_length, edge_points=edge_points)

    """ The following functions will return a UnitCell object of their repsective categories,
    just for convenience. """

    def get_shifted_points(self, x_shift, y_shift, z_shift, size="unit_cells", points="all"):
        if size == "unit_cells":
            x_shift *= self.x_size
            y_shift *= self.y_size
            z_shift *= self.z_size
        
        if points == "all":
            shifted_points = np.copy(self.all_points)
        elif points == "edge":
            shifted_points = np.copy(self.edge_points_)
        
        shift_points(shifted_points, x_shift, y_shift, z_shift)
        return shifted_points

    def simple_cubic(side_length):
        return UnitCell.cube_from_function(raw_unit_cells.simple_cubic, side_length, edge_points=raw_unit_cells.simple_cubic(side_length))
    
    def body_centered_cubic(side_length):
        return UnitCell.cube_from_function(raw_unit_cells.body_centered_cubic, side_length, edge_points=raw_unit_cells.simple_cubic(side_length))
    
    def face_centered_cubic(side_length):
        return UnitCell.cube_from_function(raw_unit_cells.face_centered_cubic, side_length, edge_points=raw_unit_cells.simple_cubic(side_length))