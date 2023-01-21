import unittest

from persistence import file_io


# > The `MyTestCase` class is a subclass of the `unittest.TestCase` class
class MyTestCase(unittest.TestCase):
    def test_file_writing(self):
        """
        The function test_file_writing() tests the open_file() function in the file_io module by passing it a made-up file
        name and then checking to see if a FileNotFoundError is raised.
        """
        made_up_file = 'madeupfile.txt'
        file_io.open_file(made_up_file)

        self.assertRaises(FileNotFoundError)
