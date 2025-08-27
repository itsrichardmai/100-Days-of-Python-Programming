
print('''
dictionary = {
    "Bug":"An error that prevents a program from running as excepcted",
    "Function": "A piece of code that you can call easily over and over again",
    "Loop": "The action of doing something over and over again"
    }
''')

# wipe a dictionary 

programming_dictionary = {}
print(programming_dictionary)

# edit an item in a dictionary 

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# loop through a dictionary 

for key in programming_dictionary:
    print(f"key ={key}")
    print(f"programming_dictionary[key]: {programming_dictionary[key]}")