# fruits = ["Apple", "Pear", "Mango", "Banana"]

# for fruit in fruits:
#     print(fruit, "pie")

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 68, 199, 78]
# student_scores.sort(reverse=True)
# print("Student Scores :", student_scores)

# sum = 0
# for score in student_scores:
#     sum += score

# print("total :", sum)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 68, 199, 78, 1000, 2000, 1029012]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)