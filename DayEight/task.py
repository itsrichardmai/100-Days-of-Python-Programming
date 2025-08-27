
# def greet():
#     print(f"Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")

# Function that allows for input 

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}")

greet_with_name("Chimken")

# def my_function(something):
    #do this with something 

    # something = parameter 
    # something = 123 argument

# Functions with more than 1 input 
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Richard","SF")
greet_with(name="Richard", location="SF")