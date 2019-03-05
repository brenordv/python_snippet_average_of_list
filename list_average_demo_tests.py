# -*- coding: utf-8 -*-

from unittest import TestCase, main

from list_average_demo import check_list_type, check_list_item_type, check_list_size
from list_average_demo import simple_avg, simple_avg_numpy, not_so_simple_avg


class ListValidationTest(TestCase):
    """
    Checks the type of the informed list.
    It must be a list or a tuple.
    """

    def test_list_type_string(self):
        """Passes the wrong type for the variable."""
        self.assertRaises(TypeError, check_list_type, **{"num_list": "wrong_type"})

    def test_list_type_int(self):
        """Passes the wrong type for the variable."""
        self.assertRaises(TypeError, check_list_type, **{"num_list": 1})

    def test_list_type_float(self):
        """Passes the wrong type for the variable."""
        self.assertRaises(TypeError, check_list_type, **{"num_list": 2.5})

    def test_list_type_list(self):
        """Passes the correct type for the variable."""
        self.assertTrue(check_list_type(num_list=[]))

    def test_list_type_tuple(self):
        """Passes the correct type for the variable."""
        self.assertTrue(check_list_type(num_list=(1, 2)))


class ListItemValidationTest(TestCase):
    """
    Checks the items inside the list. They must be either int or float.
    """

    def test_list_item_type_string(self):
        """Passes the wrong type of item."""
        self.assertRaises(TypeError, check_list_item_type, **{"num_list": ["foo", "bar"]})

    def test_list_item_type_dict(self):
        """Passes the wrong type of item."""
        self.assertRaises(TypeError, check_list_item_type, **{"num_list": [{}, {}]})

    def test_list_item_type_none(self):
        """Passes the wrong type of item."""
        self.assertRaises(TypeError, check_list_item_type, **{"num_list": [None, None]})

    def test_list_item_type_valid_int(self):
        """Passes the correct type of item."""
        self.assertTrue(check_list_item_type(num_list=(1, 2)))

    def test_list_item_type_valid_float(self):
        """Passes the correct type of item."""
        self.assertTrue(check_list_item_type(num_list=(1.4, 2.75)))

    def test_list_item_type_valid_mixed(self):
        """Passes the correct type of item."""
        self.assertTrue(check_list_item_type(num_list=(1, 2.75)))


class ListSizeValidationTest(TestCase):
    """
    Checks the size of the list that will be used in the calculation.
    Must have at least 1 item.
    """

    def test_list_size_invalid(self):
        """Passes a list with the wrong number of items."""
        self.assertRaises(ValueError, check_list_size, **{"num_list": []})

    def test_list_size_invalid2(self):
        """Passes a list with the wrong number of items."""
        self.assertRaises(ValueError, check_list_size, **{"num_list": list()})

    def test_list_size_valid_single(self):
        """Passes a list with the correct number of items."""
        self.assertTrue(check_list_size(num_list=[1]))

    def test_list_size_valid_multiple(self):
        """Passes a list with the correct number of items."""
        self.assertTrue(check_list_size(num_list=[1, 2]))


class AverageSimpleAvgTest(TestCase):
    """
    Tests the function 'simple_avg'
    """
    def test_average_all_ints(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(5.5, simple_avg(num_list=my_numbers))

    def test_average_all_floats(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1.25, 2.10, 3.25, 4.10, 5.10, 6.25, 7.66, 8.25, 9.66, 10.25]
        self.assertEqual(5.786999999999999, simple_avg(num_list=my_numbers))

    def test_average_mixed(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1, 2, 3, 4, 5.25, 6.66, 7.80, 8.90, 8.04, 9, 10]
        self.assertEqual(5.968181818181819, simple_avg(num_list=my_numbers))


class AverageSimpleAvgNumPyTest(TestCase):
    """
    Tests the function 'simple_avg_numpy'
    """
    def test_average_all_ints(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(5.5, simple_avg_numpy(num_list=my_numbers))

    def test_average_all_floats(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1.25, 2.10, 3.25, 4.10, 5.10, 6.25, 7.66, 8.25, 9.66, 10.25]
        self.assertEqual(5.786999999999999, simple_avg_numpy(num_list=my_numbers))

    def test_average_mixed(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1, 2, 3, 4, 5.25, 6.66, 7.80, 8.90, 8.04, 9, 10]
        self.assertEqual(5.968181818181819, simple_avg_numpy(num_list=my_numbers))


class AverageNotSoSimpleAvgTest(TestCase):
    """
    Tests the function 'no_so_simple_avg'
    """
    def test_average_all_ints(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(5.5, not_so_simple_avg(num_list=my_numbers))

    def test_average_all_floats(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1.25, 2.10, 3.25, 4.10, 5.10, 6.25, 7.66, 8.25, 9.66, 10.25]
        self.assertEqual(5.786999999999999, not_so_simple_avg(num_list=my_numbers))

    def test_average_mixed(self):
        """Passes a valid list and checks it against it's proven value."""
        my_numbers = [1, 2, 3, 4, 5.25, 6.66, 7.80, 8.90, 8.04, 9, 10]
        self.assertEqual(5.968181818181819, not_so_simple_avg(num_list=my_numbers))


if __name__ == '__main__':
    main()
