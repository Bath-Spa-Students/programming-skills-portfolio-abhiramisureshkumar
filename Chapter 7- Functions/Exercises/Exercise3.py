#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

#arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size,message):
    print("the size and the message for the given shirt is: ",size,message)
    make_shirt(6,"bathspa university")

size=int(input("enter your shirt size:"))
size=int(input("confirm your shirt size:"))
msg=input("enter the message!")


make_shirt(size,msg)




