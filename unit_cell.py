import enum
from math import dist
import numpy as np

import raw_unit_cells
from geometry_utils import shift_points

class UnitCell:
    """ A representation of the points in a unit cell. 
    
    Attributes
    ----------
    all_points : np.array
        A matrix of each point in the unit cell. Each point is represented
        as a numpy array of x, y, and z.
    num_points : int
        The number of total points in the unit cell.
    edge_points: np.array
        The "edge points" of the unit cell. These points will be drawn as
        a bounding box, helping to visually separate different unit cells
        in a larger plot.
    num_edge_points : int
        The number of total edge points
    size : tuple of float (x, y, z)
        The size of the unit cell, represented by the same units 
        as the coordinates.
    x_size, y_size, z_size : float
        The dimensions represented in 'size', unpacked for convenient 
        access
    """    

    def __init__(self, points:np.array, side_length:float = None, edge_points:np.array = None,  x_size:float=None, y_size:float=None, z_size:float=None) -> None:
        """ A constructor for the UnitCell class

        Parameters
        ----------
        points : np.array
            Every point in the unit cell. Represented as a matrix of 
            (x, y, z) numpy arrays.
        edge_points : np.array, optional
            The edge points of the unit cell. These will be drawn as a
            bounding box, helping to make different unit cells visually 
            distinct. 
        side_length : float, optional
            The side length of a unit cell. This can be used when the unit
            cell is a cube, and the x, y, and z size dimensions are the 
            same. If a value is not given, one must pass the 'x_size',
            'y_size' and 'z_size'
        x_size, y_size, z_size: float, optional
            The size of the unit cell in the same units as the points. If
            a value is not given to all three parameters, then a value
            must be given for the 'side_length' 

        Raises
        ------
        ValueError
            If neither a side_length or a specific x, y, and z size is 
            passed.
        """        
        self.all_points = points

        self.num_points = len(points)

        self.edge_points = edge_points
        self.num_edge_points = len(edge_points)

        if x_size != None and y_size != None and z_size != None:
            self.size = (x_size, y_size, z_size)
        else:
            if side_length == None:
                raise ValueError("You must either pass the x, y, and z size of the unit cell, or a side length")
        
            self.size = (side_length, side_length, side_length)

        self.x_size, self.y_size, self.z_size = self.size

    def get_point_copy(self):
        """ Returns a copy of the 'all_points' attribute.

        Returns
        -------
        np.array :
            A copy of the 'all_points' attribute.
        """        

        return np.copy(self.all_points)

    def get_shifted_points(self, x_shift, y_shift, z_shift, shift_unit="unit_cells", points="all"):
        """Returns a copy of the unit cell's points, shifted in space.

        Parameters
        ----------
        x_shift, y_shift, z_shift : float
            The magnitude of the shift.
        shift_unit : [{"unit_cells", "raw_units"}, optional]
            The unit by which to describe the magnitude of the point 
            shifting.
        points : [{"all", "edge"}, optional]
            Whether to return a copy of all shifted points, or just the
            edge points.
        
        Returns
        -------
        np.array
            A copy of the entire unit cell's points with the described 
            shift
        """        
        
        if shift_unit == "unit_cells":
            x_shift *= self.x_size
            y_shift *= self.y_size
            z_shift *= self.z_size
        elif shift_unit != "raw_units":
            raise ValueError("shift_unit must be either unit_cells, or raw_units")

        if points == "all":
            shifted_points = np.copy(self.all_points)
        elif points == "edge":
            shifted_points = np.copy(self.edge_points)
        
        shift_points(shifted_points, x_shift, y_shift, z_shift)
        return shifted_points

    def simple_cubic(side_length:float) -> 'UnitCell':
        """Returns a UnitCell object with the points of a simple cubic

        Parameters
        ----------
        side_length : float
            The side length of the unit cell
        
        Returns
        -------
        UnitCell : 
            A unit cell with a simple cubic structure and a side_length 
            of 'side_length'
        """        
        return UnitCell(raw_unit_cells.simple_cubic(), side_length=side_length, edge_points=raw_unit_cells.simple_cubic(side_length))
    
    def body_centered_cubic(side_length:float) -> 'UnitCell':
        """Returns a UnitCell object with the points of a body centered cubic

        Parameters
        ----------
        side_length : float
            The side length of the unit cell
        
        Returns
        -------
        UnitCell : 
            A unit cell with a body centered cubic structure and a side
            length of 'side_length'
        """        
        return UnitCell(raw_unit_cells.body_centered_cubic(), side_length=side_length, edge_points=raw_unit_cells.simple_cubic(side_length))
    
    def face_centered_cubic(side_length:float) -> 'UnitCell':
        """Returns a UnitCell object with the points of a face centered cubic

        Parameters
        ----------
        side_length : float
            The side length of the unit cell
        
        Returns
        -------
        UnitCell : 
            A unit cell with a face centered cubic structure and a side
            length of 'side_length'
        """        
        return UnitCell(raw_unit_cells.face_centered_cubic(), side_length=side_length, edge_points=raw_unit_cells.simple_cubic(side_length))