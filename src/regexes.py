import re

def extract_markdown_images(text):
    alt_text = re.findall(r"!\[(.*?)\]",text)
    url = re.findall(r"\((.*?)\)",text)
    
    if len(alt_text)!=len(url):
        raise Exception("URL/Alt Text missmatch. Check text format to make sure if follows the ![alt_text](url) format")
    
    l_of_tups = []
    for i in range(len(alt_text)):
        l_of_tups.append((alt_text[i],url[i]))
    
    return l_of_tups



text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

assert extract_markdown_images(text) == [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
