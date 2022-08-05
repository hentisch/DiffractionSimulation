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

from tqdm import tqdm

def get_2d_lattice_points(lattice:CrystalLattice, axis:str, slice_ind:int):
    raw_points = lattice.get_2d_slice(axis, slice_ind)

    return np.unique(raw_points, axis=0)

class DiffractionPlot:
    
    def __init__(self, interatomic_spacing) -> None:
        self.points = get_2d_lattice_points(CrystalLattice((3, 1, 1), UnitCell.simple_cubic(1)), 'y', 1)
        self.points /= interatomic_spacing

        self.interatomic_spacing = interatomic_spacing
    
    def plot_points(self):
        plt.scatter(self.points[:,0], self.points[:,1])
        plt.show()

    def calculate_diffraction(self, point_of_observation:tuple, angle_of_scattering:float):
        wavenumber = wc.convert(1, "wavelength", "wavenumber")
        phase_shift = wavenumber * np.sin(angle_of_scattering) * self.interatomic_spacing
        value_at_observation_point = 0j
        for point in self.points:
            atomic_distance = dist(point, point_of_observation)
            scattering_value = angle_free_atom_scattering(1, 0.1, 1, 'k', atomic_distance)
            if point[1] == 1:
                polar_scattering_value = list(cmath.polar(scattering_value))
                polar_scattering_value[1] += phase_shift
                scattering_value = cmath.rect(*polar_scattering_value)
            value_at_observation_point += scattering_value
        return value_at_observation_point

    def get_meshgrid(self, angle, min, max, step, x_shift, y_shift):
        x_points = np.arange(min, max, step)
        y_points = np.arange(min, max, step)
        xx, yy = np.meshgrid(x_points, y_points)
        
        xx += x_shift
        yy += y_shift

        phase_points = np.zeros(xx.shape)

        for y_i, row in enumerate(tqdm(phase_points)):
            for x_i, col in enumerate(phase_points):
                phase_points[y_i][x_i] = cmath.polar(self.calculate_diffraction((xx[y_i][x_i], yy[y_i][x_i]), angle))[1]
        
        plt.imshow(phase_points)
        plt.colorbar()
        plt.show()
        
        

if __name__ == "__main__":
    plot = DiffractionPlot(0.070710678118)
    # plot.plot_points()
    # print(plot.calculate_diffraction((10, 10), 0.785398))
    plot.get_meshgrid(1.9, -0.1, 0.1, 0.008, 0, 1e9) #0.