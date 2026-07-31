SUBJECTS = ("Math", "Science", "English")

student_names = set()
student_marks = {}


def total_marks(marks_list):
    """Recursive function to calculate the total of a list of marks."""
    if not isinstance(marks_list, list):
        raise TypeError("Marks data type error.")
    if len(marks_list) == 0:
        return 0
    return marks_list[0] + total_marks(marks_list[1:])


def add_student():
    name = input("Enter student name: ")
    marks = []

    try:
        for subject in SUBJECTS:
            mark = int(input(f"Enter marks for {subject}: "))
            marks.append(mark)
    except ValueError:
        print("Invalid input! Please enter numeric marks.")
        return

    student_names.add(name)
    student_marks[name] = marks


def display_students():
    if not student_names:
        print("No student records available.")
        return

    for name in student_names:
        print(f"{name} : {student_marks[name]}")


def calculate_average():
    name = input("Enter student name to calculate average: ")

    try:
        if name not in student_names:
            raise NameError("Student name not found.")

        marks = student_marks[name]

        if not isinstance(marks, list):
            raise TypeError("Marks data type error.")

        total = total_marks(marks)
        average = total / len(marks)

        print(f"Total Marks: {total}")
        print(f"Average Marks: {average}")

    except NameError as e:
        print(e)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError as e:
        print(e)


def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
    