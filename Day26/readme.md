# List and Dictionary Comprehension 

Create a new list from a previous list

We have been doing that using For Loops 

If I want to create a new list where each number is increased by 1,
I would append the increased number to the new_list

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1 
    new_list.append(add_1)

# List Comprehension 

new_list = [new_item for item in list]

<!-- In the example of our states game  -->
if answer_state == "Exit":
missing_states = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv)

# Dictionary Comprehension 

new_dict = {new_key:new_value for item in list}


Each row is a pandas series object which means we can type into the rows and get hold of the value under a particular column by using the dot 
