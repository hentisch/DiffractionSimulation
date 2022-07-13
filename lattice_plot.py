from crystal_latttice import CrystalLattice
from unit_cell import UnitCell

import numpy as np
from mayavi import mlab

from utils import rgb_to_mayavi

def plot_lattice(lattice:CrystalLattice):
    points = lattice.get_raw_points()
    plot = mlab.points3d(points[:,0], points[:,1], points[:,2], scale_factor=0.1, resolution=20)
    points = np.array([[1, 2, 3], [1, 4, 3]]) 
    for unit_cell_edges in lattice.edge_points:
        plot_box(unit_cell_edges, (255, 0, 0))
    mlab.show()



def num_differences(arr_a:np.array, arr_b:np.array):
    assert arr_a.shape == arr_b.shape
    one_difference = 0
    for i, e in enumerate(arr_a):
        if e != arr_b[i]:
            one_difference += 1
    return one_difference


def plot_box(corner_points:np.array, color:tuple):
    """TODO, this method is really poorly optimized, 
    https://docs.enthought.com/mayavi/mayavi/auto/example_plotting_many_lines.html,
    would probably be the way to do this"""
    
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