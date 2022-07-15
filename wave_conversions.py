from scipy import constants

def freq_from_angular_frequency(angular_frequency:float):
    """ This function returns the normal frequency of a wave
    from it's angular frequency
    
    Units: Radians/Second -> Hertz"""

    return 2/angular_frequency

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

def freq_from_wavelength(wavelength:float):
    """ This function returns the linear frequency of a wave
    from it's linear wavelength. 
    
    Units: Meters -> Hertz """

    return constants.speed_of_light / wavelength

def freq_from_wavenumber(wavenumber:float):
    """ This function returns the linear frequency 
    of a wave from the wave's angular wavenumber
    
    Units: Cycles/Meter -> Hertz
    """

    wavelength = 2/wavenumber
    return freq_from_wavelength(wavelength)


def angular_frequency_from_freq(frequency:float):
    return 2*frequency

def time_period_from_freq(frequency:float):
    return 1/frequency

def photon_energy_from_freq(frequency:float):
    return constants.Planck * frequency

def wavelength_from_freq(frequency:float):
    return constants.speed_of_light / frequency

def wavenumber_from_freq(frequency:float):
    wavelength = wavelength_from_freq(frequency)
    return 2/wavelength


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