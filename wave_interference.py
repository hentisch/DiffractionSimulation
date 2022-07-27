import wave
import matplotlib.pyplot as plt
import numpy as np

import utils as u

import wave_conversions as wc

class Wave:
    def plot(self, num_samples, color, max, min=0):
        u.add_graph_to_plot(self, min, max, num_samples=num_samples, color=color)
    
    def get_y_values(self, x_values:np.array):
        x_values = np.zeros(x_values.shape)

        return [self(x) for x in x_values]


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

    def __init__(self, component_waves:list[ComponentWave], composite_wave:CompositeWave, max:float, num_samples:float) -> None:
        self.component_waves = component_waves
        self.composite_wave = composite_wave
        self.all_waves = component_waves + [composite_wave]

        self.max = max
        self.num_samples = num_samples

        self.wave_lines = []
    
    def plot(self):
        fig, ax = plt.subplots()
        for i, wave in enumerate(self.all_waves):
            x_values = np.linspace(0, self.max, self.num_samples)
            y_values = [wave(x) for x in x_values]
            self.wave_lines.append(plt.plot(x_values, y_values, color=self.colors[i%len(self.colors)]))

        plt.subplots_adjust(left=0.5, bottom=0.5)

        # wave_a_shift = plt.axes([0.1, 0.1, 0.03, 1])
        wave_a_shift = plt.axes([0.25, 0.2, 0.65, 0.03])
        wave_a_shift_slider = plt.Slider(
            ax=wave_a_shift, 
            label="Wave A Phase shift",
            valmin=0,
            valmax=2,
            valinit=0
        )

        wave_a_wavelength = plt.axes([0.25, 0.1, 0.65, 0.03])
        wave_a_wavelength_slider = plt.Slider(
            ax=wave_a_wavelength,
            label="Wave A Wavelength",
            valmin=0,
            valmax=10,
            valinit=0
        )
        wave_a_wavelength_slider.on_changed(lambda x: self.update_wavelength(self.component_waves[0], wave_a_shift_slider.val))
        plt.show()

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
        

w = ComponentWave(1, 0)
a = ComponentWave(2, np.pi)
w_a = w+a

n = WavePlot([w, a], w_a, 10, 1000)

n.plot()