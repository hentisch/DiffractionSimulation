import numpy as np

from raw_unit_cells import simple_cubic
from unit_cell import UnitCell

class CrystalLattice:
    """ A representation of the points in a crystal lattice.
    
    Attributes
    ----------
    all_points : np.array
        A 3d tensor of every point in the crystal lattice. The points are
        organized into groups of unit cells, with the points themselves  
        being simple x, y, z coordinates
    edge_points : np.array
        A 3d tensor of each "edge point" in the crystal lattice. The edge
        points will form the bounding box of each unit cell when they 
        are rendered.
    """

    def __init__(self, shape:tuple[int, int, int], unit_cell:UnitCell) -> None:
        """_summary_

        Parameters
        ----------
        shape : tuple of int (x, y, z)
            The shape that the crystal lattice should take. This is 
            described in unit cells.
        unit_cell : UnitCell
            The unit cell the lattice should be composed of. 

        See Also
        --------
        UnitCell : 
            The class used to represent a unit cell. 
        """        

        self.all_points = np.zeros((np.prod(shape), unit_cell.num_points, 3))
        self.edge_points = np.zeros((np.prod(shape), unit_cell.num_edge_points, 3))

        current_lattice_index = 0

        for x in range(1, shape[0]+1):
            for y in range(1, shape[1]+1):
                for z in range(1, shape[2]+1):
                    adjusted_unit_cell = unit_cell.get_shifted_points(x, y, z)
                    adjusted_edge_points = unit_cell.get_shifted_points(x, y, z, points="edge")
                    self.all_points[current_lattice_index] = adjusted_unit_cell
                    self.edge_points[current_lattice_index] = adjusted_edge_points
                    current_lattice_index += 1
        
    def get_raw_points(self):
        """Returns the lattice structure as a matrix of points

        Returns
        -------
        np.array:
            A 2d array representing a list of (x, y, z) points at which
            atoms should be drawn
        """        
        return self.all_points.reshape((self.all_points.shape[1]*self.all_points.shape[0], 3))