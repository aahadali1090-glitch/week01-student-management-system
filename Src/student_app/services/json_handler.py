
import json

from student_app.config import DATA_FILE


def load_students():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["students"]


def save_students(students):
    data = {"students": students}

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Student data saved successfully!")

def display_all_students():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n===== All Student Records =====")

    for index, student in enumerate(students, start=1):
        print(f"\nStudent #{index}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Grade: {student['grade']}")

    print(f"\nTotal Students: {len(students)}")

from student_app.services.calculator import calculate_grade


