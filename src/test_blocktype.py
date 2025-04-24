from blocktype import *
import unittest

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        text = "#This is a heading."
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_multiple_heading(self):
        text = "###This is a heading.\n#This is another heading."
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        text = "```python\nprint('Hello, World!')\n```"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.CODE)
    def test_quote(self):
        text = "> This is a quote."
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.QUOTE)
    def test_unordered_list(self):
        text = "- This is an unordered list item."
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    def test_ordered_list(self):
        text = "1. This is an ordered list item."
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
    def test_paragraph(self):
        text = "This is a paragraph."
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    def test_empty_string(self):
        text = ""
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    def test_whitespace_string(self):
        text = "   "
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
    def test_not_an_ordered_list(self):
        text= "2. This is not an ordered list item."
        block_type = block_to_block_type(text)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)
        
    def test_not_a_heading(self):
        text = "This ## is not a heading."
        block_type = block_to_block_type(text)
        self.assertNotEqual(block_type, BlockType.HEADING)
        
    def test_not_a_code(self):
        text = "```python\nprint('Hello, World!')"
        block_type = block_to_block_type(text)
        self.assertNotEqual(block_type, BlockType.CODE)
    def test_not_a_quote(self):
        text = "This is not a quote."
        block_type = block_to_block_type(text)
        self.assertNotEqual(block_type, BlockType.QUOTE)
    def test_not_an_unordered_list(self):
        text = "-This is not an unordered list item."
        block_type = block_to_block_type(text)
        self.assertNotEqual(block_type, BlockType.UNORDERED_LIST)
    def test_not_an_ordered_list(self):
        text = "1This is not an ordered list item."
        block_type = block_to_block_type(text)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)
    
