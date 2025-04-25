import os 
from page_generator import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for path in os.listdir(dir_path_content):
        dir_path_content_full = os.path.join(dir_path_content, path)
        print("Full Path: ",dir_path_content_full)
        if os.path.isdir(dir_path_content_full):
            # If the path is a directory, recursively call the function
            generate_pages_recursive(dir_path_content_full, template_path, os.path.join(dest_dir_path+'/'+path))
        elif os.path.isfile(dir_path_content_full):
            # If the path is a file, generate the page
            os.makedirs(dest_dir_path, exist_ok=True)
            generate_page(dir_path_content_full, template_path, os.path.join(dest_dir_path+'/'+path.replace('.md', '.html')))
            
