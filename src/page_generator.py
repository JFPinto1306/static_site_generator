from extract_title_from_markdown import extract_title
from markdown_blocks import markdown_to_html_node

def generate_page(basepath,from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Reading markdown
    with open(from_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        
        
    # Reading template
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()
        
    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()
    
    title = extract_title(md_content)
    
    # Replacing title in template
    template = template.replace("{{ Title }}", title)
    
    # Replacing content
    template = template.replace("{{ Content }}", html_string)
    
    # Replacing basepath
    template = template.replace('href="/', 'href="{basepath}/')
    template = template.replace('src="/', 'src="{basepath}/')
    
    # Writing full HTML page to dest path
    with open(dest_path, 'w', encoding='utf-8') as dest_file:
        dest_file.write(template)
        