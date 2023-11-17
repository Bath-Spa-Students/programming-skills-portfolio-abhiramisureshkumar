#replacing elements in List


list1=[7 , 2 , 6 , 89 , 65 , 34]
if 34 in list1:
    print(34)
    num=list1.index(34)
    list1[num]=650
    print(list1)