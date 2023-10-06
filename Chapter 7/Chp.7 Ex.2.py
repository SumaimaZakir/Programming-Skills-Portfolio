"""
Chapter 7 Exercise 2 Favorite Book
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my

favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book(title):  # defines the function with a parameter 'title'

    print(f"{title} is one of my favorite books.")  # prints the parameter in a sentence.


favorite_book('Alchemist')  # calls the function with an argument