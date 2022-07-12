import numpy as np

import raw_unit_cells

class UnitCell:
    """ An class which represents a unit cell for a crystal lattice. 
    This contains plenty of static methods which will give you a certain type of lattice"""

    def __init__(self, points:np.array, side_length, x_size=None, y_size=None, z_size=None) -> None:
        self.points = points
        if x_size != None and y_size != None and z_size != None:
            self.size = (x_size, y_size, z_size)
        else:
            self.size = (side_length, side_length, side_length)

    def cube_from_function(unit_cell_function:function, side_length):
        """ This function will create a unit cell object from the 
        passed function, with the given side length. """
        return UnitCell(unit_cell_function(side_length))
    
    """ The following functions will return a UnitCell object of their repsective categories,
    just for convenience. """
    
    def simple_cubic(side_length):
        return UnitCell.cube_from_function(raw_unit_cells.simple_cubic)
    
    def body_centered_cubic(side_length):
        return UnitCell.cube_from_function(raw_unit_cells.body_centered_cubic)
    
    def face_centered_cubic(side_length):
        return UnitCell.cube_from_function(raw_unit_cells.face_centered_cubic)