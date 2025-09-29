import random 
import pandas as pd 

def main():
    # numbers = [1,2,3]
    # List comprehension 
    # new_list = [n+1 for n in numbers]
    # print(new_list)
    
    # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    # squared_numbers = [num*num for num in numbers]
    # print(squared_numbers)

    # list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    # numbers = [int(num) for num in list_of_strings]
    # result = [num for num in numbers if num % 2 == 0]
    # print(result)

    names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
    # Output: [0, 32, 8, 2, 8, 64, 42]
    student_scores = {student:random.randint(1,100) for student in names}
    print("Random Student Scores: ", student_scores)

    passed_students = {student:score for (student, score) in student_scores.items() if score>=70}
    print("Passing Students:", passed_students)

    # Exercise 1 - List & Dictionary Comprehension 
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    sentence_list = sentence.split()
    # Split the sentence into a list of words 
    print(sentence_list)

    result = {word:len(word) for word in sentence_list}
    print(result)
    # Exercise 2: Weather_c 
    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

    weather_f = {day:(value*9/5)+32 for (day, value) in weather_c.items()}

    print(weather_f)

    # How to use Loops to iterate over a pandas Data Frame
    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }
    
    # Looping through dictionaries 
    for (key, value) in student_dict.items():
        print(value)
    
    # Student DataFrame using Pandas

    df = pd.DataFrame(student_dict)
    print("Student DataFrame:", df)
    # Loop throuh a DataFrame
    # for (key, value) in df.items():
        # print(value)
    
    # Loop through the rows of a dataframe
    for (index, row) in df.iterrows():
        print("Student:\n", row.student)
        print("Score:\n", row.score)

    # for (index, row) in df.itterows():

if __name__ == '__main__':
    main()
