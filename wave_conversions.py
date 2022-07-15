from scipy import constants
import numpy as np

""" Note: Any measure of degree will be in radians """

def freq_from_angular_frequency(angular_frequency:float):
    """ This function returns the normal frequency of a wave
    from it's angular frequency
    
    Units: Radians/Second -> Hertz"""

    return angular_frequency/2*np.pi

def freq_from_wavenumber(wavenumber:float):
    """ This function returns the linear frequency 
    of a wave from the wave's angular wavenumber
    
    Units: Cycles/Meter -> Hertz
    """

    wavelength = 2*np.pi/wavenumber
    return freq_from_wavelength(wavelength)

def freq_from_wavelength(wavelength:float):
    """ This function returns the linear frequency of a wave
    from it's linear wavelength. 
    
    Units: Meters -> Hertz """

    return constants.speed_of_light / wavelength

def freq_from_time_period(time_period:float):
    """ This function returns the linear frequency 
    of a wave from it's time period
    
    Seconds -> Hertz"""
    return 1/time_period

def freq_from_photon_energy(photon_energy:float):
    """ Returns the linear frequency of a wave
    from it's photon energy
    
    Units: Joules -> Hertz """

    return constants.Planck/photon_energy


def angular_frequency_from_freq(frequency:float):
    """ Returns the angular frequency of a wave
    from it's linear frequency
    
    Units: Hertz -> Rotations/Second """

    return 2*np.pi*frequency

def time_period_from_freq(frequency:float):
    """ Returns the time period of a wave from
    it's linear frequency
    
    Units: Hertz -> Seconds """
    
    return 1/frequency

def photon_energy_from_freq(frequency:float):
    """ Returns the photon energy of a wave
    from it's linear frequency 
    
    Units: Hertz -> Joules """

    return constants.Planck * frequency

def wavelength_from_freq(frequency:float):
    """ Returns the wavelength of a wave
    from it's linear frequency
    
    Untils: Hertz -> Meters """

    return constants.speed_of_light / frequency

def wavenumber_from_freq(frequency:float):
    """ Returns the wavenumber of a wave
    from it's linear frequency
    
    Utils: Hertz -> Cycles/Meter """

    wavelength = wavelength_from_freq(frequency)
    return 2*np.pi/wavelength


def convert(unit_a:float, unit_a_type:str, unit_b_type:str):
    
    """ In this dictionary, each key has a tuple of functions as it's values, the first
    function converting from a given unit into frequency, and the second converting
    from frequency into the unit of the key. """

    functions = {
        "angular_frequency": (freq_from_angular_frequency, angular_frequency_from_freq),
        "time_period": (freq_from_time_period, time_period_from_freq),
        "photon_energy": (freq_from_photon_energy, photon_energy_from_freq),
        "wavelength": (freq_from_wavelength, wavelength_from_freq),
        "wavenumber": (freq_from_wavenumber, wavenumber_from_freq),
        "frequency": (lambda x: x, lambda x: x)
    }

    frequency = functions[unit_a_type][0](unit_a)

    return functions[unit_b_type][1](frequency)