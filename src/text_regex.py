from regexes import *
import unittest

class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
        
    def test_extract_markdown_links_no_link(self):
        matches = extract_markdown_links(
            "This is text with a [link]without a link"
        )
        self.assertListEqual([], matches)
        
    def test_extract_markdown_links_no_text(self):
        matches = extract_markdown_links(
            "This is text with a []()"
        )
        self.assertListEqual([], matches)
    
    
    
