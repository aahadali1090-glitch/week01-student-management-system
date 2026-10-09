
from student_app.services.json_handler import load_students

students = load_students()

print("Student Records")
print("--------------------")

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Grade:", student["grade"])
    print("--------------------")
