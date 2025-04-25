from textnode import *
from htmlnode import *
from copy_to_public import *
from page_generator import *
from recursive_pages import *
import sys
# Not because it is easy, but because it is hard

# Default basepath
basepath = '/'

# Check if command-line arguments were provided
if len(sys.argv) > 1:
    basepath = sys.argv[1]  # The first argument is at index 1, not 0
        

def main():
        copy_to_public()
        generate_pages_recursive(basepath,"./content", "./template.html", "./docs")
main()
