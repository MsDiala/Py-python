# **Reading and Writing Files in Python**
## Overview
-----
When you’re working with Python, you don’t need to import a library in order to read and write files. It’s handled natively in the language.

The first thing you’ll need to do is use Python’s built-in `open` function to get a *file object*.

`File objects` contain methods and attributes that can be used to collect information about the file you opened. They can also be used to manipulate said file.

## Overview
-----
In Python, a file is categorized as either text or binary, and the difference between the two file types is important.

Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax.

Each line is terminated with a special character, called the EOL or End of Line character. There are several types, but the most common is the comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun.

A backslash character can also be used, and it tells the interpreter that the next character – following the slash – should be treated as a new line. This character is useful when you don’t want to start a new line in the text itself but in the code.

A binary file is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that know or understand the file’s structure. In other words, they must be applications that can read and interpret binary.
## `open()` function
In order to open a file for writing or use in Python, you must rely on the built-in `open()` function.

 `open()` will return a file object, so it is most commonly used with two arguments.

 An argument is nothing more than a value that has been provided to a function, which is relayed when you call it. So, for instance, if we declare the name of a file as “Test File,” that name would be considered an argument.

 The syntax to open a file object in Python is:
 ```python
file_object  = open(“filename”, “mode”) #where file_object is the variable to add the file object.
 ```
 The second argument you see – mode – tells the interpreter and developer which way the file will be used.
## Mode
------
Including a mode argument is optional because a default value of ‘r’ will be assumed if it is omitted. The ‘r’ value stands for read mode, which is just one of many.

The modes are:

- ‘r’ – Read mode which is used when the file is only being read
- ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
- ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
- ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file

So, let’s take a look at a quick example.
```python
F = open(“workfile”,”w”)
Print F
```
This snippet opens the file named “workfile” in writing mode so that we can make changes to it. The current information stored within the file is also displayed – or printed – for us to view.

Once this has been done, you can move on to call the objects functions. The two most common functions are read and write.
## Create a text file
To get more familiar with text files in Python, let’s create our own and do some additional exercises.

Using a simple text editor, let’s create a file. You can name it anything you like, and it’s better to use something you’ll identify with.

For the purpose of this tutorial, however, we are going to call it “testfile.txt”.

Just create the file and leave it blank.

To manipulate the file, write the following in your Python environment (you can copy and paste if you’d like):
```python
file = open(“testfile.txt”,”w”)

file.write(“Hello World”)
file.write(“This is our new text file”)
file.write(“and this is another line.”)
file.write(“Why? Because we can.”)

file.close()
```
Naturally, if you open the text file – or look at it – using Python you will see only the text we told the interpreter to add.
```bash
$ cat testfile.txt
Hello World
This is our new text file
and this is another line.
Why? Because we can.

```
## Reading a Text File in Python
There are actually a number of ways to read a text file in Python, not just one.

If you need to extract a string that contains all characters in the file, you can use the following method:

```python
file.read()
```
The full code to work with this method will look something like this:
```python
file = open(“testfile.text”, “r”)
print file.read()
```
The output of that command will display all the text inside the file, the same text we told the interpreter to add earlier. There’s no need to write it all out again, but if you must know, everything will be shown except for the “$ cat testfile.txt” line.



Another way to read a file is to call a certain number of characters.  

For example, with the following code the interpreter will read the first five characters of stored data and return it as a string:
```python
file = open(“testfile.txt”, “r”)

print file.read(5)
```
Notice how we’re using the same file.read() method, only this time we specify the number of characters to process?

The output for this will look like:
```python
Hello
```
If you want to read a file line by line – as opposed to pulling the content of the entire file at once – then you use the readline() function.

Why would you use something like this?

Let’s say you only want to see the first line of the file – or the third. You would execute the readline() function as many times as possible to get the data you were looking for.

Each time you run the method, it will return a string of characters that contains a single line of information from the file.
```python
file = open(“testfile.txt”, “r”)
print file.readline()
```
output:
```
Hello World
```
If we wanted to return only the third line in the file, we would use this:
```python
file = open(“testfile.txt”, “r”)
print file.readline(3)
```
But what if we wanted to return every line in the file, properly separated? You would use the same function, only in a new form. This is called the `file.readlines()` function.
```python
file = open(“testfile.txt”, “r”)
print file.readlines()
```

The output you would get from this is:
```
[‘Hello World’, ‘This is our new text file’, ‘and this is another line.’, ‘Why? Because we can.’]
```
## Looping over a file object
When you want to read – or return – all the lines from a file in a more memory efficient, and fast manner, you can use the loop over method. The advantage to using this method is that the related code is both simple and easy to read.
```python
file = open(“testfile.txt”, “r”)
for line in file:
print line,
```

This will return:
```
Hello World
This is our new text file
and this is another line.
Why? Because we can.
```

## Using the File Write Method
-----
One thing you’ll notice about the file write method is that it only requires a single parameter, which is the string you want to be written.

This method is used to add information or content to an existing file. To start a new line after you write data to the file, you can add an EOL character.

```python
file = open(“testfile.txt”, “w”)

file.write(“This is a test”)
file.write(“To add more lines.”)

file.close()
```

Obviously, this will amend our current file to include the two new lines of text. There’s no need to show output.

## Closing a File
-----
When you’re done working, you can use the `fh.close()` command to end things. What this does is close the file completely, terminating resources in use, in turn freeing them up for the system to deploy elsewhere.

It’s important to understand that when you use the `fh.close()` method, any further attempts to use the file object will fail.

Notice how we have used this in several of our examples to end interaction with a file? This is good practice.
