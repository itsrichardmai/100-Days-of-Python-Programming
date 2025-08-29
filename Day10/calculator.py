logo = '''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
      
_____________________
|  _________________  |
| | RM           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      '''
print('''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
      
_____________________
|  _________________  |
| | RM           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      ''')

def add(n1, n2):
    return n1 + n2 
def subtract(n1, n2): 
    return n1 - n2 
def multiply(n1, n2):
    return n1 * n2 
def divide(n1, n2):
    return n1 / n2 

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    print(logo)
    number1 = float(input("What's the first number?: "))

    keep_going = True
    while keep_going:
        for symbol in operations:
            print(symbol)
        
        operation = input("What operation: ?")
        number2 = float(input("What's the second number?: "))
        answer = (operations[operation](number1, number2))
        print(f"your answer is {answer}")
        should_continue = input(f"Operate on {answer}? type 'y' for yes. 'n' for no. 'q' to close. ")
        if should_continue == 'n':
            print("\n" *10)
            calculator()
        elif should_continue == 'y':
            number1 = answer
        elif should_continue == 'q':
            print("Thank you! Goodbye!")
            keep_going = False
            break
        else: 
            print("You did not enter a valid option.")

calculator()
