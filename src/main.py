from textnode import *
from htmlnode import *
from copy_to_public import *
from page_generator import *
from recursive_pages import *

# Not because it is easy, but because it is hard


def main():
        copy_to_public()
        generate_pages_recursive("./content", "./template.html", "./public")
main()
