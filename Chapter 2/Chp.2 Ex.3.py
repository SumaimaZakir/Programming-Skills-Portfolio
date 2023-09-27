"""
Chapter 2 Exercise 3 Stripping Names
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

person_name = "\t Sumaima \n"  # Use a variable to represent a person's name with whitespace characters

print("Name with Whitespace:", person_name)  # Print the name with whitespace

print("Name using lstrip():", person_name.lstrip())  # Print the name using lstrip() to remove leading whitespace

print("Name using rstrip():", person_name.rstrip())  # Print the name using rstrip() to remove trailing whitespace

print("Name using strip():", person_name.strip())   # Print the name using strip() to remove both leading and trailing whitespace
