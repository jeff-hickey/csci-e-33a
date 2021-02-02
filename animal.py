"""
1. a) Create a class called Dog with the following functions:
    init, grow, fetch_sticks, __str__
   b) Create a LazyDog class that is a child class of Dog and
   override the following functions: fetch_sticks, __str__

"""
from time import time


class Dog:

    def __init__(self, name):
        raise NotImplemented

    def grow(self):
        raise NotImplemented

    def fetch_sticks(self, sticks):
        raise NotImplemented

    def __str__(self):
        raise NotImplemented


class LazyDog(Dog):
    pass


"""
2. Create a list of Dogs, then write a function to iterate
 the list and print each Dog.
"""


def list_dogs():
    raise NotImplemented


"""
3. Create a list of Dogs, then filter the list to a subset of 
    the original. Hint: You might use a lambda and/or the filter
    function of a list.
"""


def filter_dogs():
    raise NotImplemented


"""
4. Create a Decorator to measure the execution time of previous functions.
"""


def measure_time(f):
    raise NotImplemented


@measure_time
def main():
    list_dogs()
    filter_dogs()


if __name__ == "__main__":
    main()
