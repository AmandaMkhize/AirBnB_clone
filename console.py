#!/usr/bin/python3
"""Command interpreter module."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 
    'User': User, 
    'State': State, 
    'City': City, 
    'Amenity': Amenity, 
    'Place': Place, 
    'Review': Review
}

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg in classes:
            print([str(obj) for obj in storage.all()[arg].values()])
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        print(len(storage.all()[class_name]))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attribute_dict = eval(args[2])
        for k, v in attribute_dict.items():
            setattr(instance, k, v)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

