from textnode import *
from htmlnode import *
from main import *
from regexes import *

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



def split_nodes_image(old_nodes):

    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
                
        extract = extract_markdown_images(old_node.text)

        if len(extract)==0:
            new_nodes.append(old_node)
            continue
            
            
        remaining_text = old_node.text
            
        for tup in extract:
            alt_text = tup[0]
            url = tup[1]
            full_text = "![{}]({})".format(alt_text,url)
            
            section = remaining_text.split(full_text,1)
            
            if section[0] != "":
                new_nodes.append(TextNode(section[0],TextType.TEXT))
                
            new_nodes.append(TextNode(alt_text,TextType.IMAGE,url))
            if len(section) > 1:
                remaining_text = section[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))            
        
    return new_nodes

def split_nodes_link(old_nodes):

    new_nodes = []
    
    for old_node in old_nodes:
        
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
    
        extract = extract_markdown_links(old_node.text)
        

        if len(extract)==0:
            new_nodes.append(old_node)
            continue
            
            
        remaining_text = old_node.text
            
        for tup in extract:
            alt_text = tup[0]
            url = tup[1]
            full_text = "[{}]({})".format(alt_text,url)
            
            section = remaining_text.split(full_text,1)
            
            if section[0] != "":
                new_nodes.append(TextNode(section[0],TextType.TEXT))
                
            new_nodes.append(TextNode(alt_text,TextType.LINK,url))
            if len(section) > 1:
                remaining_text = section[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
        
    return new_nodes    
    
    
def text_to_textnodes(text):
    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split by each delimiter in sequence
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Now handle special cases like images and links
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    
    return nodes