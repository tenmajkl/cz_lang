from parser import Parser
from files import parse_file 
import os

def to_c(arguments):
    print("Translating...")
    file = arguments[0]
    print("Parsing file...")
    content, content_lines = parse_file(file)
    parser = Parser(content, content_lines)
    print("Translating code..")
    result = parser.parse()
    
    print("Creating c file...")
    new_file = file.split(".")
    new_file[-1] = "c"
    new_file = ".".join(new_file)
    
    f = open(new_file, "w")
    f.write(result)
    f.close()
    print("Translated!")
    return new_file

def compile(arguments):
    file = to_c(arguments)
    print("Compiling...")
    new_file = file.split(".")
    new_file.pop(-1)
    new_file = ".".join(new_file)

    os.system(f"gcc {file} -o {new_file}")
    os.remove(file)
    print("Compiled!")

    return new_file

