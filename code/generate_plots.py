import subprocess
import light_plot
import matplotlib_scattering as mls
from wave_interference import ComponentWave, WavePlot
import numpy as np
import matplotlib.pyplot as plt

from diffraction_plot import DiffractionPlot

import diffraction_plot
def download_photo_51():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/en/b/b2/Photo_51_x-ray_diffraction_image.jpg", "-O", "../materials/slideshow/images/photo_51.png"])
    subprocess.run(["convert", "../materials/slideshow/images/photo_51.png", "../materials/slideshow/images/photo_51.png"])

def download_protien():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/6/60/Myoglobin.png", "-O", "../materials/slideshow/images/protein.png"])

def download_wave_interference_image():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/d/d5/Two_point_source_interference_Pattern_-_panoramio.jpg", "-O", "../materials/slideshow/images/pond_wave_interference.jpg"])

def download_bragg_difraction_diagram():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Braggs_Law.svg/2560px-Braggs_Law.svg.png", "-O", "../materials/slideshow/images/braggs.png"])

def pi_shifted_wave():
    w = ComponentWave(1, 0)
    a = ComponentWave(1, np.pi)
    w_a = w+a

    n = WavePlot([w, a], w_a, 2, 10000)

    n.plot("π Shifted Waves", "../materials/slideshow/plots/pi_shifted_matplotlib.png", size=(1920, 1440), line_styles=['dotted', 'dotted', 'solid'])

def in_phase_wave():
    w = ComponentWave(1, 0)
    a = ComponentWave(1, 0.5)
    w_a = w+a

    n = WavePlot([w, a], w_a, 2, 10000)
    n.plot("In Phase Waves", "../materials/slideshow/plots/in_phase_matplotlib.png", size=(1920, 1440), line_styles=['dotted', 'dotted', 'solid'])

def lattice_from_diffraction():
    plot = DiffractionPlot(0.070710678118)
    plot.plot_points()
    plt.title("Points used in diffraction simulations")
    plt.xlabel("Point on X-Axis (Nanometers)")
    plt.ylabel("Point on Y-Axis (Nanometers)")
    plt.savefig("../materials/slideshow/plots/lattice_simulation_points.png")

def slideshow():
    download_photo_51()
    download_protien()
    download_wave_interference_image()
    download_bragg_difraction_diagram()

    pi_shifted_wave()
    in_phase_wave()

    plt.clf()

    mls.get_amplitude_graph()
    plt.savefig("../materials/slideshow/plots/thomson_amplitude.png", dpi=300)

    plt.clf()

    mls.get_phase_graph()
    plt.savefig("../materials/slideshow/plots/phase.png", dpi=300, pad_inches=1)

    light_plot.main("../materials/slideshow/plots/light.png", (960, 540))

def slideshow_intense():
    plot = diffraction_plot.DiffractionPlot(0.070710678118)
    plot.get_meshgrid(0.785398, 0.1, -5e8, 5e8, 1e7, 1e9, 1e9)
    plt.savefig("../materials/slideshow/images/constructive_atoms.png", dpi=300)

    plot = diffraction_plot.DiffractionPlot(0.070710678118)
    plot.get_meshgrid(0.785398, 1, -5e8, 5e8, 1e7, 1e9, 1e9)
    plt.savefig("../materials/slideshow/images/nonconstructive_atoms_wavelength.png", dpi=300)

    plot = diffraction_plot.DiffractionPlot(0.070710678118)
    plot.get_meshgrid(0.785398, 0.1, -5e8, 5e8, 1e7, 4e9, 4e9)
    plt.savefig("../materials/slideshow/images/nonconstructive_viewpoint_4cm.png", dpi=300)

    plot = diffraction_plot.DiffractionPlot(0.070710678118)
    plot.get_meshgrid(0.785398, 0.1, -5e5, 5e5, 1e3, 1e9, 1e9)
    plt.savefig("../materials/slideshow/images/nonconstructive_sizing.png", dpi=300)
if __name__ == "__main__":
    slideshow_intense()
