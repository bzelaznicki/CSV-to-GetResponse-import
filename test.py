from constants import *
from converter import *
import unittest

class TestConvertHeader(unittest.TestCase):
    
    def test_minimal_headers(self):
        # Test with just a few essential columns
        csv_data = '''email,first_name,tags
    test@example.com,John,"tag1, tag2"'''
        
        result = process_csv_data(csv_data)
        expected = [{
            "email": "test@example.com",
            "first_name": "John",
            "tags": ["tag1", "tag2"]
        }]
        self.assertEqual(result, expected)

    def test_all_standard_headers(self):
        # Test with all common fields
        csv_data = '''email,tags,first_name,last_name,address,city,state,postal_code
    test@example.com,"tag1,tag2",John,Doe,123 Main St,Boston,MA,12345'''
        
        result = process_csv_data(csv_data)
        expected = [{
            "email": "test@example.com",
            "tags": ["tag1", "tag2"],
            "first_name": "John",
            "last_name": "Doe",
            "address": "123 Main St",
            "city": "Boston",
            "state": "MA",
            "postal_code": "12345"
        }]
        self.assertEqual(result, expected)

    def test_extra_headers(self):
        # Test with extra columns that aren't in our mapping
        csv_data = '''email,custom_field,first_name,tags,unknown_column
    test@example.com,custom_value,John,"tag1,tag2",ignore_this'''
        
        result = process_csv_data(csv_data)
        expected = [{
            "email": "test@example.com",
            "first_name": "John",
            "tags": ["tag1", "tag2"],
            "custom_field": "custom_value",
            "unknown_column": "ignore_this"
        }]
        self.assertEqual(result, expected)
    def test_empty_tags(self):
        csv_data = '''email,tags
    test@example.com,""'''
        result = process_csv_data(csv_data)
        expected = [{"email": "test@example.com", "tags": []}]
        self.assertEqual(result, expected)

    def test_mixed_whitespace_tags(self):
        csv_data = '''email,tags
    test@example.com,"  tag1,    tag2   ,tag3  "'''
        result = process_csv_data(csv_data)
        expected = [{"email": "test@example.com", "tags": ["tag1", "tag2", "tag3"]}]
        self.assertEqual(result, expected)

    def test_duplicate_headers(self):
        # Test how system handles duplicate headers
        csv_data = '''email,tags,email
    test@example.com,"tag1,tag2",another@example.com'''
        with self.assertRaises(ValueError):
            process_csv_data(csv_data)

    def test_empty_csv(self):
        csv_data = ""
        with self.assertRaises(ValueError):
            process_csv_data(csv_data)        
    def test_headers_only(self):
        csv_data = '''email,tags'''
        result = process_csv_data(csv_data)
        self.assertEqual(result, [])  # Should return empty list when no data rows

    def test_malformed_csv(self):
        csv_data = '''email,tags
    test@example.com,"unclosed quote string",tag1,extra_column
    next@example.com,tag2'''
        with self.assertRaises(ValueError):  # Changed to ValueError
            process_csv_data(csv_data)
    def test_various_email_formats(self):
        csv_data = '''email,tags
    not_an_email,tag1
    test@example.com,tag2
    missing@.com,tag3
    @incomplete.com,tag4'''
        result = process_csv_data(csv_data)
        expected = [
            {"email": "not_an_email", "tags": ["tag1"]},
            {"email": "test@example.com", "tags": ["tag2"]},
            {"email": "missing@.com", "tags": ["tag3"]},
            {"email": "@incomplete.com", "tags": ["tag4"]}
        ]
        self.assertEqual(result, expected)    
    def test_special_chars_in_tags(self):
        csv_data = '''email,tags
    test@example.com,"tag#1,tag$2,tag@3,tag&4,tag-5"'''
        result = process_csv_data(csv_data)
        expected = [
            {"email": "test@example.com", "tags": ["tag#1", "tag$2", "tag@3", "tag&4", "tag-5"]}
        ]
        self.assertEqual(result, expected)         
    def test_line_endings(self):
        # Unix style (\n)
        unix_csv = '''email,tags\ntest@example.com,"tag1,tag2"\nother@example.com,"tag3,tag4"'''
        
        # Windows style (\r\n)
        windows_csv = '''email,tags\r\ntest@example.com,"tag1,tag2"\r\nother@example.com,"tag3,tag4"'''
        
        # Old Mac style (\r)
        mac_csv = '''email,tags\rtest@example.com,"tag1,tag2"\rother@example.com,"tag3,tag4"'''
        
        expected = [
            {"email": "test@example.com", "tags": ["tag1", "tag2"]},
            {"email": "other@example.com", "tags": ["tag3", "tag4"]}
        ]
        
        # All three should produce the same output
        self.assertEqual(process_csv_data(unix_csv), expected)
        self.assertEqual(process_csv_data(windows_csv), expected)
        self.assertEqual(process_csv_data(mac_csv), expected)
    def test_unicode_chars(self):
        csv_data = '''email,tags
    üser@example.com,"tág1,标签2,タグ3"'''
        expected = [
            {"email": "üser@example.com", "tags": ["tág1", "标签2", "タグ3"]}
        ]
        self.assertEqual(process_csv_data(csv_data), expected)           
    def test_large_file(self):
        large_csv = "email,tags\n" + "\n".join([
            f'test{i}@example.com,"tag1,tag2,tag3"'
            for i in range(10000)
        ])
        result = process_csv_data(large_csv)
        self.assertEqual(len(result), 10000)
        # Check first and last entries
        self.assertEqual(result[0], {"email": "test0@example.com", "tags": ["tag1", "tag2", "tag3"]})
        self.assertEqual(result[-1], {"email": "test9999@example.com", "tags": ["tag1", "tag2", "tag3"]})  
    def test_different_encodings(self):
        # UTF-8 with BOM, UTF-16, etc
        csv_data = '''email,tags
    José@example.com,"tág1,漢字,🐻"
    भारत@example.com,"тег1,العلامة,테스트"'''
        
        # Test with different encodings
        encodings = ['utf-8', 'utf-8-sig', 'utf-16']
        for encoding in encodings:
            # Encode the data in the specified encoding
            encoded_data = csv_data.encode(encoding)
            # Decode it back and process
            decoded_data = encoded_data.decode(encoding)
            result = process_csv_data(decoded_data)
            
            expected = [
                {"email": "José@example.com", "tags": ["tág1", "漢字", "🐻"]},
                {"email": "भारत@example.com", "tags": ["тег1", "العلامة", "테스트"]}
            ]
            self.assertEqual(result, expected)   
    def test_tag_conversion(self):
        test_cases = [
            ("Hello World!", "hello_world"),
            ("TaG1!!!", "tag1"),
            ("résumé", "resume"),
            ("  spaces  ", "spaces"),
            ("multiple___spaces", "multiple_spaces"),
            ("!@#$%^", ""),  # How should empty results be handled?
            ("漢字", "")
        ]
        
        for input_tag, expected in test_cases:
            result = convert_tag(input_tag)
            self.assertEqual(result, expected)   
    def test_tag_edge_cases(self):
        test_cases = [
            # Empty inputs
            ("", ""),
            (" ", ""),
            
            # Just special characters
            ("@#$", ""),
            ("___", ""),
            
            # Numbers only
            ("123", "123"),
            
            # Mixed case with multiple spaces/specials
            ("Hello   World!!!___", "hello_world"),
            
            # Unicode spaces and separators
            ("\u2002\u2003Hello\u2002World\u2002", "hello_world"),
            
            # Emojis and symbols
            ("👋 Hello 🌍", "hello"),
            
            # Non-breaking spaces
            ("Hello\u00A0World", "hello_world"),
            
            # Control characters
            ("Hello\n\tWorld", "hello_world")
        ]
        
        for input_tag, expected in test_cases:
            result = convert_tag(input_tag)
            self.assertEqual(result, expected)  
    def test_tag_length(self):
        test_cases = [
            # Exactly 64 chars
            ("a" * 64, "a" * 64),
            
            # More than 64 chars
            ("a" * 100, "a" * 64),
            
            # Long string with spaces and special chars
            # "hello_" is 6 chars, so we can fit 10 complete "hello_" (60 chars)
            # plus "hell" (4 chars) to make 64 total
            ("Hello " * 20, ("hello_" * 10) + "hell"),
            
            # Long unicode that converts to shorter ASCII
            ("é" * 100, "e" * 64)
        ]
        
        for input_tag, expected in test_cases:
            result = convert_tag(input_tag)
            self.assertEqual(result, expected)
            self.assertLessEqual(len(result), 64)

    def test_convert_csv(self):
        input_data = """Email,Tags,Name,Country
    email@test.com,"Python, Coding",John,US
    other@test.com,"python, Gaming",Jane,UK
    third@test.com,CODING,Bob,CA"""
        
        expected_headers = ["email", "name", "country", "tag:coding", "tag:gaming", "tag:python"]
        expected_rows = [
            ["email@test.com", "John", "US", "1", "0", "1"],
            ["other@test.com", "Jane", "UK", "0", "1", "1"],
            ["third@test.com", "Bob", "CA", "1", "0", "0"]
        ]
        
        result_headers, result_rows = convert_csv(input_data)
        self.assertEqual(result_headers, expected_headers)
        self.assertEqual(result_rows, expected_rows)          
if __name__ == '__main__':
    unittest.main()
