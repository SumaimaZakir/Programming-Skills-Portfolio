"""
Chapter 5 Exercise 3 Glossary 2
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

glossary = { #makes a dicitonary
    'print' : 'displays the value of the variable', #defines the key 'print' with a value
    'input' : 'allows you to enter data in a program', #defines the key 'input' with a value
    'string' : 'is a group of characters or letters', #defines the key 'string' with a value
    'variable' : 'is represented by a letter or a string and is assigned to a value',#defines the key 'variable' with a value
    'constant' : 'is a variable whose value does not change' #defines the key 'constant' with a value
}

for key, value in glossary.items(): #checks the key and value through the dictionary
    print(f"{key} {value}\n") #prints the key and value