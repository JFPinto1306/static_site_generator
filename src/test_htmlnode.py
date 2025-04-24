from htmlnode import *
import unittest


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class="container" id="main"')
        
    def test_empty_props_to_html(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), '')
        
    def test_props_to_html_random_worder(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class="container" id="main"')
    
    def test_none_props_to_html(self):
        node = HTMLNode(tag="div", props=None)
        self.assertEqual(node.props_to_html(), '')
    
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", props={"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div,Hello,None,{'class': 'container'})")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_props(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node2, '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_multiple_props(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com","class":"container"}).to_html()
        self.assertEqual(node2, '<a href="https://www.google.com" class="container">Click me!</a>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        
        
    # Test cases for ParentNode
    def test_parent_to_html_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("span", "text")])
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_parent_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_parent_to_html_empty_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_to_html_with_valid_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        assert parent_node.to_html() == "<div><span>child</span></div>"

    def test_to_html_missing_tag(self):
        try:
            ParentNode(None, [LeafNode("span", "text")])
        except ValueError as e:
            assert str(e) == "All parent nodes must have a tag"

    def test_to_html_empty_children(self):
        try:
            ParentNode("div", [])
        except ValueError as e:
            assert str(e) == "All parent nodes must have children"

    def test_to_html_invalid_child_type(self):
        try:
            ParentNode("div", ["I am not a node"])
        except ValueError as e:
            assert str(e) == "Children must be either LeafNode or ParentNode"

    def test_to_html_non_list_children(self):
        try:
            ParentNode("div", None)
        except ValueError as e:
            assert str(e) == "Children must be a list of LeafNode or ParentNode"
            

        
    
