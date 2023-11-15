#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.
#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.

glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the Python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    
    "if"  : "if statement evaluates condition",
    "elif": "used to test multiple condition",
    "else": "used to execute both the true part and the false part of a given condition",

    }


print(f"\n", "string",glossary["string"])
print(f"\n", "comment",glossary["comment"])
print(f"\n", "list",glossary["list"])
print(f"\n", "if",glossary["if"])
print(f"\n", "elif",glossary["elif"])
print(f"\n", "else",glossary["else"])