#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.



print("USB stick price $6.\n Note: Girl has $50.")
quantity = int(input ("how many can the girl buy:"))
price = int(50 - (quantity* 6))
print ("the girl's change is:\n", price)
