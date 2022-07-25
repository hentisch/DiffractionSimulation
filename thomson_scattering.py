from math import atan2, dist
from random import random
import numpy as np
import scipy as sp
from scipy import integrate
import wave_conversions as wc

from geometry_utils import angle_between_lines, index_by_dimension
from array_utils import get_different_index, get_indices, num_differences
from utils import graph_function


def amplitude_of_atomic_diffraction(angle_of_observation:float, wavenumber:float, charge_distribution:float):
    np.seterr('raise')
    k = ( 4*np.pi * np.sin(angle_of_observation*2) ) / wc.convert(wavenumber, 'wavenumber', 'wavelength')
    func = lambda r: 4*np.pi*r*charge_distribution * (np.sin(k*r)/k*r)
    return integrate.quad(func, 0.1e-10, np.inf)

#TODO, make this method return phase and amplitude
def scattering_by_angle(angle_of_observation:float, distance_from_scattering:float, observation_time:float, wavelength:float, wave_amplitude:float, returned_value="amplitude") -> float:
    """ Finds the amplitude of Thomson scattering from a certain
    point in space. This point is described in terms of the 
    'angle_of_observation', and 'distance_from_scattering'.
    
    
    Parameters
    ---------- 
    angle_of_observation : float
        Angle of the point of observation in respect to the incident 
        light, on the plane of scattering. This should be described in
        radians.
    distance_from_scattering : float
        Distance between the point of scattering and the point of 
        observation. This should be described in meters.
    observation_time : float
        The time at which the scattered light is observed. This should
        be described in seconds.
    wavelength : float
        The wavelength of the incident light. This should be described in 
        meters.
    wave_amplitude : float 
        The strength of the incident electric field. This should be 
        described in volts/meter.
    returned_value : str, [{"amplitude", "phase", "both"}, optional]
        The part of the scattered wave to be returned
    
    Returns
    -------
    amplitude : float
        The amplitude of the scattered electric field at the passed 
        point. This is described in volts/meter (assuming you passed the
        right units).
    phase: float
        The phase of the scattered electric field at the passed point.
        This is described in radians (assuming you passed the right
        units)
    both : tuple of float
        A tuple of the amplitude and phase of the wave at the described
        point (amplitude, phase)
    
    
    See Also
    --------
    amplitude_by_space : 
        A wrapper around this function, which uses points in 3d space
        rather than the 'angle_of_observation' and 
        'distance_from-scattering'. 
    """
    
    thomson_scattering_length = sp.constants.value("classical electron radius")

    oscillatory_multiplicand = -thomson_scattering_length*wave_amplitude
    
    oscillatory_wave_value = np.exp(1j * (wc.convert(wavelength, "wavelength", "wavenumber")*distance_from_scattering - wc.convert(wavelength, "wavelength", "angular_frequency")*observation_time) ) / distance_from_scattering

    complex_value = oscillatory_multiplicand * oscillatory_wave_value  * round(np.cos(angle_of_observation), 5)

    amplitude = abs(complex_value)
    phase = np.arctan(complex_value.real/complex_value.imag)

    if returned_value == "amplitude":
        return amplitude
    elif returned_value == "phase":
        return phase
    elif returned_value == "both":
        return (amplitude, phase)
    else:
        raise ValueError(f"Could not interpret value {returned_value}, use either \"amplitude\" or \"phase\"")

def scattering_by_space(scattering_point:tuple, observation_point:tuple, wavevector_origin:tuple, observation_time:float, wave_amplitude:float, polarization_of_electric_field="z", returned_value="amplitude") -> float:
    """ Finds the amplitude of Thomson scattering based on several points
    in 3d space.
    
    Parameters
    ----------
    scattering_point : tuple of int (x, y, z)
        The point at which the incident light is scattered.
    observation_point: tuple of int (x, y, z)
        The point at which the scattering of the incident light is 
        observed.
    wavevector_origin : tuple of int (x, y, z)
        The initial point of the wavevector of the incident light. The 
        terminal point is assumed to be the 'scattering_point'.
    observation_time : float
        The time at which the scattered light is observed. This should
        be described in seconds. 
    wave_amplitude : float
        The amplitude of incident light's electric field. This should
        be described in volts/meter.
    polarization_of_electric_field : str, [{"z", "x", "y"}, optional]
        The dimension in which the electric field should be polarized. 
    returned_value : str, [{"amplitude", "phase", "both"}, optional]
        The part of the scattered wave to be returned.
    
    Returns
    -------
    amplitude : float
        The amplitude of the scattered electric field at the passed 
        point. This is described in volts/meter (assuming you passed the
        right units).
    phase: float
        The phase of the scattered electric field at the passed point.
        This is described in radians (assuming you passed the right
        units)
    both : tuple of float
        A tuple of the amplitude and phase of the wave at the described
        point (amplitude, phase)
    
    See Also
    --------
    scattering_by_angle : 
        The function this function wraps. Computes Thomson 
        scattering based on the distance from the source of scattering,
        and the angle of the observation point in respect to the 
        incident light.
    """

    distance_from_scattering = dist(scattering_point, observation_point)
    wavenumber = dist(wavevector_origin, scattering_point) #magnitude of the wavevector
    wavelength = wc.convert(wavenumber, "wavenumber", "wavelength")
    
    """ The first thing we need to do (after finding the distance from scattering) is to simplify 
    our 3d coordinates to 2d coordinates on the plane of polarization and the direction of the wave """

    assert num_differences(scattering_point, wavevector_origin) <= 1, "The plane of polarization and the wave direction should just be 2 of the 3 spacial dimensions"

    polarization_dim_index = index_by_dimension[polarization_of_electric_field]
    wave_dir_dim_ind = get_different_index(scattering_point, wavevector_origin)
    assert polarization_dim_index != wave_dir_dim_ind, "The dimension of polarization and the dimension of the wave direction should be different"
    dimensions = sorted((polarization_dim_index, wave_dir_dim_ind)) #Because this is sorted, x will come before y, and so on

    atom_2d = get_indices(scattering_point, dimensions)
    observation_2d = get_indices(observation_point, dimensions)
    incident_2d = get_indices(wavevector_origin, dimensions)

    incident_rad_vector = (incident_2d, atom_2d)
    observation_vector = (atom_2d, observation_2d)

    respective_angle = angle_between_lines(incident_rad_vector, observation_vector)

    return scattering_by_angle(angle_of_observation=respective_angle, distance_from_scattering=distance_from_scattering, observation_time=observation_time,
    wavelength=wavelength, wave_amplitude=wave_amplitude, returned_value=returned_value)

if __name__ == "__main__":
    """ This script is not really meant to be ran on it's own - this bit of code just allows you to graph different variables of the function
    for the purpose of debugging.
    
    Note that this does require matplotlib to be installed, which is not listed in the requirements.txt file """
    
    function = lambda x: scattering_by_angle(angle_of_observation = np.pi*1, distance_from_scattering=5, observation_time=x, wavelength=1e-8, wave_amplitude=1)
    graph_function(function, min=0.1, max=100, num_samples=10000)
