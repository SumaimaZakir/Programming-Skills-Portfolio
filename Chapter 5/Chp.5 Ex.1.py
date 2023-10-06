"""
Chapter 5 Exercise 1 Person
Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""
info = { #makes a dictionary
    'first_name' : 'John', #defines the variable first_name
    'last_name' : 'Junior', #defines the variable last_name
    'age' : 21, #defines the variable age
    'city' : 'Dubai' #defines the city
}

print(info['first_name']) #prints the value stored in 'first_name'
print(info['last_name']) #prints the value stored in 'last_name'
print(info['age']) #prints the value stored in 'age'
print(info['city']) #prints the value stored in 'city'