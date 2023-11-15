#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the Python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    "if"  : "if statement evaluates condition",
    "elif": "used to test multiple condition",
    "else": "used to execute both the true part and the false part of a given condition",

    }
for word,meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")