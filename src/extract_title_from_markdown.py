
def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line[0]=='#' and line[1] != '#':
            return line[2:].strip()
    raise Exception('No title found in markdown file')


