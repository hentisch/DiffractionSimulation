from math import atan2, dist
from random import random
import numpy as np
import scipy as sp

from astropy import constants
from astropy import units as u

from scipy import integrate

import wave_conversions as wc

import cmath

from geometry_utils import angle_between_lines, index_by_dimension
from array_utils import get_different_index, get_indices, num_differences
from utils import graph_3d_function, graph_function

from numba import njit

#TODO, make this method return phase and amplitude
@njit()
def scattering_by_angle(angle_of_observation:float, distance_from_scattering:float, observation_time:float, wavelength:float, wave_amplitude:float, returned_value="amplitude", round_cos=False) -> float:
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
    returned_value : [{"amplitude", "phase", "both"}, optional]
        The part of the scattered wave to be returned
    round_cos : bool
        If True, the cosine value which attenuates the scattering will be
        rounded. Note that while this does make the values of the function
        more predictable, it does have a significant effect on performance
        when this function is called many times.
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
    
    # thomson_scattering_length = sp.constants.value("classical electron radius")

    thomson_scattering_length = 2.8179403262e-15

    oscillatory_multiplicand = -thomson_scattering_length*wave_amplitude
    
    wavenumber = wc.convert(wavelength, "wavelength", "wavenumber")
    angular_frequency = wc.convert(wavelength, "wavelength", "angular_frequency")

    thing = wavenumber*distance_from_scattering - angular_frequency*observation_time

    real_oscillatory_value = np.cos(thing) + np.sin(thing)

    cosine_val = np.cos(angle_of_observation)

    if round_cos:
        cosine_val = np.round(cosine_val, 5)

    if returned_value == "real":
        return oscillatory_multiplicand * real_oscillatory_value  * cosine_val
    else:
        complex_value = oscillatory_multiplicand * real_oscillatory_value * 1j * cosine_val

    if returned_value == "imaginary":
        return complex_value.imag

    amplitude, phase = cmath.polar(complex_value)

    if returned_value == "amplitude":
        return amplitude
    elif returned_value == "phase":
        return phase
    elif returned_value == "both":
        complex_value
    else:
        raise ValueError(f"Could not interpret the returned value parameter, please, use either \"amplitude\" or \"phase\"")

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

def charge_distribution(distance_from_atom, electron_shell):
    #To prevent overflow errors, this method represents values
    #internally as nanometers
    electron_distances = [x/1e-9 for x in [2e-11, 1.6e-10]]
    electron_distance = electron_distances[electron_shell]

    distance_from_atom /= 1e-9

    nominator = np.exp(-(2*distance_from_atom / electron_distance))
    denominator = np.pi * electron_distance**3
    return nominator/denominator * 1e-9

@njit()
def integrable_function(angle_of_observation, distance_of_observation, incident_field_strength=1, wavelength=1, observation_time=0, returned_value="amplitude"):
    spherical_integral_conversion = distance_of_observation**2 * np.sin(angle_of_observation)
    return scattering_by_angle(angle_of_observation, distance_of_observation, observation_time, wavelength, incident_field_strength, returned_value=returned_value) * spherical_integral_conversion

def scattering_from_atom(incident_field_strength, wavelength, observation_time, returned_value="amplitude"):
    integrated_value, err = integrate.dblquad(integrable_function, 0, np.inf, 0, np.pi, args=(incident_field_strength, wavelength, observation_time, returned_value))
    return integrated_value * np.pi * 2
    
if __name__ == "__main__":
    """ This script is not really meant to be ran on it's own - this bit of code just allows you to graph different variables of the function
    for the purpose of debugging."""
    
    # graph_3d_function(lambda angle, dist: scattering_by_angle(angle, dist, 1, 1, 1, "phase"), 0.1, 10, 300, "angle", "distance from observation", "phase")
    # graph_3d_function(lambda angle, dist: scattering_by_angle(angle, dist, 1, 1, 1, "amplitude"), 0.1, 10, 300, "angle", "distance from observation", "amplitude")

    # result, err = integrate.quad(lambda r: charge_distribution(r, 0), 0, 1e-13)
    # print(result)
    # graph_function(lambda x: charge_distribution(x, 0), 1e-13, 1e-11, 1000)
    # print(charge_distribution(10, 0))
    # print(result)
