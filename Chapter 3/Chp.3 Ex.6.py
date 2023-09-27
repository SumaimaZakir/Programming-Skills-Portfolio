"""
Chapter 3 Exercise 6 Shrinking guest list
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""
guest = ['Mike', 'Sara', 'John'] #list of 3 guests

print("Oh no! My new dining table won't be able to arrive on time, sorry I can only invite two people!\n") #prints that only 2 guests can come

popped_guest = guest.pop(0) #removes the first guest

print(f"Sorry, {popped_guest}, I can't invite you anymore.\n") #says that the first removed guest cant come

print("You're still invited", guest[0]) #tells the first guest in the list that they can still come
print("You're still invited", guest[1], "\n") #tells the second guest in the list that they can still come

del guest[:] #removes everyone in the list

print(guest, "\n") #prints an empty list