#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.

#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.


# Invite some people to dinner.
guests = ['sofi', 'sara', 'alex']

name = guests[0].title()
print(f"{name}, i'm inviting you to join for dinner with ,me tonight.")

name = guests[1].title()
print(f"{name},i'm inviting you to join for dinner with ,me tonight .")

name = guests[2].title()
print(f"{name},i'm inviting you to join for dinner with ,me tonight .")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")


del(guests[1])
guests.insert(1, 'halia')


name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")
