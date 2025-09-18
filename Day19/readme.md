# More Turtle Graphics, Event Listeners, State and Multiple Instances

Making Etch a Sketch 

This game will allow us to use the up and down arrows to move the turtle forward and back and turn our turtle clockwise and anti clockwise to continue drawing 


# High Order Functions 

In order to create a lot of the games we spoke about, we need to listen to the things the user does 

The code that allows us to do this are caLLED event listeners

In the turtle documentation, there are event listening methods.
These allow the turtle screen to listen and wait for events the user might trigger

When we use a function as an argument ( something that is going to passed in to another function, we don't use the paranthesis at the end ) The parenthesis triggers the function to happen there and then. But what we want is this on key to listen for when the spacebar is pressed to trigger the move forward function. 

We're now controlling our turtle using a keystroke.

We are using a function as an input. 
When we pass a function as an input, we only pass the name. Not the parenthesis. 

Example of passing a function into another function:
i.e 

def add(n1, n2):
return n1 + n2 
...
def calculator(n1, n2, func):
return funct(n1,n2)

Higher Order Functions:
A function that could work with other functions because they are taking other functions as input and then working with it in the body of function 

Very useful for listening to events and triggering functions

# Objects State and Instances 

timmy.color = green
tommy.color = purple

We will build out our turtle racing game and we will see this in action. Each turtle object will have a different state. 

