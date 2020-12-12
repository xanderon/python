#input but cold now
student_heights = [187, 176, 159, 188, 190, 184, 183, 186]
total_height = 0
total_students = 0
for student in student_heights:
    total_height += student
    total_students += 1
avg_height = total_height / total_students      
print(f"for {student_heights} \nwe have an avegarge of {round(avg_height)} ")
