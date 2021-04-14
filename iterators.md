# Iterators
Iterators are objects that can be iterated upon. In this tutorial, you will learn how iterator works and how you can build your own iterator using `__iter__` and `__next__` methods.

## What are iterators in Python?

Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, `__iter__()` and `__next__()`, collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The `iter()` function (which in turn calls the `__iter__()` method) returns an iterator from them.

## Iterating Through an Iterator in Python

We use the `next()` function to manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise `StopIteration`. Following is an example.
```python
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next()

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)

```
output
```python
4
7
0
3

Traceback (most recent call last):
  File "<stdin>", line 24, in <module>
    next(my_iter)
StopIteration
```
Building Your Own Iterator in Python

Building an iterator from scratch is easy in Python. We just have to implement the methods `__iter__()` and `__next__()`.

The `__iter__()` method returns the iterator object itself. If required, some initialization can be performed.

The `__next__()` method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise `StopIteration`.

Here, we show an example that will give us next power of 3 in each iteration. Power exponent starts from zero up to a user set number.
```python
class PowThree:
    """Class to implement an iterator
    of powers of three"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 3 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
```
Now we can create an iterator and iterate through it as follows.
```python
>>> a = PowThree(4)
>>> i = iter(a)
>>> next(i)
1
>>> next(i)
3
>>> next(i)
9
>>> next(i)
27
>>> next(i)
81
>>> next(i)
Traceback (most recent call last):
...
StopIteration
```
## Python Infinite Iterators
-----
It is not necessary that the item in an iterator object has to exhaust. There can be infinite iterators (which never ends). We must be careful when handling such iterator.

Here is a simple example to demonstrate infinite iterators.

The built-in function `iter()` can be called with two arguments where the first argument must be a callable object (function) and second is the sentinel. The iterator calls this function until the returned value is equal to the sentinel.
```python
>>> int()
0

>>> inf = iter(int,1)
>>> next(inf)
0
>>> next(inf)
0
```
We can see that the `int()` function always returns 0. So passing it as `iter(int,1)` will return an iterator that calls `int()` until the returned value equals 1. This never happens and we get an infinite iterator.

The advantage of using iterators is that they save resources. Like shown above, we could get all the odd numbers without storing the entire number system in memory. We can have infinite items (theoretically) in finite memory.
