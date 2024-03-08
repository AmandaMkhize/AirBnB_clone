#!/usr/bin/python3
"""Command interpreter for Airbnb Clone"""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel and saves it to JSON file"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        try:
            new_instance = eval(arg[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        if len(arg) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all()[arg[0] + "." + arg[1]]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        if len(arg) < 2:
            print("** instance id missing **")
            return
        try:
            del storage.all()[arg[0] + "." + arg[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        objs = []
        if arg:
            if arg not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if arg in key:
                    objs.append(str(value))
        else:
            for obj in storage.all().values():
                objs.append(str(obj))
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split()
        if len(arg) < 2:
            print("** instance id missing **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        try:
            obj = storage.all()[arg[0] + "." + arg[1]]
        except KeyError:
            print("** no instance found **")
            return
        setattr(obj, arg[2], arg[3])
        obj.save()

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

