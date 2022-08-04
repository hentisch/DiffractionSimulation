from crystal_latttice import CrystalLattice
from unit_cell import UnitCell

import matplotlib.pyplot as plt

def plot_2d_lattice(lattice:CrystalLattice, axis:str, slice_ind:int):
    points = lattice.get_2d_slice(axis, slice_ind)

    plt.scatter(points[:,0], points[:,1])
    plt.show()

if __name__ == "__main__":
    plot_2d_lattice(CrystalLattice((4, 1, 3), UnitCell.simple_cubic(1)), 'y', 1)