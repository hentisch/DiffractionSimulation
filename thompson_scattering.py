from math import atan2, dist
import numpy as np
import scipy as sp
from scipy import integrate
import wave_conversions as wc

from utils import angle_between_lines, get_different_index, get_indices, graph_function, num_differences


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

def magnitude_by_space(atom_point:tuple, observation_point:tuple, wavevector_origin:tuple, observation_time:float, wave_amplitude:float, polarization_of_electric_field="z"):
    distance_from_scattering = dist(atom_point, observation_point)
    wavenumber = dist(wavevector_origin, atom_point) #magnitude of the wavevector
    
    """ The first thing we need to do (after finding the distance from scattering) is to simplify 
    our 3d coordinates to 2d coordinates on the plane of polarization and the direction of the wave """

    assert num_differences(atom_point, wavevector_origin) <= 1, "The plane of polarization and the wave direction should just be 2 of the 3 spacial dimensions"

    index_of_dimension = {'x':0, 'y':1, 'z':2}
    polarization_dim_index = index_of_dimension[polarization_of_electric_field]
    wave_dir_dim_ind = get_different_index(atom_point, wavevector_origin)
    assert polarization_dim_index != wave_dir_dim_ind, "The dimension of polarization and the dimension of the wave direction should be different"
    dimensions = sorted((polarization_dim_index, wave_dir_dim_ind)) #Because this is sorted, x will come before y, and so on

    atom_2d = get_indices(atom_point, dimensions)
    observation_2d = get_indices(observation_point, dimensions)
    incident_2d = get_indices(wavevector_origin, dimensions)

    incident_rad_vector = (incident_2d, atom_2d)
    observation_vector = (atom_2d, observation_2d)

    respective_angle = angle_between_lines(incident_rad_vector, observation_vector)

    return magnitude_by_angle(angle_of_observation=respective_angle, distance_from_scattering=distance_from_scattering, observation_time=observation_time,
    wavenumber=wavenumber, wave_amplitude=wave_amplitude)

if __name__ == "__main__":
    """ This script is not really meant to be ran on it's own - this bit of code just allows you to graph different variables of the function
    for the purpose of debugging.
    
    Note that this does require matplotlib to be installed, which is not listed in the requirements.txt file """
    
    function = lambda x: magnitude_by_angle(angle_of_observation = x, distance_from_scattering=5, observation_time=2, wavenumber=4, wave_amplitude=2)
    graph_function(function, min=0.1, max=100, num_samples=1000)
