
from student_app.services.json_handler import load_students, save_students

students = load_students()

new_student = {
    "name": "Sara",
    "marks": 92,
    "grade": "A"
}

if not any(student["name"] == new_student["name"] for student in students):
    students.append(new_student)
    save_students(students)
else:
    print("Student already exists!")

print("\nSaved Students:")

for student in load_students():
    print(student)
