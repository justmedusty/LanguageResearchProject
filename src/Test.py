import unittest

from business.sorting_functions import SortingFunction
from persistence import file_io


class MyTestCase(unittest.TestCase):
    def test_file_writing(self):
        """
        The function test_file_writing() tests the open_file() function in the file_io module by passing it a made-up file
        name and then checking to see if a FileNotFoundError is raised.
        """
        made_up_file = 'madeupfile.txt'
        file_io.open_file(made_up_file)
        print("Test by Dustyn Gibb")
        self.assertRaises(FileNotFoundError)

    def test_ascending_sort(self):
        """
        It tests the sort_ascending function in the SortingFunction class.
        """
        sorting_function = SortingFunction()
        mock_list = [
            [2], [1], [4], [3], [5], [6]
        ]
        sorted_list = sorting_function.sort_ascending(mock_list)
        self.assertEqual(sorted_list[0], [1])

    def test_descending_sort(self):
        """
        It tests the descending sort function.
        """
        sorting_function = SortingFunction()
        mock_list = [
            [2], [1], [4], [3], [5], [6]
        ]
        sorted_list = sorting_function.sort_descending(mock_list)
        self.assertEqual(sorted_list[0], [6])
