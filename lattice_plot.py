from crystal_latttice import CrystalLattice
from unit_cell import UnitCell

import numpy as np
from mayavi import mlab

def plot_lattice(lattice:CrystalLattice):
    points = lattice.get_raw_points()
    plot = mlab.points3d(points[:,0], points[:,1], points[:,2], scale_factor=0.1, resolution=20)
    mlab.show()

lattice = CrystalLattice((3, 3, 3), UnitCell.face_centered_cubic(1))
print(lattice.points)
plot_lattice(lattice)