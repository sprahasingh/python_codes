heights = input("Enter heights separated by ','\n").split(',')
student_heights = []
for n in range(0, len(heights)):
    student_heights.append(int(heights[n]))
total_sum = 0
num = 0
for height in student_heights:
    total_sum += height
for student in student_heights:
    num += 1
print(f"total height = {total_sum}")
print(f"number of students = {num}")
print(f"average height = {round(total_sum / num)}")
