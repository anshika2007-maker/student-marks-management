students = []


def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    # Student must score at least 33 in every subject
    if percentage >= 33 and all(mark >= 33 for mark in marks.values()):
        result = "PASS"
    else:
        result = "FAIL"

    highest_subject = max(marks, key=marks.get)
    lowest_subject = min(marks, key=marks.get)

    return total, percentage, grade, result, highest_subject, lowest_subject


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")

    marks = {}

    subjects = ["Maths", "Python", "English", "DBMS", "Computer"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully! ✅")


def display_result(student):
    name = student["name"]
    marks = student["marks"]

    total, percentage, grade, result, highest, lowest = calculate_result(marks)

    print("\n================================")
    print("        STUDENT RESULT")
    print("================================")

    print("Name:", name)

    print("\nSubject Marks:")

    for subject, mark in marks.items():
        print(f"{subject}: {mark}")

    print("\nTotal Marks:", total, "/ 500")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", result)

    print("\nHighest Marks:")
    print(f"{highest}: {marks[highest]}")

    print("\nLowest Marks:")
    print(f"{lowest}: {marks[lowest]}")

    print("================================")


def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n--- All Students ---")

    for i, student in enumerate(students, start=1):
        marks = student["marks"]

        total, percentage, grade, result, highest, lowest = calculate_result(marks)

        print(
            f"{i}. {student['name']} | "
            f"Percentage: {percentage:.2f}% | "
            f"Grade: {grade} | "
            f"Result: {result}"
        )


def search_student():
    if len(students) == 0:
        print("\nNo students found.")
        return

    name = input("\nEnter student name to search: ")

    found = False

    for student in students:

        if student["name"].lower() == name.lower():
            display_result(student)
            found = True
            break

    if not found:
        print("\nStudent not found.")


def main():

    while True:

        print("\n")
        print("================================")
        print("   STUDENT MARKS MANAGEMENT")
        print("================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("\nThank you for using Student Marks Management System! 👋")
            break

        else:
            print("\nInvalid choice. Please select 1-4.")


main()