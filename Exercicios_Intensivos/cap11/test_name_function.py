import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Teste oarra 'name_function.py' """

    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam? """
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_midle_name(self):
        """ Nmes como 'Wolfgang Amadeus Mozart' funcionam?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'amadeus', 'mozart'
        )
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')


unittest.main()