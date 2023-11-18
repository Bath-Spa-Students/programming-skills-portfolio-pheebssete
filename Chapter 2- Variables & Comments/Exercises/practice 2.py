# create marks input courses

course1 = float(input("Put your course 1 marks: "))
course2 = float(input("Put your course 2 marks: "))

average_marks = (course1 + course2 ) / 5

total_marks = float(input("Enter the total marks: ")) 
percentage = (average_marks / total_marks) * 100

print(f"The average of all courses is: {average_marks:.2f}")
print(f"The percentage of the student is: {percentage:.2f}%")