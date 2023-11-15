#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

#each pet

my_pets=[
    {"kind": "Dog","owner": "Alexa"},
    {"kind": "Cat","owner": "Philips"},
    {"kind": "Birds","owner": "George"},
    {"kind": "Fish","owner": "Aviona"},
]

for pet in my_pets:
    print(f"kind of animal: {pet['kind']}\n")
    print(f"owner's name:{pet ['owner']}\n")