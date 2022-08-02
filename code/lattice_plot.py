from crystal_latttice import CrystalLattice
from unit_cell import UnitCell

import numpy as np
from mayavi import mlab

from utils import rgb_to_mayavi
from array_utils import num_differences

def plot_lattice(lattice:CrystalLattice):
    """Plots and displays a Mayavi plot of the passed crystal lattice

    Parameters
    ----------
    lattice : CrystalLattice
        The crystal lattice to make a plot of.
    
    Returns
    -------
    None
    """    
    points = lattice.get_raw_points()
    plot = mlab.points3d(points[:,0], points[:,1], points[:,2], scale_factor=0.1, resolution=20)
    points = np.array([[1, 2, 3], [1, 4, 3]]) 
    for unit_cell_edges in lattice.edge_points:
        plot_box(unit_cell_edges, (255, 0, 0))
    mlab.show()

def plot_box(corner_points:np.array, color:tuple) -> None:

    """ Plots a bounding box in the current Mayavi plot
    
    Parameters
    ---------- 
    corner_points:np.array
        The corner points making up the bounding box
    color:tuple of int (r, g, b)
        The desired color of the bounding box, represented as a 24 bit
        color, with each value ranging from 0 to 255
        
    Returns
    -------
    None
    
    Note
    ----
    This method is not very well optimized,
    <https://docs.enthought.com/mayavi/mayavi/auto/example_plotting_many_lines.html>
    would probably be a better way. """

    lines = set()
    for point in corner_points:
        for other_point in corner_points:
            if np.array_equiv(point, other_point):
                continue
            
            if num_differences(point, other_point) == 1:
                line = (tuple(point), tuple(other_point))
                if line not in lines:
                    lines.add(tuple(line))
                    line = np.array([point, other_point])
                    mlab.plot3d(line[:,0], line[:,1], line[:,2], tube_radius=None, color=rgb_to_mayavi(*color))

if __name__ == "__main__":
    lattice = CrystalLattice((1, 5, 1), UnitCell.face_centered_cubic(1))
    plot_lattice(lattice)