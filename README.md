# AirBnB Clone

This project involves writing a command interpreter for the AirBnB Clone project that will be used with the frontend, database storage, API and integration.

## Description

This command interpreter will help in the following tasks: 1. Create a new object 2. Retrieve an object from file 3. Do operations on objects 4. Update ttributes of an object 5. Destroy an object

A parent class called `BaseModel` tales care of initialiation, serialization and deserialization of future instances.

All classes used in AirBnB(User, State, City, Place) that inherit from `BaseModel' have been created.

An abstract storage engine writes class instances to a local file which persists data on reload.

Unittests in the `/tests` folder run checks on the class instances to validate that they have the required output.

### How to run

Run `console.py` in the

```bash
./console.py
```

A command interpreter will appear, type `help` to view available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

```

To view a command documentation, type `help` followed by the command;

```bash
(hbnb) help quit
Quit command to exit the program
```

### Creating an instance

In order to create an instance of `BaseModel` class use the `create` command followed by the name of the class.

```bash
(hbnb) create BaseModel
e25df7b6-9758-49ef-b2d7-8a6521afb914
```

This prints the id of the newly create instance.

### Deleting an instance

Use the `destroy` command to delete an instance. Pass the id of the instance to delete.

```bash
(hbnb) destroy BaseModel e25df7b6-9758-49ef-b2d7-8a6521afb914
(hbnb)
```

### Printing all instances

Use `all` to print string representation of all instances

```bash
(hbnb) all
["[BaseModel] (20e159c0-26e2-4953-bfaa-5ed0fc64506a) {'id': '20e159c0-26e2-4953-bfaa-5ed0fc64506a', 'created_at': datetime.datetime(2022, 8, 7, 23, 8, 27, 399371), 'updated_at': datetime.datetime(2022, 8, 7, 23, 8, 27, 399371)}"]
(hbnb)

```
