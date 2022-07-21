import numpy as np

def rgb_to_mayavi(r:int, g:int, b:int) -> tuple:
    """Returns the passed integer R, G, and B values as a tuple of floats
    between 0 and 1 (instead of 0-255).


    Parameters
    ----------
    r, g, b : int
        The R, G, and B values of a 24 bit color on a range from 0/255

    Returns
    -------
    tuple of float (r, g, b)
        The R, G, and B values of a 24 bit color on a range from 0-1
    """
    
    return r/255, g/255, b/255

def graph_function(func:'function', min:float, max:float, num_samples:int) -> None:
    """Display a graph of a numerical function

    Parameters
    ----------
    func : function(float)
        The function to be graphed
    min : float
        The minimum value of the plot
    max : float
        The maximum value of the plot
    num_samples : int
        The number of points to calculate and render on the plot. Note
        that higher values will create a smoother plot, though will also
        take longer to be display and be slower to interact with.
    
    Returns
    -------
    None

    Notes
    -----
    This function uses matplotlib, which is not listed as a requirement
    in this project. To install matplotlib just use pip install matplotlib
    """    

    import matplotlib.pyplot as plt

    x_values = np.linspace(min, max, num=num_samples)

    y_values = np.zeros(num_samples)

    for i, x in enumerate(x_values):
        y_values[i] = func(x)
        # print(func(x))
    
    plt.plot(x_values, y_values)

    plt.show()