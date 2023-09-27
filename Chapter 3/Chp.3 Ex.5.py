"""
Chapter 3 Exercise 5 Change Guest list
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
"""
guest = ['Mike', 'Sara', 'John'] #list of 3 guiests

print("Would you like to go to dinner with me,", guest[0], "?") #prints the invite to the first guest
print("Would you like to go to dinner with me,", guest[1], "?") #prints the invite to the second guest
print("Would you like to go to dinner with me,", guest[2], "?\n") #prints the invite to the third guest and creates a new line

print(f"Oh no! {guest[2]} can't come.\n") #prints that the last guest can't come

popped_guests = guest.pop(2) #removes the second guest on the list

new = input("Who would you like to invite?: ") #asks the user to add a new guest

guest.append(new) #adds the guest the user input in the list

print("Would you like to go to dinner with me,", guest[0], "?") #prints the invite to the first guest
print("Would you like to go to dinner with me,", guest[1], "?") #prints the invite to the second guest
print("Would you like to go to dinner with me,", guest[2], "?\n") #prints the invite to the third guest and creates a new line