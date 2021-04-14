Python provides two very important features to handle any unexpected error in your Python programs and to add debugging capabilities in them −

- Exception Handling − This would be covered in this tutorial. Here is a list standard Exceptions available in Python.
- Assertions − This would be covered in Assertions in Python tutorial.

List of Standard Exceptions −
<table>
<tr>
<th style="text-align:center;">Sr.No.</th>
<th style="text-align:center;">Exception Name &amp; Description</th>
</tr>
<tr>
<td class="ts">1</td>
<td><p><b>Exception</b></p>
<p>Base class for all exceptions</p></td>
</tr>
<tr>
<td class="ts">2</td>
<td><p><b>StopIteration</b></p>
<p>Raised when the next() method of an iterator does not point to any object.</p></td>
</tr>
<tr>
<td class="ts">3</td>
<td><p><b>SystemExit</b></p>
<p>Raised by the sys.exit() function.</p></td>
</tr>
<tr>
<td class="ts">4</td>
<td><p><b>StandardError</b></p>
<p>Base class for all built-in exceptions except StopIteration and SystemExit.</p></td>
</tr>
<tr>
<td class="ts">5</td>
<td><p><b>ArithmeticError</b></p>
<p>Base class for all errors that occur for numeric calculation.</p></td>
</tr>
<tr>
<td class="ts">6</td>
<td><p><b>OverflowError</b></p>
<p>Raised when a calculation exceeds maximum limit for a numeric type.</p></td>
</tr>
<tr>
<td class="ts">7</td>
<td><p><b>FloatingPointError</b></p>
<p>Raised when a floating point calculation fails.</p></td>
</tr>
<tr>
<td class="ts">8</td>
<td><p><b>ZeroDivisionError</b></p>
<p>Raised when division or modulo by zero takes place for all numeric types.</p></td>
</tr>
<tr>
<td class="ts">9</td>
<td><p><b>AssertionError</b></p>
<p>Raised in case of failure of the Assert statement.</p></td>
</tr>
<tr>
<td class="ts">10</td>
<td><p><b>AttributeError</b></p>
<p>Raised in case of failure of attribute reference or assignment.</p></td>
</tr>
<tr>
<td class="ts">11</td>
<td><p><b>EOFError</b></p>
<p>Raised when there is no input from either the raw_input() or input() function and the end of file is reached.</p></td>
</tr>
<tr>
<td class="ts">12</td>
<td><p><b>ImportError</b></p>
<p>Raised when an import statement fails.</p></td>
</tr>
<tr>
<td class="ts">13</td>
<td><p><b>KeyboardInterrupt</b></p>
<p>Raised when the user interrupts program execution, usually by pressing Ctrl+c.</p></td>
</tr>
<tr>
<td class="ts">14</td>
<td><p><b>LookupError</b></p>
<p>Base class for all lookup errors.</p></td>
</tr>
<tr>
<td class="ts">15</td>
<td><p><b>IndexError</b></p>
<p>Raised when an index is not found in a sequence.</p></td>
</tr>
<tr>
<td class="ts">16</td>
<td><p><b>KeyError</b></p>
<p>Raised when the specified key is not found in the dictionary.</p></td>
</tr>
<tr>
<td class="ts">17</td>
<td><p><b>NameError</b></p>
<p>Raised when an identifier is not found in the local or global namespace.</p></td>
</tr>
<tr>
<td class="ts">18</td>
<td><p><b>UnboundLocalError</b></p>
<p>Raised when trying to access a local variable in a function or method but no value has been assigned to it.</p></td>
</tr>
<tr>
<td class="ts">19</td>
<td><p><b>EnvironmentError</b></p>
<p>Base class for all exceptions that occur outside the Python environment.</p></td>
</tr>
<tr>
<td class="ts">20</td>
<td><p><b>IOError</b></p>
<p>Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.</p></td>
</tr>
<tr>
<td class="ts">21</td>
<td><p><b>IOError</b></p>
<p>Raised for operating system-related errors.</p></td>
</tr>
<tr>
<td class="ts">22</td>
<td><p><b>SyntaxError</b></p>
<p>Raised when there is an error in Python syntax.</p></td>
</tr>
<tr>
<td class="ts">23</td>
<td><p><b>IndentationError</b></p>
<p>Raised when indentation is not specified properly.</p></td>
</tr>
<tr>
<td class="ts">24</td>
<td><p><b>SystemError</b></p>
<p>Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.</p></td>
</tr>
<tr>
<td class="ts">25</td>
<td><p><b>SystemExit</b></p>
<p>Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.</p></td>
</tr>
<tr>
<td class="ts">26</td>
<td><p><b>TypeError</b></p>
<p>Raised when an operation or function is attempted that is invalid for the specified data type.</p></td>
</tr>
<tr>
<td class="ts">27</td>
<td><p><b>ValueError</b></p>
<p>Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.</p></td>
</tr>
<tr>
<td class="ts">28</td>
<td><p><b>RuntimeError</b></p>
<p>Raised when a generated error does not fall into any category.</p></td>
</tr>
<tr>
<td class="ts">29</td>
<td><p><b>NotImplementedError</b></p>
<p>Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.</p></td>
</tr>
</table>

## Assertions in Python
------
An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program.

The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised.

Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.

Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.
The assert Statement

When it encounters an assert statement, Python evaluates the accompanying expression, which is hopefully true. If the expression is false, Python raises an AssertionError exception.

The syntax for assert is −
```python
assert Expression[, Arguments]
```
If the assertion fails, Python uses ArgumentExpression as the argument for the `AssertionError`. AssertionError exceptions can be caught and handled like any other exception using the try-except statement, but if not handled, they will terminate the program and produce a traceback.
### Example

Here is a function that converts a temperature from degrees Kelvin to degrees Fahrenheit. Since zero degrees Kelvin is as cold as it gets, the function bails out if it sees a negative temperature −
```python
#!/usr/bin/python
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)
```
When the above code is executed, it produces the following result −

```python
32.0
451
Traceback (most recent call last):
File "test.py", line 9, in <module>
print KelvinToFahrenheit(-5)
File "test.py", line 4, in KelvinToFahrenheit
assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
```
## What is Exception?
----
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.

When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.
Handling an exception

If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.
Syntax

Here is simple syntax of `try....except...else` blocks −
```python
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
```
Here are few important points about the above-mentioned syntax −

- A single try statement can have multiple except statements. This is useful when the try block contains statements that may throw different types of exceptions.

- You can also provide a generic except clause, which handles any exception.

- After the except clause(s), you can include an else-clause. The code in the else-block executes if the code in the try: block does not raise an exception.

- The else-block is a good place for code that does not need the try: block's protection.

#### Example

This example opens a file, writes content in the, file and comes out gracefully because there is no problem at all −

```python
#!/usr/bin/python
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()
```
This produces the following result −

```python
Written content in the file successfully
```
Example

This example tries to open a file where you do not have write permission, so it raises an exception −
```python
#!/usr/bin/python

try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
```
This produces the following result −
```python
Error: can't find file or read data

The except Clause with No Exceptions
```
You can also use the except statement with no exceptions defined as follows −
```python
try:
   You do your operations here;
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
```
This kind of a try-except statement catches all the exceptions that occur. Using this kind of try-except statement is not considered a good programming practice though, because it catches all exceptions but does not make the programmer identify the root cause of the problem that may occur.
## The except Clause with Multiple Exceptions

You can also use the same except statement to handle multiple exceptions as follows −
```python
try:
   You do your operations here;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list,
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.
```
## The try-finally Clause

You can use a finally: block along with a try: block. The finally block is a place to put any code that must execute, whether the try-block raised an exception or not. The syntax of the try-finally statement is this −
```python
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
```
You cannot use else clause as well along with a finally clause.
Example

```python
#!/usr/bin/python
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print "Error: can\'t find file or read data"
```
If you do not have permission to open the file in writing mode, then this will produce the following result −
```python
Error: can't find file or read data
```
Same example can be written more cleanly as follows −
```python
#!/usr/bin/python

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"
```
When an exception is thrown in the try block, the execution immediately passes to the finally block. After all the statements in the finally block are executed, the exception is raised again and is handled in the except statements if present in the next higher layer of the *try-except* statement.
## Argument of an Exception

An exception can have an *argument*, which is a value that gives additional information about the problem. The contents of the argument vary by exception. You capture an exception's argument by supplying a variable in the except clause as follows −
```python
try:
   You do your operations here;
   ......................
except ExceptionType, Argument:
   You can print value of Argument here...
```
If you write the code to handle a single exception, you can have a variable follow the name of the exception in the except statement. If you are trapping multiple exceptions, you can have a variable follow the tuple of the exception.

This variable receives the value of the exception mostly containing the cause of the exception. The variable can receive a single value or multiple values in the form of a tuple. This tuple usually contains the error string, the error number, and an error location.
#### Example

Following is an example for a single exception −

```python
#!/usr/bin/python

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument
# Call above function here.
temp_convert("xyz");
```
This produces the following result −
```python
The argument does not contain numbers
invalid literal for int() with base 10: 'xyz'
```
## Raising an Exceptions

You can raise exceptions in several ways by using the raise statement. The general syntax for the raise statement is as follows.
Syntax
```python
raise [Exception [, args [, traceback]]]
```
Here, Exception is the type of exception (for example, `NameError`) and argument is a value for the exception argument. The argument is optional; if not supplied, the exception argument is None.

The final argument, traceback, is also optional (and rarely used in practice), and if present, is the traceback object used for the exception.
#### Example

An exception can be a string, a class or an object. Most of the exceptions that the Python core raises are classes, with an argument that is an instance of the class. Defining new exceptions is quite easy and can be done as follows −
```python
def functionName( level ):
   if level < 1:
      raise "Invalid level!", level
      # The code below to this would not be executed
      # if we raise the exception
```
**Note**: In order to catch an exception, an "except" clause must refer to the same exception thrown either class object or simple string. For example, to capture above exception, we must write the except clause as follows −
```python
try:
   Business Logic here...
except "Invalid level!":
   Exception handling here...
else:
   Rest of the code here...
```
## User-Defined Exceptions
----
Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions.

Here is an example related to RuntimeError. Here, a class is created that is subclassed from RuntimeError. This is useful when you need to display more specific information when an exception is caught.

In the try block, the user-defined exception is raised and caught in the except block. The variable e is used to create an instance of the class Networkerror.
```python
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
```
So once you defined above class, you can raise the exception as follows −
```python
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
```
