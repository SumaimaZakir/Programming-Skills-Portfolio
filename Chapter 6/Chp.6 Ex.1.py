"""
Chapter 6 Exercise 1 Pizza Toppings
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""

while True:  # Executes while the statement is true

    topping = input(
        "Enter any ingredient to put on the pizza. Enter 'QUIT' if you want to stop adding toppings: ")  # alows the user to input any topping or enter 'quit'

    if topping == 'QUIT':  # executes if the user enters 'QUIT'
        print("Enjoy your pizza!")  # prints "Enjoy your pizza!"
        break  # stops the code
    else:  # Execute if the user doesn't enter 'QUIT'
        print(topping, "has been added to your pizza.")  # prints the topping the user had inputted in.
        continue  # continues with the code until the user enters 'QUIT'