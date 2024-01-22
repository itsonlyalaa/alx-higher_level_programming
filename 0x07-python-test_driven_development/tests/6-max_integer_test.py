#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test_maxinteger class to test the max_integer function"""

    def test_Normal(self):
        """Normal cases"""
        self.assertEqual(max_integer([3, 4, 5]), 5)
        self.assertEqual(max_integer([-6, -2, 5]), 5)
        self.assertEqual(max_integer([-4, -32, -3]), -3)
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_List_Is_Empty(self):
        """An empty list"""
        self.assertEqual(max_integer([]), None)

    def test_Max_Int_List(self):
        """"Find the max in a list of ints"""
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), max(list1))

    def test_Max_Float_List(self):
        """Find the max in a list of floats"""
        list2 = [2.3, 7.3, 2.6, 3.3, 5.9]
        self.assertEqual(max_integer(list2), max(list2))

    def test_Max_Float_Int_List(self):
        """Find the max in a list of int and floats"""
        list3 = [2.3, 7.3, 2.6, 3.3, 5.9, 4, 8, 11, 12]
        self.assertEqual(max_integer(list3), max(list3))

    def test_Negative_List(self):
        """Find the max in a list of negative int and floats"""
        list4 = [-2.3, -7.3, -2.6, -3.3, -5.9, -4, -8, -11, -12]
        self.assertEqual(max_integer(list4), max(list4))

    def test_Argument_Is_String(self):
        """Raise TypeError if the argument is a string"""
        with self.assertRaises(TypeError):
            max_integer("Hello world", 1)

    def test_Argument_Is_Tuple(self):
        """Raise TypeError if the argument is a tuple"""
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3)

    def test_Argument_Is_Int_Float(self):
        """Raise TypeError if the argument is a int or float"""
        with self.assertRaises(TypeError):
            max_integer(3)
        with self.assertRaises(TypeError):
            max_integer(3.4)

    def test_Argument_Is_Boolean(self):
        """Raise TypeError if the argument is a bool"""
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_Special_Chars(self):
        """Test error cases"""
        with self.assertRaises(TypeError):
            max_integer("", "")

if __name__ == '__main__':
    unittest.main()
