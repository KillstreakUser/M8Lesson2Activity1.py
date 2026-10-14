students = ["Student.1", "Student.2", "Student.3", "Student.4", "Student.5", "Raman"]
print("Class List:", students)

print("Total Students:", len(students))
print("First Student:", students[0])
print("Last Student:", students[-1])
print("First Three:", students[:3])

students.append("Me")
print("\nAfter adding Me", students)
students.remove("Me")
print("\nAfter Removing Me", students)
students.sort()
print("Sorted Alphabetically:", students)
students.reverse()
print("Reversed:", students)

teacher = {"name": "Mr. Sharma", "subject": "Python", "experience": 5}
print("\nteacher profile:", teacher)

print("Subejct:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not Found"))
teacher["experience"] = 6
teacher["email"] = "sharma@gmail.com"
teacher.pop("experience")
print("Updated Teacher Profile:", teacher)

call_numbers = [1,2,3,4,5,6]
names = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Raman"]
student_directory = dict(zip(call_numbers, names))
print("\nStudent Directory:", student_directory)
print("\nStudent Role Number 6:", student_directory[6])