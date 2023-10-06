"""
Chapter 6 Exercise 4 Deli
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""
sandwhich_orders = ['chicken', 'egg', 'fish']  # creates a list with 3 sandwhiches
finished_sandwhiches = []  # creates an empty list

while sandwhich_orders:  # while

    sandwhich_now = sandwhich_orders.pop()  # pops all the elements one by one
    print(f"I am now making your {sandwhich_now} sandwhich.")  # prints the popped sandwhich in order
    finished_sandwhiches.append(sandwhich_now)  # adds the popped sandwhiches to the empty list

print("\n\n")  # prints new lines

for sandwhich in finished_sandwhiches:  # runs through the list and selects the elements one by one
    print(f"I made you a {sandwhich} sandwhich")  # prints each element one by one