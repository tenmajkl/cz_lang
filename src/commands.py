commands = {
        "-h": ["commands.help_command", "List of all commands"],
        "-c": ["compiler.compile", "Compiles code to executable"],
        "-t": ["compiler.to_c", "Compiles code to c-code"]
}

def help_command(argumnets):
    for command in commands.keys():
        print(f"{command} - {commands[command][1]}")
