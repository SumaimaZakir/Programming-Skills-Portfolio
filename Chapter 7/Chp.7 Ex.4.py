"""
Chapter 7 Exercise 4 Large Shirts
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
"""


def make_shirt(size='Large', message='I love Python'):  # makes a function with default values

    print(f"I am going to make a {size} shirt.")  # states that it will make a large shirt
    print(f"It will say {message}.\n")  # states that the shirt will say I love Python


make_shirt()  # calls teh function as is
make_shirt(
    size='medium')  # calls the function and replaces the value for the argument 'size' with the use of keyword arguments
make_shirt('Extra Large', 'Hello')  # calls the function and uses positional arguments