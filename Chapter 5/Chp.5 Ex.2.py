"""
Chapter 5 Exercise 2 Glossary
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.
"""
glossary = { #creates a dictionary
    'print' : 'displays the value of the variable', #defines the key 'print' with a value
    'input' : 'allows you to enter data in a program', #defines the key 'input' with a value
    'string' : 'is a group of characters or letters', #defines the key 'string' with a value
    'variable' : 'is represented by a letter or a string and is assigned to a value', #defines the key 'variable' with a value
    'constant' : 'is a variable whose value does not change' #defines the key 'constant' with a value
}

print("The function print",{glossary['print']}, "\n") #prints the definition of the key 'print'
print("The function input",{glossary['input']}, "\n") #prints the definition of the key 'input'
print("A string",{glossary['string']}, "\n") #prints the definition of the key 'string'
print("A variable",{glossary['variable']}, "\n") #prints the definition of the key 'variable'
print("A constant",{glossary['constant']}, "\n") #prints the definition of the key 'constant'