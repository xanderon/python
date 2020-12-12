student_heights = [187, 176, 159, 188, 190, 184, 183, 186]
max = student_heights[0]
for student in student_heights:
    if max < student:
        max = student
print(max)
