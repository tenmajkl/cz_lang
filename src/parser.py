import re
from keywords import keywords

class Parser:
    def __init__(self, content:str, content_lines:list) -> None:
        self.content = content
        self.content_lines = content_lines

    def parse(self):
        result = ""
        for statement in self.content_lines:
            parsed_statement = self.parse_str(statement)
            statement = parsed_statement[0]
            strings = parsed_statement[1]
            for keyword in keywords.keys():
                statement = re.sub(keyword, keywords[keyword], statement)

            if statement.endswith(".\n"):
                statement = re.sub("\.\\n$", ";\n", statement)

            statement = self.reparse_str(statement, strings)
            result += statement

        return result

    def parse_str(self, statement):
        strings = re.findall("\"(.+)\"", statement)
        if len(strings) == 0:
            return [statement, {}]

        named_strings = {}
        for string in strings:
            name = f"CZ_STRING_{strings.index(string)}"
            named_strings[name] = string
            statement = re.sub(string, name, statement)


        return [statement, named_strings]


    def reparse_str(self, statement, strings):
        for string_name in strings.keys():
            statement = re.sub(string_name, strings[string_name], statement)

        return statement


