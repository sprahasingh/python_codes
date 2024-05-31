student_scores = input("Enter scores separated by space\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
value = 0
for n in student_scores:
    if n > value:
        value = n
print(f"The highest score in the class is: {value}")
