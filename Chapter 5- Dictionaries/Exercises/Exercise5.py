#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

#each pet
pets=[]
pet={'kind': 'Dog','name':'jimmy','owner': 'Alexa','place':'USA'}
pets.append(pet)
pet= {'kind': 'Cat','name':'sissy','owner': 'Philips','place':'UAE'}
pets.append(pet)
pet={'kind': 'Birds','name':'tito','owner': 'George','place':'London'}
pets.append(pet)
    

for pet in pets:
    print("\nthis is about "+ pet['name'].title() +":")
    for key, value in pet.items():
      print("\t" + key + ":"+ str(value))