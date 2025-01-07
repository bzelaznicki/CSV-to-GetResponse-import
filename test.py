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
    def test_empty_string(self):
        self.assertEqual(convert_header(''), '')

    def test_mixed_cases(self):
        self.assertEqual(convert_header('E-mail Address'), 'email')
        self.assertEqual(convert_header('ZIP Code'), 'postal_code')

    def test_leading_trailing_spaces(self):
        self.assertEqual(convert_header('  header  '), 'header')

    def test_special_characters_with_numbers(self):
        self.assertEqual(convert_header('Phone#1'), 'phone_1')
        self.assertEqual(convert_header('Contact-2'), 'contact_2')

    def test_empty_csv(self):
        with self.assertRaises(ValueError) as context:
            get_and_convert_headers("")
        self.assertEqual(str(context.exception), 'CSV appears to be empty')

    def test_whitespace_only_headers(self):
        with self.assertRaises(ValueError) as context:
            get_and_convert_headers("   ,  ,  ")
        self.assertEqual(str(context.exception), 'All headers were invalid or empty after conversion')

    def test_special_chars_only(self):
        with self.assertRaises(ValueError) as context:
            get_and_convert_headers("!@#,$%^,&*()")
        self.assertEqual(str(context.exception), 'All headers were invalid or empty after conversion')

    def test_valid_and_invalid_mixed(self):
        result = get_and_convert_headers("valid,   ,!@#,name,###")
        self.assertEqual(result, ['valid', 'name'])
    def test_quoted_headers(self):
        csv_data = '"First Name","Last,Name","Email Address"'
        result = get_and_convert_headers(csv_data)
        self.assertEqual(result, ['first_name', 'last_name', 'email'])  # email_address -> email

    def test_mixed_quoted_unquoted(self):
        csv_data = 'ID,"Full Name",email,"Phone,Number"'
        result = get_and_convert_headers(csv_data)
        self.assertEqual(result, ['id', 'full_name', 'email', 'phone_number'])

    def test_field_mappings(self):
        csv_data = '"Email Address","Phone Number","First Name"'
        result = get_and_convert_headers(csv_data)
        self.assertEqual(result, ['email', 'phone', 'first_name'])  # Testing multiple mappings
    def test_polish_headers(self):
        csv_data = '"imie","nazwisko","telefon komorkowy","kod pocztowy"'
        result = get_and_convert_headers(csv_data)
        self.assertEqual(result, ['first_name', 'last_name', 'mobile_phone', 'postal_code'])    

    def test_email_variations(self):
        csv_data = '"e-mail","email address","e-mail_address","adres email"'
        result = get_and_convert_headers(csv_data)
        self.assertEqual(result, ['email', 'email', 'email', 'email'])   
    
    def test_accented_headers(self):
        csv_data = '"Téléphone","E-mail","Prénom","Straße"'
        result = get_and_convert_headers(csv_data)
        # Update expectation to match our standardized mappings
        self.assertEqual(result, ['phone', 'email', 'first_name', 'street'])

    def test_special_chars(self):
        csv_data = '"Phone #","E_mail","Street address","ZIP"'
        result = get_and_convert_headers(csv_data)
        # Update expectation to match our standardized mappings
        self.assertEqual(result, ['phone', 'email', 'street', 'postal_code'])

    def test_mixed_accents_and_mappings(self):
        csv_data = '"téléphone komórkowy","adres émail","código postal"'
        result = get_and_convert_headers(csv_data)
        self.assertEqual(result, ['telephone_komorkowy', 'email', 'postal_code'])
if __name__ == '__main__':
    unittest.main()
