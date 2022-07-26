import wave
import matplotlib.pyplot as plt
import numpy as np

import utils as u

import wave_conversions as wc

class Wave:
    def plot(self, num_samples, color, max, min=0):
        u.add_graph_to_plot(self, min, max, num_samples=num_samples, color=color)


class ComponentWave(Wave):
    def __init__(self, wavelength:float, added_phase:float) -> None:
        self.set_wavelength(wavelength)

        self.added_phase = added_phase
    
    def set_wavelength(self, wavelength:float):
        self.wavelength = wavelength

        self.wavenumber = wc.convert(wavelength, "wavelength", "wavenumber")
        self.angular_freq = wc.convert(wavelength, "wavelength", "angular_frequency")
        self.time_period = wc.convert(wavelength, "wavelength", "time_period")

    def __call__(self, time:float):
        return np.exp(1j * (self.wavenumber*time+self.added_phase - self.angular_freq*self.time_period))
    
    def __add__(self, other:Wave):
        return CompositeWave([self, other])

class CompositeWave(Wave):
    def __init__(self, waves:list[ComponentWave]) -> None:
        self.waves = list(waves)
    
    def __call__(self, time):
        value = 0
        for wave in self.waves:
            value += wave(time)
        return value
    
    def __add__(self, other:Wave):
        return CompositeWave(self.waves + [other])
    

def generate_wave_function(wavelength:float, added_phase:float):
    wavenumber = wc.convert(wavelength, "wavelength", "wavenumber")
    angular_freq = wc.convert(wavelength, "wavelength", "angular_frequency")
    time_period = wc.convert(wavelength, "wavelength", "time_period")

    return lambda t: np.exp(1j * (wavenumber*t+added_phase - angular_freq*time_period))

def plot_wave(wavelength:float, added_phase:float, color="black", min=0, max=5, num_samples=2000):
    wave_func = generate_wave_function(wavelength, added_phase)
    u.add_graph_to_plot(wave_func, min, max, num_samples=num_samples, color=color)


class WavePlot:

    colors = ["red", "green", "blue", "orange", "black"]

    def __init__(self, waves:list[ComponentWave], max:float, num_samples:float) -> None:
        for i, wave in enumerate(waves):
            wave.plot(num_samples, self.colors[i%len(self.colors)], max)
            

w = ComponentWave(1, 0)
a = ComponentWave(2, np.pi)
w_a = w+a

n = WavePlot([w, a, w_a], 5, 1000)

plt.show()