#!/usr/bin/python3
"""Program entry"""

import cmd
import models
from models.base_model import BaseModel
import shlex

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

    def do_create(self, args):
        """ Create an object"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        """print str rep of an instance"""
        ls = shlex.split(arg)
        if len(ls) == 0:
            print("** class name missing **")
            return False
        if ls[0] in classes:
            if len(ls) > 1:
                k = ls[0] + "." + ls[1]
                if k in models.storage.all():
                    print(models.storage.all()[k])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def destroy():
        """Delete instances"""
        ...

    def all():
        """prints all"""
        ...

    def update():
        """updates instances"""
        ...


if __name__ == '__main__':
    HBNBCommand().cmdloop()
