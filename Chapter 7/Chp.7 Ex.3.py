"""
Chapter 7 Exercise 3 T-Shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size, message):  # defines the function with 2 parameter

    print(f"I am going to make a {size} t-shirt")  # states the size of the shirt being made
    print(f"It will say {message}\n")  # states what the shirt will say


make_shirt('Large', 'python')  # calls the function and uses positional arguments
make_shirt(size='Medium', message='python')  # calls the function and uses keyword arguments