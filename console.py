#!/usr/bin/python3
"""Program entry"""

import cmd
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """The console class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        exit()

    def do_help(self, arg):
        """Display help docs"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing...Override cmds
        emptyline method"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
