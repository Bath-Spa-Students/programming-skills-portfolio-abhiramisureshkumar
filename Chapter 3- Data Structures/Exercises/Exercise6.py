#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

#•Print a message to each of the two people still on your list, letting them know they’re still invited.

#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
members = ['sofi', 'sara', 'alex']
print(f" i'm inviting you to join for dinner with me tonight.{members[0]}")
print(f" i'm inviting you to join for dinner with me tonight.{members[1]}")
print(f" i'm inviting you to join for dinner with me tonight.{members[2]}")
print(f"{members[2]}, can't make it for dinner with me tonight.")
members[2]="aviona"
print(members)
print(f" i'm inviting you to join for dinner with me tonight.please come {members[0]}")
print(f" i'm inviting you to join for dinner with me tonight.please come {members[1]}")
print(f" i'm inviting you to join for dinner with me tonight.please come {members[2]}")
print("sorry guys,i need to shrink the number of people.so only two people can join with me")
name=members.pop(2)
print(f"{name} i'm sorry , but i won't be able you invite you for dinner with me tonight.")
print(f"{members[0]}, you're still invited.please come")
print(f"{members[1]}you're still invited.please come")
del members[0]
print(members)

