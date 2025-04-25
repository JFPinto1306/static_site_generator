import unittest
from extract_title_from_markdown import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_one_header(self):
        text = "# This is a title"
        title = extract_title(text)
        self.assertEqual(title, "This is a title")
        
    def test_multiple_headers(self):
        text = "# This is a title\n## This is a subtitle"
        title = extract_title(text)
        self.assertEqual(title, "This is a title")
    def test_no_header(self):
        text = "This is a title"
        with self.assertRaises(Exception):
            extract_title(text)
    def test_empty_string(self):
        text = ""
        with self.assertRaises(Exception):
            extract_title(text)
            
    def test_multiple_header(self):
        text = "### This is not a header"
        with self.assertRaises(Exception):
            extract_title(text)
    
