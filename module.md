# Modules in python
## Introduction

Python modules are .py files that consist of Python code. Any Python file can be referenced as a module.

Some modules are available through the Python Standard Library and are therefore installed with your Python installation. Others can be installed with Python’s package manager pip. Additionally, you can create your own Python modules since modules are comprised of Python .py files.

This tutorial will guide you through writing Python modules for use within other programming files.
Writing and Importing Modules

Writing a module is just like writing any other Python file. Modules can contain definitions of functions, classes, and variables that can then be utilized in other Python programs.

From our Python 3 local programming environment or server-based programming environment, let’s start by creating a file hello.py that we’ll later import into another file.

To begin, we’ll create a function that prints Hello, World!:
###### hello.py
```python
# Define a function
def hi():
    print("Hello, World!")
```
If we run the program on the command line with python `hello.py` nothing will happen since we have not told the program to do anything.

Let’s create a second file in the same directory called `main.py` so that we can import the module we just created, and then call the function. This file needs to be in the same directory so that Python knows where to find the module since it’s not a built-in module.
###### main.py
```python
# Import hello module
import hello


# Call function
hello.hi()
```
Because we are importing a module, we need to call the function by referencing the module name in dot notation.

We could instead import the module as from `hello import hi` and call the function directly as `hi()`. You can learn more about this method by reading how to using `from ... import` when importing modules.

Now, we can run the program on the command line:
```bash
    python main.py
```
When we do, we’ll receive the following output:
```bash
Output
Hello, World!
```
To see how we can use variables in a module, let’s add a variable definition in our `hello.py` file:
###### hello.py
```python
# Define a function
def hi():
    print("Hello, World!")

# Define a variable
tiger = "Sagar"
```
Next, we’ll call the variable in a print() function within our `main.py` file:
###### main.py
```python
# Import hello module
import hello


# Call function
hello.hi()

# Print variable
print(hello.tiger)
```
Once we run the program again, we’ll receive the following output:
```bash
Output
Hello, World!
Sagar
```
Finally, let’s also define a class in the `hello.py` file. We’ll create the class `Bear` with name and color attributes and a function that will print out the attributes when called.
###### hello.py
```python
# Define a function
def hi():
    print("Hello, World!")

# Define a variable
tiger = "Sagar"


# Define a class
class Bear:
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def tell_me_about_the_bear(self):
        print("This bear is " + self.color + ".")
        print(self.name + " is the Bear's name.")
```
We’ll now add the class to the end of our `main.py` file:
###### main.py
```python
# Import hello module
import hello


# Call function
hello.hi()

# Print variable
print(hello.tiger)

# Call class
rr = hello.Bear("Grizzly", "Brown")
rr.tell_me_about_the_bear()
```
Once we have called the `Bear` class with `hello.Bear()`, we can access the functions and attributes of the class within the `main.py` file’s namespace. This lets us write `rr.tell_me_about_the_bear()` on the last line without invoking `hello`. We could also, for example, call one of the class’s attributes such as `rr.color` without referencing the name of the `hello` module.

When we run the program, we’ll receive the following output:
```bash
Output
Hello, World!
Sagar
This bear is Brown.
Grizzly is the Bear\'s name.
```
It is important to keep in mind that though modules are often definitions, they can also implement code. To see how this works, let’s rewrite our `hello.py` file so that it implements the `hi()` function:
###### hello.py
```python
# Define a function
def hi():
    print("Hello, World!")

# Call function within module
hi()
```
We have also deleted the other definitions in the file.

Now, in our `main.py` file, we’ll delete every line except for the import statement:
###### main.py
```python
# Import hello module
import hello
```
When we run `main.py` we’ll receive the following output:
```bash
Output
Hello, World!
```
This is because the `hello` module implemented the `hi()` function which is then passed to `main.py` and executes when `main.py` runs.

A module is a Python program file composed of definitions or code that you can leverage in other Python program files.
## Accessing Modules from Another Directory

Modules may be useful for more than one programming project, and in that case it makes less sense to keep a module in a particular directory that’s tied to a specific project.

If you want to use a Python module from a location other than the same directory where your main program is, you have a few options.
### Appending Paths

One option is to invoke the path of the module via the programming files that use that module. This should be considered more of a temporary solution that can be done during the development process as it does not make the module available system-wide.

To append the path of a module to another programming file, you’ll start by importing the sys module alongside any other modules you wish to use in your main program file.

The `sys` module is part of the Python Standard Library and provides system-specific parameters and functions that you can use in your program to set the path of the module you wish to implement.

For example, let’s say we moved the `hello.py` file and it is now on the path `/usr/rag/` while the `main.py` file is in another directory.

In our `main.py` file, we can still import the `hello` module by importing the `sys` module and then appending `/usr/rag/` to the path that Python checks for files.
###### main.py
```python
import sys
sys.path.append('/usr/rag/')

import hello
...
```
As long as you correctly set the path for the `hello.py` file, you’ll be able to run the `main.py` file without any errors and receive the same output as above when `hello.py` was in the same directory.
### Adding the Module to the Python Path

A second option that you have is to add the module to the path where Python checks for modules and packages. This is a more permanent solution that makes the module available environment-wide or system-wide, making this method more portable.

To find out what path Python checks, run the Python interpreter from your programming environment:
```bash
    python
```
Next, import the sys module:
```python
    import sys
```
Then have Python print out the system path:
```python
    print(sys.path)
```
Here, you’ll receive some output with at least one system path. If you’re in a programming environment, you may receive several. You’ll want to look for the one that is in the environment you’re currently using, but you may also want to add the module to your main system Python path. What you’re looking for will be similar to this:
```python
Output
'/usr/rag/my_env/lib/python3.5/site-packages'
```
Now you can move your `hello.py` file into that directory. Once that is complete, you can import the `hello` module as usual:
###### main.py
```python
import hello
...
```
When you run your program, it should complete without error.

Modifying the path of your module can ensure that you can access the module regardless of what directory you are in. This is useful especially if you have more than one project referencing a particular module.
