#!/usr/bin/python3

#
# File:         function_defined.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         13-Oct-2021
# Description:  Define some of the major list functions.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# ---------------------------- Function Definitions ---------------------------
def size(my_list):
    """Process a list and return its length.

    Parameters
    ----------
    list
        List whose elements are to be counted.

    Returns
    -------
    int
        The number of elements the list has.
    """
    # Initialise a variable to keep track of each element
    # encountered in the list.
    length = 0

    for _ in my_list:
        length += 1

    return length


def to_string(my_list, sep=', '):
    """Process a list and return the string version of it.

    Parameters
    ----------
    my_list : list
        List to be converted.
    sep : str, default=', '
        Separate each element when converted.

    Returns
    ------
    str
        Result of the conversion of the list.
    """
    # Initialise an empty string to be appended later.
    string = ''

    # Begin the conversion.
    # If the list contains no element (an empty list), returns an empty string.
    if size(my_list) == 0:
        return ''

    else:
        # Initialise a variable to keep track of the location of the current
        # element being iterated.
        count = 1
        for i in my_list:
            if size(my_list) != count:
                string += (str(i) + sep)
            else:
                string += (str(i))
            count += 1
        return string


def count_item(value, my_list):
    """Receive a value and return the occurrences of that value
       in the given list.

    Parameters
    ----------
    value : str
        The element to be counted.
    my_list : list
        The list whose elements are to be counted.

    Returns
    -------
    int
        The occurrences of the specified value.
    """
    # Initialise a variable to count the occurrences of the value.
    count = 0

    for i in my_list:
        if i == value:
            count += 1

    return count


def search(value, my_list):
    """Receive a value and return the location of that value in the given list.

    Parameters
    ----------
    value : str
        The element to be located.
    my_list : list
        The list to be looped through to locate the specified value.

    Returns
    -------
    int or None
        The location of the value in the list,
        or None if the value is not in the list.
    """
    # Initialise a variable to specify the index of the value.
    index = -1
    for i in my_list:
        index += 1
        if i == value:
            return index
    return None




