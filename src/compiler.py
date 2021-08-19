from parser import Parser
from files import parse_file 

def compile(file):
    content, content_lines = parse_file(file)
    parser = Parser(content, content_lines)
    result = parser.parse()

    new_file = file.split(".")
    new_file[-1] = "c"
    new_file = ".".join(new_file)

    f = open(new_file, "w")
    f.write(result)
    f.close()
