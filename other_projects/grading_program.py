student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if 90 < score <= 100:
        grade = "Outstanding"
    elif 80 < score <= 90:
        grade = "Exceeds Expectations"
    elif 70 < score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student] = grade
print(student_grades)
