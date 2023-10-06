"""
Chapter 6 Exercise 2 Movie Tickets
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket
"""
while True:  # Executes while the statement is true

    age = int(input(
        "Hi! Welcome to the movie theatre, how old are you?: "))  # using the function int to only allow inputs that contain an integer

    if age < 3:  # Executes if the user input is less than 3
        print(f"Wow, {age} years old? Here you go! Your ticket is free.")  # prints the cost of the ticket
        break  # ends the program
    elif age >= 3 and age <= 12:  # Executes if the user input is less than or equal to 3 and less than or equal to 12
        print(f"Wow, {age} years old? Here you go! Your ticket costs $10.")  # prints the cost of the ticket
        break  # ends the program
    else:  # Executes if the user input is greater than 12
        print(f"Wow, {age} years old? Here you go! Your ticket costs $15. ")  # prints the cost of the ticket
        break  # ends the program