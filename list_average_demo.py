# -*- coding: utf-8 -*-

"""list_average_demo.py
Simple demo of how to calculate the average of a list of numbers.
"""

from functools import reduce
from numpy import mean


def check_list_type(num_list):
    """
    Checks the type of the variable informed.
    :param num_list: list to be checked.
    :return: True if OK.
    """
    if not isinstance(num_list, (list, tuple)):
        raise TypeError("Expecting list or tuple. Got: {}".format(type(num_list)))

    return True


def check_list_item_type(num_list):
    """
    Checks the type of items in the informed list.
    :param num_list: list to be checked.
    :return: True if OK.
    """
    if not all([isinstance(i, (int, float)) for i in num_list]):
        raise TypeError("The list can only contain ints or floats")

    return True


def check_list_size(num_list):
    """
    Checks the size of the list..
    :param num_list: list to be checked.
    :return: True if OK.
    """
    if len(num_list) == 0:
        raise ValueError("Cannot calculate average for an empty list.")

    return True


def check_list(num_list):
    """
    Basic checks to see if list is valid.
    :param num_list: list/tuple of numbers that will be used.
    :return: True if everything is OK. Raises Exception in case of errors.
    """
    check_list_type(num_list=num_list)
    check_list_item_type(num_list=num_list)
    check_list_size(num_list=num_list)

    return True


def simple_avg(num_list):
    """
    Simple average.
    :param num_list: list to be used in calculation.
    :return: average of item lists.
    """
    check_list(num_list=num_list)
    return sum(num_list) / len(num_list)


def simple_avg_numpy(num_list):
    """
    Simple average using the mean function from Numpy.
    :param num_list: list to be used in calculation.
    :return: average of item lists.
    """
    check_list(num_list=num_list)
    return mean(num_list)


def not_so_simple_avg(num_list):
    """
    Average of items in a list using reduce + lambda.
    :param num_list: list to be used in calculation.
    :return: average of item lists.
    """
    check_list(num_list=num_list)
    return reduce(lambda x, y: x + y, num_list) / len(num_list)


def main():
    """
    Main function. Quick way to interact with the user.
    If you want, run the tests for a more complete overview.
    :return: True
    """
    my_numbers_str = input("Type the numbers you want, separating them with commas. (Example: 1, 2, 3, 4, 5, 6)\n> ")
    my_numbers = list()
    for str_n in my_numbers_str.split(","):
        try:
            my_numbers.append(int(str_n))

        except:
            my_numbers.append(float(str_n))

    print("\nThe results are in:")
    print("simple_avg:\t\t\t{}".format(simple_avg(num_list=my_numbers)))
    print("simple_avg_numpy:\t{}".format(simple_avg_numpy(num_list=my_numbers)))
    print("not_so_simple_avg:\t{}".format(not_so_simple_avg(num_list=my_numbers)))

    return True


if __name__ == '__main__':
    main()
