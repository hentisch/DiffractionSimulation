from statistics import mean
import wave
import matplotlib.pyplot as plt
import numpy as np

import utils as u

import wave_conversions as wc

import string

class Wave:

    def plot(self, num_samples, color, max, min=0):
        u.add_graph_to_plot(self, min, max, num_samples=num_samples, color=color)
    
    def get_y_values(self, x_values:np.array):
        x_values = np.zeros(x_values.shape)

        return [self(x) for x in x_values]

    def set_wavelength(self, wavelength:float):
        self.wavelength = wavelength

        self.wavenumber = wc.convert(wavelength, "wavelength", "wavenumber")
        self.angular_freq = wc.convert(wavelength, "wavelength", "angular_frequency")
        self.time_period = wc.convert(wavelength, "wavelength", "time_period")

class ComponentWave(Wave):
    def __init__(self, wavelength:float, added_phase:float, amplitude:float=1) -> None:
        self.set_wavelength(wavelength)

        self.added_phase = added_phase
        
        self.amplitude = 1

    def __call__(self, time:float):
        return np.cos(self.wavenumber*time+self.added_phase - self.angular_freq*self.time_period) * self.amplitude
    
    def __add__(self, other:Wave):
        return CompositeWave([self, other])

class CompositeWave(Wave):
    def __init__(self, waves:list[ComponentWave]) -> None:
        self.waves = list(waves)
        self.wavelength = mean([wave.wavelength for wave in self.waves])
        self.amplitude = mean([wave.amplitude for wave in self.waves])
    
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

    def __init__(self, component_waves:list[ComponentWave], composite_wave:CompositeWave, max:float, num_samples:float) -> None:
        self.component_waves = component_waves
        self.composite_wave = composite_wave
        self.all_waves = component_waves + [composite_wave]

        self.max = max
        self.num_samples = num_samples

        self.wave_lines = []
    
    def plot(self, title:str="Wave Interference", filepath:str=None, aspect_ratio:float=4/3, inches_per_unit:float=1):
        fig, ax = plt.subplots()

        x_left, x_right = ax.get_xlim()
        y_low, y_high = ax.get_ylim()
        ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*aspect_ratio)

        for i, wave in enumerate(self.all_waves):
            x_values = np.linspace(0, self.max, self.num_samples)
            y_values = [wave(x) for x in x_values]
            if i == len(self.all_waves)-1: #This is true when we are on the composite wave:
                # label = f"Composite Wave, Wavelength - {wave.wavelength}, Amplitude - {wave.amplitude}"
                label = "Composite Wave"
            else:
                label = f"Wavelength - {wave.wavelength}, Amplitude - {wave.amplitude}" 
            self.wave_lines.append(plt.plot(x_values, y_values, color=self.colors[i%len(self.colors)], label=label))

        plt.legend(loc="upper left")

        plt.xlabel("Time")
        plt.ylabel("Field Strength")
        plt.title(title)

        if filepath == None:
            plt.show()
        else:
            plt.savefig(filepath, dpi=300)


    def update_wavelength(self, wave, new_wavelength:float, fig):
        wave.wavelength  = new_wavelength
        self.update_plot(fig)

    def update_shift(self, wave, shift:float, fig):
        wave.added_phase = shift
        self.update_plot(fig)

    def update_plot(self, fig):
        x_values = np.linspace(0, self.max, self.num_samples)
        for i, line in enumerate(self.wave_lines):
            line.set_ydata(self.all_waves[i].get_y_values(x_values))
        fig.canvas.draw_idle()