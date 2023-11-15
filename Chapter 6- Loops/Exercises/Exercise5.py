#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders= ['turkey','pastrami','veg','cheese','pastrami','tuna']
finished_sandwiches=[]

print("sorry,pastrami is not available")
while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop(0)  
    print(f"your {current_order} sandwich is ready.")  
    finished_sandwiches.append(current_order)

    print("\n list of finished sandwiches:")
    for sandwich in finished_sandwiches:
        print(sandwich)