import numpy as np
import copy

def swap_indices(arr, index_a:int, index_b:int) -> None:
    """Swap two indices of an array

    Parameters
    ----------
    arr : array_like
        The array to swap 
    index_a, index_b : int
        The indices of 'arr' to swap
    
    Returns
    -------
    None
    """    

    temp = copy.copy(arr[index_a])
    arr[index_a] = arr[index_b]
    arr[index_b] = temp

def flatten_matrix(matrix):
    """Return a flattened version of a matrix

    Parameters
    ----------
    matrix : 2d array_like
        The matrix to flatten.

    Returns
    -------
    1d array_like 
        A flattened version of the passed matrix.
    
    See Also
    --------
    np.ndarray.flatten : A method to flatten numpy arrays. Much faster 
    than this function, which should only be used for other array_like
    types.
    """
        
    items = []
    for row in matrix:
        for element in row:
            items.append(element)
    return items

def num_differences(arr_a, arr_b):
    """Return the number of indices containing different values between 
    two array_like's.

    Parameters
    ----------
    arr_a, arr_b : array_like
        The two arrays to find the different indices between

    Returns
    -------
    int
        Number of different indices between the two arrays
    """    
    assert len(arr_a) == len(arr_b), "Both arrays need to be the same shape"

    differences = 0
    for i, e in enumerate(arr_a):
        if e != arr_b[i]:
            differences += 1
    return differences

def get_different_index(arr_a, arr_b, check_single_difference=False) -> int:
    """ Return the first index between two equally sized arrays that
    contain different values.

    Parameters
    ----------
    arr_a, arr_b : array_like
       The two arrays to compare.
    
    check_single_difference : bool, default=False
        Weather or not to check if there is only one index with a 
        different value between the two arrays.

    Raises
    ------
    ValueError
        If 'arr_a' and 'arr_b' are not of the same length.

    Returns
    -------
    int
        The first index with a different between 'arr_a' and 'arr_b'.
    """    

    if len(arr_a) != len(arr_b):
        raise ValueError("Arr a and b must have the same length")

    if check_single_difference:
        num_diff = num_differences(arr_a, arr_b)
        assert num_diff == 1, f"There are a total of {num_diff} indices different between the two arrays, there should only be one"
    
    for i, e in enumerate(arr_a):
        if arr_b[i] != e:
            return i

def get_indices(arr, indices) -> list:
    """Return a list of the values in each index of 'indices'

    Parameters
    ----------
    arr : array_like
        The array containing the values composing the returned list 
    indices : array_like
        A list of each index to make up the returned list

    Returns
    -------
    list
        A list containing the value of arr at each index in indices
    """    
    elements = []
    for index in indices:
        elements.append(arr[index])
    return elements

def exclude_indices(arr, indices) -> list:
    if len(indices) > 8: #Totally arbitrary value for optimization
        indices = set(indices)
    
    elements = []
    for i, item in enumerate(arr):
        if i not in indices:
            elements.append(item)
    
    return elements

def fill_skipping(arr, values, indices):
    new_arr = []

    if len(indices) > 8: #Totally arbitrary value for optimization
        indices = set(indices)
    
    value_ind = 0
    for i, element in enumerate(arr):
        if i not in indices:
            new_arr.append(values[value_ind])
            value_ind += 1
        else:
            new_arr.append(element)
    
    return new_arr

def multiply_by_scalar(arr, scalar):
    products = []
    for element in arr:
        products.append(element*scalar)
    return products