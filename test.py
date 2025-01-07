from constants import *
from converter import *
import unittest

class TestConvertHeader(unittest.TestCase):

    def test_remove_accents(self):
        self.assertEqual(convert_header('Café'), 'cafe')
        self.assertEqual(convert_header('naïve'), 'naive')
        self.assertEqual(convert_header('résumé'), 'resume')

    def test_lowercase_conversion(self):
        self.assertEqual(convert_header('HEADER'), 'header')
        self.assertEqual(convert_header('HeAdEr'), 'header')

    def test_remove_non_alphanumeric(self):
        self.assertEqual(convert_header('header!@#'), 'header')
        self.assertEqual(convert_header('header 123'), 'header_123')

    def test_field_mappings(self):
        self.assertEqual(convert_header('Telefon komórkowy'), 'mobile_phone')  # Assuming FIELD_MAPPINGS = {'old_field_name': 'new_field_name'}

    def test_replace_spaces_with_underscores(self):
        self.assertEqual(convert_header('header with spaces'), 'header_with_spaces')

    def test_multiple_spaces_to_single_underscore(self):
        self.assertEqual(convert_header('header    with    spaces'), 'header_with_spaces')



if __name__ == '__main__':
    unittest.main()
