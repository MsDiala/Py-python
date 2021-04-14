# Python Inheritance
## Introduction

Object-oriented programming creates reusable patterns of code to curtail redundancy in development projects. One way that object-oriented programming achieves recyclable code is through inheritance, when one subclass can leverage code from another base class.

This tutorial will go through some of the major aspects of inheritance in Python, including how parent classes and child classes work, how to override methods and attributes, how to use the `super()` function, and how to make use of multiple inheritance.
## What Is Inheritance?

**Inheritance** is when a class uses code constructed within another class. If we think of inheritance in terms of biology, we can think of a child inheriting certain traits from their parent. That is, a child can inherit a parent’s height or eye color. Children also may share the same last name with their parents.

Classes called **child classes** or **subclasses** inherit methods and variables from **parent classes** or **base classes**.

We can think of a parent class called `Parent` that has class variables for `last_name`, `height`, and `eye_color` that the child class `Child` will inherit from the `Parent`.

Because the `Child` subclass is inheriting from the `Parent` base class, the `Child` class can reuse the code of `Parent`, allowing the programmer to use fewer lines of code and decrease redundancy.

## Parent Classes

Parent or base classes create a pattern out of which child or subclasses can be based on. Parent classes allow us to create child classes through inheritance without having to write the same code over again each time. Any class can be made into a parent class, so they are each fully functional classes in their own right, rather than just templates.

Let’s say we have a general `Bank_account` parent class that has `Personal_account` and `Business_account` child classes. Many of the methods between personal and business accounts will be similar, such as methods to withdraw and deposit money, so those can belong to the parent class of `Bank_account`. The `Business_account` subclass would have methods specific to it, including perhaps a way to collect business records and forms, as well as an `employee_identification_number` variable.

Similarly, an `Animal` class may have `eating()` and `sleeping()` methods, and a `Tiger` subclass may include its own specific `roaring()` and `hunting()` methods.

Let’s create a Hunter parent class that we will later use to construct types of hunters as its subclasses. Each of these hunter will have first names and last names in addition to characteristics.

We’ll create a new file called `hunter.py` and start with the `__init__()` constructor method, which we’ll populate with `first_name` and `last_name` class variables for each hunter object or subclass.
###### hunter.py
```python
class Hunter:
    def __init__(self, first_name, last_name="tiger"):
        self.first_name = first_name
        self.last_name = last_name
```
We have initialized our `last_name` variable with the string `"tiger"`.

Let’s also add some other methods:
###### hunter.py
```python
class Hunter:
    def __init__(self, first_name, last_name="tiger"):
        self.first_name = first_name
        self.last_name = last_name

    def stealth(self):
        print("The hunter is hiding for a hunt.")

    def hunt(self):
        print("The hunter started it's hunt.")
```
We have added the methods `stealth()` and `hunt()` to the `Hunter` class, so that every subclass will also be able to make use of these methods.

Since most of the hunter we’ll be creating are considered to be water hunter (such as sharks and crocodiles) rather than land hunter(such as tiger,lions etc.,), we can add a few more attributes to the `__init__()` method:
###### hunter.py
```python
class Hunter:
    def __init__(self, first_name, last_name="Tiger",
                 geography="land",stealth = True):
        self.first_name = first_name
        self.last_name = last_name
        self.geography = geography
        self.stealth = stealth

        def stealth(self):
            print("The hunter is hiding for a hunt.")

        def hunt(self):
            print("The hunter started it's hunt.")

```
Building a parent class follows the same methodology as building any other class, except we are thinking about what methods the child classes will be able to make use of once we create those.
## Child Classes

Child or subclasses are classes that will inherit from the parent class. That means that each child class will be able to make use of the methods and variables of the parent class.

For example, a Bengaltiger child class that subclasses the Hunter class will be able to make use of the `stealth()` method declared in Hunter without needing to declare it.

We can think of each child class as being a class of the parent class. That is, if we have a child class called Rhombus and a parent class called Parallelogram, we can say that a Rhombus is a Parallelogram, just as a Bengaltiger is a Hunter.

The first line of a child class looks a little different than non-child classes as you must pass the parent class into the child class as a parameter:
```python
class Bengaltiger(Hunter):
```
The `Bengaltiger` class is a child of the `Hunter` class. We know this because of the inclusion of the word Hunter in parentheses.

With child classes, we can choose to add more methods, override existing parent methods, or simply accept the default parent methods with the pass keyword, which we’ll do in this case:
###### hunter.py
```python
...
class Bengaltiger(Hunter):
    pass
```
We can now create a Trout object without having to define any additional methods.
###### hunter.py
```python
...
class Bengaltiger(Hunter):
    pass

terry = Bengaltiger("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.geography)
print(terry.stealth)
terry.stealth()
terry.hunt()
```
We have created a `Bengaltiger` object `terry` that makes use of each of the methods of the `Hunter` class even though we did not define those methods in the `Bengaltiger` child class. We only needed to pass the value of `"Terry"` to the `first_name` variable because all of the other variables were initialized.

When we run the program, we’ll receive the following output:

Output
Terry Tiger
land
True
The hunter is hiding for a hunt.
The hunter started it's hunt.

Next, let’s create another child class that includes its own method. We’ll call this class `Javantiger`, and its special method will permit it to live with Bengaltiger:
###### hunter.py
```python
...
class Javantiger(Hunter):

    def live_with_Bengaltiger(self):
        print("The Javan tiger is coexisting with Bengal tiger.")
```
Next, let’s create a `Javantiger` object to see how this works:
###### hunter.py
```python
...
casey = Javantiger("Casey")
print(casey.first_name + " " + casey.last_name)
casey.stealth()
casey.live_with_Bengaltiger()
```
When we run the program, we’ll receive the following output:
```python
Output
Casey Tiger
The hunter is hiding for a hunt.
The Javan tiger is coexisting with Bengal tiger.
```
The output shows that the `Javantiger` object casey is able to use the `Hunter` methods `__init__()` and `stealth()` as well as its child class method of `live_with_Bengaltiger()`.

If we try to use the `live_with_Bengaltiger()` method in a `Bengaltiger` object, we’ll receive an error:
```python
Output
terry.live_with_Bengaltiger()
AttributeError: 'Bengaltiger' object has no attribute 'live_with_Bengaltiger'
```
This is because the method `live_with_Bengaltiger()` belongs only to the `Javantiger` child class, and not the `Hunter` parent class.

Child classes inherit the methods of the parent class it belongs to, so each child class can make use of those methods within programs.
## Overriding Parent Methods

So far, we have looked at the child class Trout that made use of the pass keyword to inherit all of the parent class `Hunter` behaviors, and another child class `Javantiger` that inherited all of the parent class behaviors and also created its own unique method that is specific to the child class. Sometimes, however, we will want to make use of some of the parent class behaviors but not all of them. When we change parent class methods we override them.

When constructing parent and child classes, it is important to keep program design in mind so that overriding does not produce unnecessary or redundant code.

We’ll create a `Shark` child class of the `Hunter` parent class. Because we created the `Hunter` class with the idea that we would be creating primarily land hunter, we’ll have to make adjustments for the `Shark` class that is instead a water hunter. In terms of program design, if we had more than one land hunter, we would most likely want to make separate classes for each of these two types of hunters.

Sharks, unlike land hunter,do not have stealth mode for them. They also have geography as water and are unable to move on land.

In light of this, we’ll be overriding the `__init__()` constructor method and the `stealth()` method. We don’t need to modify the `hunt()` method since sharks are hunters that can hunt in water. Let’s take a look at this child class:
###### hunter.py
```python
...
class Shark(Hunter):
    def __init__(self, first_name, last_name="Shark",
                 geography='water', stealth=False):
        self.first_name = first_name
        self.last_name = last_name
        self.geography = geography
        self.stealth = stealth

    def stealth(self):
        print("The shark cannot perform stealth actions.")
```
We have overridden the initialized parameters in the `__init__()` method, so that the last_name variable is now set equal to the string `"Shark"`, the `geography` variable is now set equal to the string `"water"`, and the `stealth` variable is now set to the Boolean value `False`. Each instance of the class can also override these parameters.

The method `stealth()` now prints a different string than the one in the Hunter parent class because sharks are not able to perform stealth actions as land hunters.

We can now create an instance of the `Shark` child class, which will still make use of the `stealth()` method of the Hunter parent class:
###### hunter.py
```python
...
sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.hunt()
sammy.stealth()
print(sammy.geography)
print(sammy.stealth)
```
When we run this code, we’ll receive the following output:
```python
Output
Sammy Shark
The hunter started it's hunt.
The shark cannot perform stealth actions.
water
False
```
The Shark child class successfully override the `__init__()` and `stealth()` methods of the `Hunter` parent class, while also inheriting the `hunt()` method of the parent class.

When there will be a limited number of child classes that are more unique than others, overriding parent class methods can prove to be useful.
## The super() Function

With the `super()` function, you can gain access to inherited methods that have been overwritten in a class object.

When we use the `super()` function, we are calling a parent method into a child method to make use of it. For example, we may want to override one aspect of the parent method with certain functionality, but then call the rest of the original parent method to finish the method.

The `super()` function is most commonly used within the `__init__()` method because that is where you will most likely need to add some uniqueness to the child class and then complete initialization from the parent.

To see how this works, let’s modify our `Bengaltiger` child class. Since Bengaltiger are typically Indian region specific, let’s add a `region` variable to the `__init__()` method and set it equal to the string "India", but then maintain the rest of the parent class’s variables and parameters:
###### hunter.py
```python
...
class Bengaltiger(Hunter):
    def __init__(self, region = "India"):
        self.region = region
        super().__init__(self)
...
```
We have overridden the `__init__()` method in the `Bengaltiger` child class, providing a different implementation of the `__init__()` that is already defined by its parent class `Hunter`. Within the `__init__()` method of our `Bengaltiger` class we have explicitly invoked the `__init__()` method of the `Hunter` class.

Because we have overridden the method, we no longer need to pass `first_name` in as a parameter to `Bengaltiger`, and if we did pass in a parameter, we would reset India region instead. We will therefore initialize the `first_name` by calling the variable in our object instance.

Now we can invoke the initialized variables of the parent class and also make use of the unique child variable. Let’s use this in an instance of Trout:
###### hunter.py
```python
...
terry = Bengaltiger()

# Initialize first name
terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.stealth)

# Use child __init__() override
print(terry.region)

# Use parent swim() method
terry.stealth()
```
```python
Output
Terry Tiger
True
India`
The hunter is hiding for a hunt.
```
The output shows that the object terry of the `Bengaltiger` child class is able to make use of both the child-specific `__init__()` variable `region` while also being able to call the `Hunter` parent `__init__()` variables of `first_name`, `last_name`, and `stealth`.

The built-in Python function `super()` allows us to utilize parent class methods even when overriding certain aspects of those methods in our child classes.
## Multiple Inheritance

Multiple inheritance is when a class can inherit attributes and methods from more than one parent class. This can allow programs to reduce redundancy, but it can also introduce a certain amount of complexity as well as ambiguity, so it should be done with thought to overall program design.

To show how multiple inheritance works, let’s create a `Coral_reef` child class than inherits from a `Coral` class and a `Sea_anemone` class. We can create a method in each and then use the pass keyword in the `Coral_reef` child class:
###### coral_reef.py
```python
class Coral:

    def community(self):
        print("Coral lives in a community.")


class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Coral, Anemone):
    pass
```
The `Coral` class has a method called `community()` that prints one line, and the `Anemone` class has a method called `protect_clownfish()` that prints another line. Then we call both classes into the inheritance tuple. This means that `Coral` is inheriting from two parent classes.

Let’s now instantiate a Coral object:
###### coral_reef.py
```python
...
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()
```
The object `great_barrier` is set as a `CoralReef` object, and can use the methods in both parent classes. When we run the program, we’ll see the following output:
```python
Output
Coral lives in a community.
The anemone is protecting the clownfish.
```
The output shows that methods from both parent classes were effectively used in the child class.

Multiple inheritance allows us to use the code from more than one parent class in a child class. If the same method is defined in multiple parent methods, the child class will use the method of the first parent declared in its tuple list.

Though it can be used effectively, multiple inheritance should be done with care so that our programs do not become ambiguous and difficult for other programmers to understand.
