# Day 16 : Object Oriented Programming 

Our code begins to become a lot more complex and become spaghetti like. 

Procedural Programming : 
We set up procedures or functions that handles our program 
Earliest paradigms of programming 

Increase in complexity and number of relationships we need to remember and manage becomes confusing. 

How can we maintain a simple relationship in our code while being able to write complex programs?

Object Oriented Programming
* Split a taks into separate pieces
* Each of those pieces become reusable in the future
* Imagine being tasked with running a restaurant. 

<!-- Defining a Waiter -->
Waiter does? = Functions 
Waiter has? = Attributes 

is_holding_plate = True
tables_responsible = [4,5,6]

methods: def take_order(table, order):
<!-- takes order to chef -->

def take_payment(amount):
<!-- add money to restaurant -->

class Waiter:
    def __init__(self, name, ):
        self.name = name
        self.is_holding_plate: True
        self.tables_responsible = []

# Object Attributes 
car.speed 
<!-- from this object, get the speed attribute.  -->

# Object Methods 
<!-- functions when tied to an object are called methods -->
car.stop()
