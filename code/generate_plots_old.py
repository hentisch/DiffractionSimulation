import os
from unit_cell import UnitCell
from lattice_plot import plot_lattice
from crystal_latttice import CrystalLattice
from wave_interference import *
import subprocess

import light_plot

from PIL import Image
from cairosvg import svg2png

from mayavi import mlab

from tqdm import tqdm

from matplotlib_scattering import get_thomson_scattering_slice

def pi_shifted_wave():
    w = ComponentWave(1, 0)
    a = ComponentWave(1, np.pi)
    w_a = w+a

    n = WavePlot([w, a], w_a, 2, 10000)

    n.plot("π Shifted Waves", "../materials/slideshow/plots/pi_shifted_matplotlib.png", size=(1920, 1440))

def in_phase_wave():
    w = ComponentWave(1, 0)
    a = ComponentWave(1, 0)
    w_a = w+a

    n = WavePlot([w, a], w_a, 2, 10000)
    n.plot("In Phase Waves", "../materials/slideshow/plots/in_phase_matplotlib.png", size=(1920, 1440), line_styles=['solid', 'dotted'])

def download_wave_interference_image():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/d/d5/Two_point_source_interference_Pattern_-_panoramio.jpg", "-O", "../materials/slideshow/images/pond_wave_interference.jpg"])

def download_phasor_gif():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/8/89/Unfasor.gif", "-O", "../materials/slideshow/images/phasor_fig.gif"])

def split_gif_into_frames(gif_path):

    slash_ind = gif_path.rfind('/')
    dot_ind = gif_path.rfind('.')

    folder_name = gif_path[slash_ind+1:dot_ind]
    folder_path = gif_path[:slash_ind] + "/" + folder_name

    try:
        os.mkdir(folder_path)
    except FileExistsError:
        pass

    gif = Image.open(gif_path)
    for frame_ind in range(0, gif.n_frames):
        gif.seek(frame_ind)
        gif.save(f"{folder_path}/frame-{frame_ind}.png")

def download_complex_plane_diagram():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/7/74/Illustration_of_a_complex_number.svg", "-O", "../materials/slideshow/images/complex_plane.svg"])

def download_complex_polar_diagram():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/7/71/Euler%27s_formula.svg", "-O", "../materials/slideshow/images/complex_polar_plane.svg"])

def download_light_spectrum():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/f/f1/EM_spectrum.svg", "-O", "../materials/slideshow/images/electromagnetic_spectrum.svg"])

def download_photo_51():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/en/b/b2/Photo_51_x-ray_diffraction_image.jpg", "-O", "../materials/slideshow/images/photo_51.png"])

def download_protien():
    subprocess.run(["wget", "https://upload.wikimedia.org/wikipedia/commons/6/60/Myoglobin.png", "-O", "../materials/slideshow/images/protein.png"])

def short_render_time():
    pi_shifted_wave()
    in_phase_wave()
    download_wave_interference_image()
    download_photo_51()
    download_protien()

    download_complex_plane_diagram()
    svg2png(url="../materials/slideshow/images/complex_plane.svg", write_to="../materials/slideshow/images/complex_plane.png")

    download_complex_polar_diagram()
    svg2png(url="../materials/slideshow/images/complex_polar_plane.svg", write_to="../materials/slideshow/images/complex_polar_plane.png")

    download_light_spectrum()
    svg2png(url="../materials/slideshow/images/electromagnetic_spectrum.svg", write_to="../materials/slideshow/images/electromagnetic_spectrum.png")

    download_phasor_gif()
    light_plot.main("../materials/slideshow/plots/light.png", (960, 540))

def get_figure_pan_gif(fig:mlab.figure, folder_path, num_frames:int):
    current_view = mlab.view(figure=fig)
    angles = np.linspace(0, 360, num_frames)

    for i in range(5):
        mlab.savefig('/tmp/img.png')
        
    for i, angle in enumerate(tqdm(angles)):
        mlab.view(azimuth=angle, elevation=current_view[1], distance=current_view[2], focalpoint=current_view[3])
        mlab.savefig(f'{folder_path}/frame-{i}.png', figure=fig, size=(800, 800))

def get_gif_of_lattice(lattice:CrystalLattice, folder_path:str):
    fig = plot_lattice(lattice)
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        pass

    get_figure_pan_gif(fig, folder_path, 100)

def get_scattering_plots():
    # get_thomson_scattering_slice(10, 100000, 'z', 0, (5, 5, 0), (5, -10, 0), "phase")
    # plt.savefig("../materials/slideshow/plots/phase_graphed.png")
    # plt.clf()

    get_thomson_scattering_slice(100, 100000, 'z', 0, (50, 50, 0), (50, -10, 0), value="amplitude")
    # plt.savefig("../materials/slideshow/plots/amplitude_graphed.png")
    plt.show()

def long_render_time():
    # get_gif_of_lattice(CrystalLattice((2, 2, 2), UnitCell.simple_cubic(1)), "../materials/slideshow/images/simple_cubic_lattice")
    # get_gif_of_lattice(CrystalLattice((2, 2, 2), UnitCell.body_centered_cubic(1)), "../materials/slideshow/images/body_centered_cubic_lattice")
    # get_gif_of_lattice(CrystalLattice((2, 2, 2,), UnitCell.face_centered_cubic(1)), "../materials/slideshow/images/face_centered_cubic_lattice")
    # get_scattering_plots()
    pass

def main():
    short_render_time()
    # long_render_time()?

if __name__ == "__main__":
    main()