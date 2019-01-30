import numpy as np


def csv_to_list(csv_string):
    """
    Converts a string with comma-separated integer values to a Python list of integers.

    Receives
    --------
    csv_string : string
        Comma-separated integer values.

    Returns
    -------
    integer_list : list
        List of integer values.
    """

    string_list = csv_string.split(',')
    integer_list = list(map(int, string_list))
    return integer_list


def list_to_array(integer_list):
    """
    Converts a list of integer values to an integer NumPy array.

    Receives
    --------
    integer_list : list
        List of integer values.

    Returns
    -------
    integer_array : numpy.array
        Numpy array of integer values.
    """

    integer_array = np.array(integer_list, dtype=int)
    return integer_array


def calculate_mean(integer_list):
    """
    Calculates the mean of a list of integer values.

    Receives
    --------
    integer_list : list
        List of integer values.

    Returns
    -------
    mean : double
        Mean value of the list.
    """

    my_array = list_to_array(integer_list)
    mean = my_array.mean()
    return mean
