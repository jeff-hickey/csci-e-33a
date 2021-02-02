"""
1. a) Create a class called Dog with the following functions:
    init, grow, fetch_sticks, __str__
   b) Create a LazyDog class that is a child class of Dog and
   override the following functions: fetch_sticks, __str__

"""
from time import time


class Dog:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.sticks_fetched = 0

    def grow(self):
        """
        Increments the dogs age.
        """
        self.age += 1

    def fetch_sticks(self, sticks):
        """
        Increments the number of sticks
        this dog has fetched.
        :param sticks:
        """
        self.sticks_fetched += sticks

    def __str__(self):
        """
        Display value for our Dog.
        :return: string representaiton
        """
        return f"{self.name} "


class LazyDog(Dog):

    def fetch_sticks(self, sticks):
        """
        Increments sticks_fetched but
        only if there are more than 5 sticks.
        :param sticks:
        """
        if sticks > 5:
            return
        self.sticks_fetched += sticks

    def sleep(self):
        """
        Prints zzz.
        :return:
        """
        print("zzz")

    def __str__(self):
        """
        Display value for our LazyDog.
        :return: string representaiton
        """
        return f"{self.name}, I'm a lazy dag."


"""
2. Create a list of Dogs, then write a function to iterate
 the list and print each Dog.
"""

# Create a list of dogs.
dogs = [Dog('Spot'), Dog('Sparky'), Dog('Barker'), Dog('Moon'),
        Dog('River'), LazyDog('Lazy Duke')]


def list_dogs():
    # Iterate and print dog names.
    for dog in dogs:
        print(dog)


"""
3. Create a list of Dogs, then filter the list to a subset of 
    the original. Hint: You might use a lambda and/or the filter
    function of a list.
"""


def filter_dogs():
    # Use a lambda function to filter the list.
    faves = list(filter(lambda x: x.name.startswith('S'), dogs))
    for fave in faves:
        print(fave)


"""
4. Create a Decorator to measure the execution time of previous functions.

"""

def measure_time(f):
    def wrapper():
        start = time()
        f()
        print(f'Elapsed time: {time() - start}')

    return wrapper


@measure_time
def main():
    list_dogs()
    filter_dogs()


if __name__ == "__main__":
    main()
