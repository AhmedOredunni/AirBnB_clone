#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Handle the commandline 
        integration of the website
    """
    base_model = BaseModel()
    prompt = "(hbnb) "

    def do_create(self, line):
        """Create and instance of the class Passed"""
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """Showed the String representation 
            of the instance with a given id. 
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")


    def do_all(self, line):
        """Prints all string representations 
            of instances based on the class name.
        """
        args = line.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                print([str(obj) for key, obj in objects.items()
                      if key.startswith(class_name)])

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    value = args[3]
                    obj = models.storage.all()[key]
                    setattr(obj, attribute_name, value)
                    models.storage.save()

    def do_EOF(self, line):
        """Use to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
