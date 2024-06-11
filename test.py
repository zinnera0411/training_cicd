"""
Test main.py
"""
import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """ Main test class """

    def test_is_upper(self):
        """ test upper case """
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """ test lower case """
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """ test capitalize """
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
