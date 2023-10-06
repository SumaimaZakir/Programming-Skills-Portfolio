"""
Chapter 5 Exercise 4 Rivers
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""
river = { #makes a dictionary
    'The Nile River' : 'Egypt', #defines the key 'Nile River' with a value
    'The Thames River' : 'UK', #defines the key 'The Thames River' with a value
    'The Amazon River' : 'South America' #defines the key 'The Amazon River' with a value

}
for key, value in river.items(): #runs through the items in the dictionary and passes the keys and values in the dictionary
    print(f"{key} runs through {value}\n") #prints the river and where it runs through

for key in river.items(): #runs through the items in the dictionary and passes the keys in the dictionary
    print({key}, "\n") #prints the rivers

for value in river.items(): #runs through the items in the dictionary and passes the values in the dicitionary
    print({value}, "\n") #prints the location of the rivers