from textnode import *
from htmlnode import *
from main import *


def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
                return LeafNode(tag=None,value=text_node.text,props=None)
        if text_node.text_type == TextType.BOLD:
                return LeafNode(tag="b",value=text_node.text,props=None)
        if text_node.text_type == TextType.ITALIC:
                return LeafNode(tag="i",value=text_node.text,props=None)
        if text_node.text_type == TextType.CODE:
                return LeafNode(tag="code",value=text_node.text,props=None)
        if text_node.text_type == TextType.LINK:
                return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        if text_node.text_type == TextType.IMAGE:
                return LeafNode(tag="img",props={"src":text_node.url,"alt":text_node.text})
        
        raise Exception("Invalid text type")
        
### EVERYTHING BELOW THIS LINE IS FOR THE SPLIT NODES DELIM ###


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

