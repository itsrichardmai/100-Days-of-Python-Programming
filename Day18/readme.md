# Day 18: Importing Modules and building a GUI 

# Types of Imports 

Basic Import: 
keyword - module to import 
import turtle 

from .. import .. 
keyword module name keyword thing in module  
from turtle import Turtle

from turtle import * 
keyword module keyword 
(*) means everything from the file 
<!-- has advantages and disadvantages -->

turtle is a module that is packaged with the standard Python library.
If the module is not packaged with the standard Python library, 
in order to access other modules, we need to go to a bigger library 

We will install these modules the internet. We plug and play whatever we need. 
Currently we are using pip 

<!-- What happens when you install a package? -->

It gets installed into the local virtual environment which is on a per project basis. 

The reason we need to work with venv in Python is actually a historical problem 
Python-3 is not backward compatible with Python 2. If you try to add Python 3 to a project with Python 3, it does not work.
So the transition has been really really slow and virtual environments help us by defining a small sandbox for our project

Because we have our venv for each and every project, and its different for every project, we can install each module and know its compatible. 

It's like freezing that project in time so that you know that once you compile everything, when that program runs, you can keep running it even if Python changes versions. 

# Tuples are immutable 
Their values cannot be changed unlike lists 
my_tuple[2] = 12 
would produce a type error. 'tuple' object does not support item assignment
why use a tuple? if you're creating a list that you want to stay constant. You don't want it to be accidentally changed or messed up. 

to change a tuple, you can put it in a list and convert it to a list. 
