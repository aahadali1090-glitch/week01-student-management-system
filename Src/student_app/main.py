
from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
from student_app.utils.validation import validate_name, validate_marks
from student_app.services.calculator import calculate_grade
from student_app.models.student import Student
from student_app.reports.student_report import display_report
from student_app.services.json_handler import (
    load_students,
    save_students,
    display_all_students
)
from student_app.logger import logger


def add_student():
    students = load_students()

    if len(students) >= MAX_STUDENTS:
        logger.warning("Maximum student limit reached")
        print("Maximum student limit reached!")
        return

    name = input("\nEnter student name: ").strip()

    if not validate_name(name):
        logger.warning("Invalid student name entered")
        print("Invalid name!")
        return

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        logger.error("Invalid marks input: non-numeric value")
        print("Marks must be a valid number!")
        return

    if not validate_marks(marks):
        logger.warning("Invalid marks entered")
        print("Marks must be between 0 and 100!")
        return

    grade = calculate_grade(marks)

    student = Student(name, marks, grade)

    students.append(student.get_details())

    save_students(students)

    logger.info("Student record saved successfully")

    display_report(student)


def main():
    logger.info("Application started")

    print(f"\nWelcome to {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")

    while True:
        print("\n===== Student Management Menu =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_all_students()

        elif choice == "3":
            logger.info("Application closed")
            print("Goodbye!")
            break

        else:
            logger.warning("Invalid menu choice entered")
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
