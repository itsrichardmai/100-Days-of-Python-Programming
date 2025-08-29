student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades= {}

for key in student_scores:
    student_grades[key] = student_scores[key]
    grade = student_grades[key] 
    
    if grade >= 91:
        student_grades[key] = "Outstanding"
    elif grade in range(81,91):
        student_grades[key] = "Exceeds Expectations"
    elif grade in range(71,81):
        student_grades[key] = "Acceptable"
    elif grade in range(0,71): 
        student_grades[key] = "Fail"
    else: student_grades[key] = grade
print(student_grades)