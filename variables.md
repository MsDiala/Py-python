# **Variables**

## Variables in Python
-----------

As the name implies, a variable is something which can change. A variable is a way of referring to a memory location used by a computer program. A variable is a symbolic name for this physical location. This memory location contains values, like numbers, text or more complicated types.

One of the main differences between Python and strongly-typed languages like C, C++ or Java is the way it deals with types. In strongly-typed languages every variable must have a unique data type. E.g. if a variable is of type integer, solely integers can be saved in the variable. In Java or C, every variable has to be declared before it can be used. Declaring a variable means binding it to a data type.

Declaration of variables is not required in Python. If there is need of a variable, you think of a name and start using it as a variable.

Another remarkable aspect of Python: Not only the value of a variable may change during program execution but the type as well. You can assign an integer value to a variable, use it as an integer for a while and then assign a string to the variable.

## Variables vs. Identifiers
------------

Variables and identifiers are very often mistaken as synonyms. In simple terms: The name of a variable is an identifier, but a variable is "more than a name". A variable has a name, in most cases a type, a scope, and above all a value. Besides this, an identifier is not only used for variables. An identifier can denote various entities like variables, types, labels, subroutines or functions, packages and so on.

## Global and Local Variables in Python
----------

Global variables are the one that are defined and declared outside a function and we need to use them inside a function.

```python
# This function uses global variable s
def code():
    print cl

# Global scope
cl = "I love Codelabs"
code()

```
output:

```bash
I love Codelabs
```

If a variable with same name is defined inside the scope of function as well then it will print the value given inside the function only and not the global value.
```python
# This function has a variable with
# name same as s.
def func():
    s = "I love learning."
    print s

# Global scope
s = "I love Codelabs"
f()
print s
```
Output:
```bash
I love learning.
I love Codelabs
```


## What are the rules for local and global variables in Python?
----------

In Python, variables that are only referenced inside a function are implicitly global. If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.

Though a bit surprising at first, a moment’s consideration explains this. On one hand, requiring `global` for assigned variables provides a bar against unintended side-effects. On the other hand, if `global` was required for all global references, you’d be using `global` all the time. You’d have to declare as global every reference to a built-in function or to a component of an imported module. This clutter would defeat the usefulness of the `global` declaration for identifying side-effects.
