import matplotlib.pyplot as plt
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

def add_graph_to_plot(func:'function', min:float, max:float, num_samples:int, color="black"):
    x_values = np.linspace(min, max, num=num_samples)

    y_values = np.zeros(num_samples)

    for i, x in enumerate(x_values):
        y_values[i] = func(x)
    
    plt.plot(x_values, y_values,  color=color)

def graph_function(func:'function', min:float, max:float, num_samples:int, title=None, x_label=None, y_label=None) -> None:
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
    title : str, optional
        A title to be rendered with the plot
    x_label, y_label : str
        A label for the x and y axis, which will be rendered with the 
        plot.
    
    Returns
    -------
    None

    Notes
    -----
    This function uses matplotlib, which is not listed as a requirement
    in this project. To install matplotlib just use pip install matplotlib
    """    
    add_graph_to_plot(func, min, max, num_samples)

    if title != None:
        plt.title(title)
    
    if x_label != None:
        plt.xlabel(x_label)
    
    if y_label != None:
        plt.ylabel(y_label)

    plt.show()