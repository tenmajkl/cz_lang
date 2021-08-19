import commands
import compiler

def run(args):
    command = commands.commands[args[1]][0]
    arguments = args[2:]
    eval(f"{command}({arguments})")
