#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

#print a message saying you’ll add that topping to their pizza.

prompt= "\nhi sir/madam , what topping would you like on your pizza?"
prompt +="\nEnter 'quit' when you are finished."

while True:
    topping = input(prompt)
    if topping!= 'Quit':
      print("I will add" + topping +"to your pizza.")
    else:
       break  