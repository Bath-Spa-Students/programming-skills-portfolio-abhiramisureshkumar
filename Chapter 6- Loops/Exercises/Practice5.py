#Largest number

num_list = []
while True:
    num = float(input("enter the number(0 to exit): "))
    num_list.append(num)
    max_num= 0
    min_num= 0
    if num ==0:
        break
    print("the maximum number is : ",max(num_list))
    print("the minimum number is : ",min(num_list))
3