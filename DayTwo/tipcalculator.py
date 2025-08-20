print("Hello! I will calculate your")
subtotal = float(input("What is the total bill? $"))
tip = float(input("What % would you like to tip?"))
total = (subtotal + (subtotal)*tip/100)
people = int(input("How many ways are we splitting the bill?"))

print(f"Your total bill is ${total}")
print(f"Your tip is: {subtotal*tip/100}")
print(f"Your total is ${total/people} per person!")
