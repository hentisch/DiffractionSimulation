import os
from wave_interference import *
import subprocess

import light_plot

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

def main():
    pi_shifted_wave()
    in_phase_wave()
    download_wave_interference_image()
    light_plot.main("../materials/slideshow/plots/light.png", (960, 540))

if __name__ == "__main__":
    main()
