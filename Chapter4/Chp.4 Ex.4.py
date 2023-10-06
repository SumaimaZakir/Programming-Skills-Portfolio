"""
Chapter 4 Exercise 4 States of Life
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.
"""
age = 25 #assigns the number to the variable, age.

if age < 2: #executes if the age is less than 2
    print("You're a baby.") #prints that the user is a baby
elif age == 2 or age < 4: #executes if the age is equal to 2 or less than 4
    print("You're a toddler.") #prints that the user is a toddler
elif age == 4 or age < 13: #executes if the age is equal to 4 or less than 13
    print("You're a kid.") #prints that the user is a kid
elif age == 13 or age < 20: #executes if the age is equal to 13 or less than 20
    print("You're a teenager.") #prints that the user is a teenager
elif age == 20 or age < 65: #executes if the age is equal to 20 or less than 65
    print("You're an adult.") #prints that the user is an adult
else: #executes if the age more than 65 years old
    print("You're an elder.") #prints that the user is an elder