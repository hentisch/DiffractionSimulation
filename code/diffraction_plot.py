import numpy as np
from scipy import integrate

from geometry_utils import angle_between_points, get_2d_points, get_3d_cos_wave, get_3d_cos_wave_between_points, rotate_2d_points
from math import dist
from crystal_latttice import CrystalLattice
from unit_cell import UnitCell

import matplotlib.pyplot as plt

from thomson_scattering import angle_free_atom_scattering
import wave_conversions as wc

import cmath

def get_2d_lattice_points(lattice:CrystalLattice, axis:str, slice_ind:int):
    raw_points = lattice.get_2d_slice(axis, slice_ind)

    return np.unique(raw_points, axis=0)

class DiffractionPlot:
    
    def __init__(self) -> None:
        self.points = get_2d_lattice_points(CrystalLattice((3, 1, 1), UnitCell.simple_cubic(1)), 'y', 1)
        self.points /= 0.707
    
    def plot_points(self):
        plt.scatter(self.points[:,0], self.points[:,1])
        plt.show()
    
    def calculate_diffraction(self, point_of_observation:tuple, angle_of_scattering:float):
        wavenumber = wc.convert(1, "wavelength", "wavenumber")
        phase_shift = wavenumber * np.sin(angle_of_scattering)
        value_at_observation_point = 0j
        for point in self.points:
            atomic_distance = dist(point, point_of_observation)
            scattering_value = angle_free_atom_scattering(1, 1, 1, 'k', atomic_distance)
            if point[1] == 1:
                polar_scattering_value = list(cmath.polar(scattering_value))
                polar_scattering_value[1] += phase_shift
                scattering_value = cmath.rect(*polar_scattering_value)
            value_at_observation_point += scattering_value
        return value_at_observation_point

if __name__ == "__main__":
    plot = DiffractionPlot()
    print(plot.calculate_diffraction((10, 10), 0.785398))
    #785398
    plot.plot_points()