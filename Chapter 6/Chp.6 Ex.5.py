"""
Chapter 6 Exercise 5 No Pastrami
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'roast beef', 'pastrami', 'ham', 'cheese'] #creates a list with 6 sandwhiches
finished_sandwiches = [] #creates an empty list

# Print a message if pastrami is in the list and remove all occurrences of pastrami
print("Sorry, the deli has run out of pastrami.") #prints that deli is out of stock
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami') #removes element with the word 'pastrami'

while sandwich_orders: # Make sandwiches
    current_sandwich = sandwich_orders.pop()
    print(f"Making a {current_sandwich} sandwich...")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:") # Display finished sandwiches
for sandwich in finished_sandwiches:
    print(sandwich) #prints each element one by one
