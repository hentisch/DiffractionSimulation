from math import atan2, dist
import numpy as np
import scipy as sp
from scipy import integrate
import wave_conversions as wc

from utils import graph_function


def amplitude_of_atomic_diffraction(angle_of_observation:float, wavenumber:float, charge_distribution:float):
    np.seterr('raise')
    k = ( 4*np.pi * np.sin(angle_of_observation*2) ) / wc.convert(wavenumber, 'wavenumber', 'wavelength')
    func = lambda r: 4*np.pi*r*charge_distribution * (np.sin(k*r)/k*r)
    return integrate.quad(func, 0.1e-10, np.inf)

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
    
    thomson_scattering_length = sp.constants.value("classical electron radius")

    oscillatory_multiplicand = -thomson_scattering_length*wave_amplitude
    
    oscillatory_wave_value = np.exp(1j * (wavenumber*distance_from_scattering - wc.convert(wavenumber, "wavenumber", "angular_frequency")*observation_time) ) / distance_from_scattering

    complex_value = oscillatory_multiplicand * oscillatory_wave_value  * round(np.cos(angle_of_observation), 5)

    if returned_value == "complex":
        return complex_value
    elif returned_value == "real":
        return complex_value.real

def magnitude_by_space(point_of_atom:tuple, point_of_observation:tuple, observation_time:float, wavenumber:float, wave_amplitude:float, polarization_of_electric_field="z"):
    distance_from_scattering = dist(point_of_atom, point_of_observation)
    """ 
    Now, we need to get the angle of the observation point, in respect to the angle
    of the incident light radiation, on the plane of polarization. First, we can reduce 
    the 3d points to 2d points on the plane of polarization """

    index_of_dimension = {'x':0, 'y':1, 'z':2}

    atom_2d = (0, 0)
    observation_2d = (0, 0)

    assert polarization_of_electric_field == 'z', "Other directions of polarization have not yet been implemented"

    atom_2d = (point_of_atom[0], point_of_atom[2])
    observation_2d = (point_of_observation[0], point_of_observation[2])

    # Now, we need to find the angle of both points with respect to 0, 0
    atom_angle = atan2(*atom_2d)
    observation_angle = atan2(*observation_2d)

    respective_angle = abs(atom_angle - observation_angle)

    return magnitude_by_angle(angle_of_observation=respective_angle, distance_from_scattering=distance_from_scattering, observation_time=observation_time,
    wavenumber=wavenumber, wave_amplitude=wave_amplitude)

if __name__ == "__main__":
    """ This script is not really meant to be ran on it's own - this bit of code just allows you to graph different variables of the function
    for the purpose of debugging.
    
    Note that this does require matplotlib to be installed, which is not listed in the requirements.txt file """

    function = lambda x: magnitude_by_angle(angle_of_observation = x, distance_from_scattering=5, observation_time=2, wavenumber=4, wave_amplitude=2)
    graph_function(function, min=0.1, max=100, num_samples=1000)
