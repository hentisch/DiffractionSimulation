import os
from wave_interference import *
import subprocess

import light_plot

from PIL import Image
from cairosvg import svg2png

def pi_shifted_wave():
    w = ComponentWave(1, 0)
    a = ComponentWave(1, np.pi)
    w_a = w+a

    n = WavePlot([w, a], w_a, 2, 10000)

    n.plot("π Shifted Waves", "../materials/slideshow/plots/pi_shifted_matplotlib.png", 7/9)

def in_phase_wave():
    w = ComponentWave(1, 0)
    a = ComponentWave(1, 0)
    w_a = w+a

    n = WavePlot([w, a], w_a, 2, 10000)
    n.plot("In Phase Waves", "../materials/slideshow/plots/in_phase_matplotlib.png", 7/9)

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

def main():
    pi_shifted_wave()
    in_phase_wave()
    download_wave_interference_image()

    download_complex_plane_diagram()
    svg2png(url="../materials/slideshow/images/complex_plane.svg", write_to="../materials/slideshow/images/complex_plane.png")

    download_complex_polar_diagram()
    svg2png(url="../materials/slideshow/images/complex_polar_plane.svg", write_to="../materials/slideshow/images/complex_polar_plane.png")

    download_phasor_gif()
    light_plot.main("../materials/slideshow/plots/light.png", (960, 540))

    
if __name__ == "__main__":
    main()