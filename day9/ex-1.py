student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if (student_scores[student] <= 70):
        student_grades[student] = 'Fail'
    if (student_scores[student] > 70 or student_scores[student] <= 80):
        student_grades[student] = 'Acceptable'
    if (student_scores[student] > 80 or student_scores[student] <= 90):
        student_grades[student] = 'Exceeds Expectations'
    if (student_scores[student] > 90):
        student_grades[student] = 'Outstanding'


# 🚨 Don't change the code below 👇
print(student_grades)
