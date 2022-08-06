import matplotlib.pyplot as plt
import numpy as np
from array_utils import fill_skipping

from geometry_utils import index_by_dimension
from thomson_scattering import scattering_by_angle

from tqdm import tqdm

min1 = -0.4
max1 = 0.4
step = 0.0001
xPts = np.arange(min1, max1 + step, step)
yPts = np.arange(min1, max1 + step, step)
xx, yy = np.meshgrid(xPts, yPts)
radius = np.sqrt(xx ** 2 + yy ** 2)
angle = np.arctan(np.abs(yy / xx))

def get_amplitude_graph():
    amplitude, phase = scattering_by_angle(angle, radius, 0, 1, 1)
    plt.imshow(amplitude*radius, origin='lower')
    col_bar = plt.colorbar()
    col_bar.ax.set_ylabel("Amplitude of Scattered Light, Volts/Meter")
    plt.title("Amplitude of Light Scattered via Thomson Scattering", fontsize=9.5)
    plt.xlabel('X Coordinate, Nanometers')
    plt.ylabel('Y Coordinate, Nanometers')

def get_phase_graph():
    amplitude, phase = scattering_by_angle(angle, radius, 0, 0.1, 1)
    plt.imshow(np.mod(phase, np.pi*2), origin='lower')
    col_bar = plt.colorbar()
    col_bar.ax.set_ylabel("Phase of Scattered Light, Radians")
    plt.title('Phase of Light Scattered via Thomson Scattering', fontsize=12)
    plt.xlabel('X Coordinate, Nanometers')
    plt.ylabel('Y Coordinate, Nanometers')

if __name__ == "__main__":
    get_amplitude_graph()
    get_phase_graph()