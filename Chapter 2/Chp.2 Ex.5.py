"""
Chapter 2 Exercise 5 USB Shopper
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""
amount = 50  #the amount of the girl
usb = 6  #cost of one usb stick

total = amount//usb  #to know how many USB sticks the girl can buy
how = total*usb  #the total cost of all the USBs
change = amount - how  #to know the change the girl will get

print("The girl can buy", total, "USB sticks and she will have", change, "as change.\n")  #prints the total amount of USBs the girl can get and the change the girl will get.
