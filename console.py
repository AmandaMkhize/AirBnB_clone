#!/usr/bin/python3
"""
Contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage

# Delay reloading until after BaseModel has been imported
storage.reload()

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of File command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to JSON file, and print the ID"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, obj_id = arg.split()
            obj = storage.all()[class_name + '.' + obj_id]
            print(obj)
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, obj_id = arg.split()
            obj = storage.all()[class_name + '.' + obj_id]
            del storage.all()[class_name + '.' + obj_id]
            storage.save()
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = []
        if not arg:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
            return
        try:
            class_name = arg.split()[0]
            for key, obj in storage.all().items():
                if key.split('.')[0] == class_name:
                    objs.append(str(obj))
            print(objs)
        except KeyError:
            print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3].strip('"')
            obj = storage.all()[class_name + '.' + obj_id]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except ValueError:
            print("** value missing **")
        except AttributeError:
            print("** attribute name missing **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

