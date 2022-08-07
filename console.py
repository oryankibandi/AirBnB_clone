#!/usr/bin/python3
"""Program entry"""

import cmd
from models.__init__ import storage
from models.base_model import BaseModel
import shlex

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """The console class"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}

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
        nw_instance = HBNBCommand.classes[args]()
        storage.save()
        print(nw_instance.id)
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
                if k in storage.all():
                    print(storage.all()[k])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete instances"""
        ls = shlex.split(arg)
        if len(ls) == 0:
            print("** class name missing **")
        elif ls[0] in classes:
            if len(ls) > 1:
                k = ls[0] + "." + ls[1]
                if k in storage.all():
                    storage.all().pop(k)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints all"""
        ls_args = shlex.split(arg)
        ls_obj = []
        if len(ls_args) == 0:
            dct_obj = storage.all()
        elif ls_args[0] in classes:
            dct_obj = storage.all(classes[ls_args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for k in dct_obj:
            ls_obj.append(str(dct_obj[k]))
        print("[" + (", ".join(ls_obj)) + "]")

    def do_update():
        """updates instances"""
        ...


if __name__ == '__main__':
    HBNBCommand().cmdloop()
