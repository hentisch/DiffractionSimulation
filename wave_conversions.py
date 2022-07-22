from scipy import constants
import numpy as np

def freq_from_angular_frequency(angular_frequency:float) -> float:
    """Returns the linear frequency of a wave based on it's angular 
    frequency.

    Parameters
    ----------
    angular_frequency : float 
        The angular frequency of the wave. This should be represented
        in radians/second.

    Returns
    -------
    float
        The linear frequency of the wave. This will be represented
        in Hertz, assuming you passed the correct units.
    """    

    return angular_frequency/2*np.pi

def freq_from_wavenumber(wavenumber:float):
    """Returns the linear frequency of a wave based on it's wavenumber.

    Parameters
    ----------
    wavenumber : float 
        The wavenumber of the wave. This should be represented in Cycles/
        Meter.

    Returns
    -------
    float
        The linear frequency of the wave. This will be represented
        in Hertz, assuming you passed the correct units.
    """    

    wavelength = 2*np.pi/wavenumber
    return freq_from_wavelength(wavelength)

def freq_from_wavelength(wavelength:float):
    """Returns the linear frequency of a light wave based on it's 
    wavelength.

    Parameters
    ----------
    wavelength : float 
        The wavelength of the wave. This should be represented in meters.

    Returns
    -------
    float
        The linear frequency of the wave. This will be represented
        in Hertz, assuming you passed the correct units.
    """    

    return constants.speed_of_light / wavelength

def freq_from_time_period(time_period:float):
    """Returns the linear frequency of a wave based on it's time period.

    Parameters
    ----------
    angular_frequency : float 
        The angular frequency of the wave. This should be represented
        in radians/second.

    Returns
    -------
    float
        The linear frequency of the wave. This will be represented
        in Hertz, assuming you passed the correct units.
    """    
    return 1/time_period

def freq_from_photon_energy(photon_energy:float):
    """Returns the linear frequency of a wave based on it's photon energy.

    Parameters
    ----------
    photon_energy : float 
        The photon_energy of the wave. This should be represented
        in Joules.

    Returns
    -------
    float
        The linear frequency of the wave. This will be represented
        in Hertz, assuming you passed the correct units.
    """    
    return constants.Planck/photon_energy


def angular_frequency_from_freq(frequency:float):
    """Returns the angular frequency of a wave based on it's linear frequency.

    Parameters
    ----------
    frequency : float 
        The linear frequency of the wave. This should be represented
        in Hertz.

    Returns
    -------
    float
        The angular frequency of the wave. This will be represented
        in rotations/second, assuming you passed the correct units.
    """    

    return 2*np.pi*frequency

def time_period_from_freq(frequency:float):
    """Returns the time period of a wave based on it's frequency.

    Parameters
    ----------
    frequency : float
        The linear frequency of the wave. This should be represented 
        in Hertz.

    Returns
    -------
    float
        The time period of the wave. This should be represented in 
        seconds, assuming you passed the correct units.
    """    
    
    return 1/frequency

def photon_energy_from_freq(frequency:float):
    """Returns the photon energy of a wave based on it's frequency.

    Parameters
    ----------
    frequency : float
        The linear frequency of the wave. This should be represented 
        in Hertz.

    Returns
    -------
    float
        The photon energy of the wave. This should be represented in 
        Joules, assuming you passed the correct units.
    """    

    return constants.Planck * frequency

def wavelength_from_freq(frequency:float):
    """Returns the wavelength of a wave based on it's frequency.

    Parameters
    ----------
    frequency : float
        The linear frequency of the wave. This should be represented 
        in Hertz.

    Returns
    -------
    float
        The wavelength of the wave. This should be represented in 
        Joules, assuming you passed the correct units.
    """    

    return constants.speed_of_light / frequency

def wavenumber_from_freq(frequency:float):
    """Returns the wavenumber of a wave based on it's frequency.

    Parameters
    ----------
    frequency : float
        The linear frequency of the wave. This should be represented 
        in Hertz.

    Returns
    -------
    float
        The wavenumber of the wave. This should be represented in 
        Cycles/Meter, assuming you passed the correct units.
    """    

    wavelength = wavelength_from_freq(frequency)
    return 2*np.pi/wavelength


def convert(value:float, unit:str, converted_unit:str):
    """Returns the equivalent value of unit a, with unit type b

    Parameters
    ----------
    value : float
        The value of the unit you are trying to convert
    unit : {"angular_frequency", "time_period", "photon_energy", "wavelength", "wavenumber", "frequency"}
        The unit of 'value'
    converted_unit : {"angular_frequency", "time_period", "photon_energy", "wavelength", "wavenumber", "frequency"}
        The unit you would like to convert 'value' to 

    Returns
    -------
    float
        'value', converted to 'converted_unit'
    
    Note
    ----
    When passing a value, make sure to use the respective base SI unit. 
    For reference, these are the base SI units for all of the units this
    function supports.

    angular frequency : radians/seconds,
    time period : seconds
    photon energy : joules
    wavelength : meters
    wavenumber : cycles/meter
    frequency : hertz
    """    

    functions = {
        "angular_frequency": (freq_from_angular_frequency, angular_frequency_from_freq),
        "time_period": (freq_from_time_period, time_period_from_freq),
        "photon_energy": (freq_from_photon_energy, photon_energy_from_freq),
        "wavelength": (freq_from_wavelength, wavelength_from_freq),
        "wavenumber": (freq_from_wavenumber, wavenumber_from_freq),
        "frequency": (lambda x: x, lambda x: x)
    }

    frequency = functions[unit][0](value)

    return functions[converted_unit][1](frequency)