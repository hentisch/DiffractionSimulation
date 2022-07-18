import numpy as np
from scipy import constants
import wave_conversions as wc

from utils import graph_function

def magnitude_by_angle(angle_of_observation:float, distance_from_scattering:float, observation_time:float, wavenumber:float, wave_amplitude:float, returned_value="real"):
    """This function will find the strength of Thompson scattering from a single electron,
    based on the point of observation.

    Units: 
        Angle of observation: Radian angle on the plane of polarization
        Distance from scattering: Meters
        Observation time: Seconds
        Wavenumber: Cycles/Meter 
        Wave Amplitude: Volts/Meter
        
        Returns: Volts/Meter"""
    
    thomson_scattering_length = constants.value("classical electron radius")

    oscillatory_multiplicand = -thomson_scattering_length*wave_amplitude
    
    oscillatory_wave_value = np.exp(1j * (wavenumber*distance_from_scattering - wc.convert(wavenumber, "wavenumber", "angular_frequency")*observation_time) ) / distance_from_scattering

    complex_value = oscillatory_multiplicand * oscillatory_wave_value  * round(np.cos(angle_of_observation), 5)

    if returned_value == "complex":
        return complex_value
    elif returned_value == "real":
        return complex_value.real

if __name__ == "__main__":
    """ This script is not really meant to be ran on it's own - this bit of code just allows you to graph different variables of the function
    for the purpose of debugging.
    
    Note that this does require matplotlib to be installed, which is not listed in the requirements.txt file """

    function = lambda x: magnitude_by_angle(angle_of_observation = x, distance_from_scattering=5, observation_time=2, wavenumber=4, wave_amplitude=2)
    graph_function(function, min=0.1, max=100, num_samples=1000)