"""
Chapter 5 Exercise 5 Pets
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""
fish = {'Gold Fish' : 'John'} #makes a dictionary that consists of the pet and owner
dog = {'Dalmation' : 'Timmy'} #makes a dictionary that consists of the pet and owner
fish = {'Molly' : 'Mike'} #makes a dictionary that consists of the pet and owner

pet = [fish, dog, fish] #creates a nested dictionary

for pets in pet: #runs through each dictionary and prints the key and value in each dictionary
    print(pets, "\n")