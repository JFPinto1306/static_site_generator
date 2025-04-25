from textnode import *
from htmlnode import *
from copy_to_public import *
from page_generator import *
from recursive_pages import *
import sys
# Not because it is easy, but because it is hard

basepath = '/'

if sys.argv:
        basepath = sys.argv[0]
        
        

def main():
        copy_to_public()
        generate_pages_recursive(basepath,"./content", "./template.html", "./docs")
main()
