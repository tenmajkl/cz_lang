from Exceptions.InvalidFileFormat import InvalidFileFormat

def parse_file(file):
    if not file.endswith(".cz"):
        raise InvalidFileFormat("Invalid File Format! Only .cz supported!")

    f = open(file)
    content_lines = f.readlines()
    content = f.read()
    f.close()
    return [content, content_lines]

