try:
    with open("marks.txt", "r") as file:
        lines = file.readlines()

    print("Student Records:")
    total_marks = 0
    student_count = 0

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        name, marks = line.split()
        marks = int(marks)

        print(f"{name} : {marks}")

        total_marks += marks
        student_count += 1

    if student_count > 0:
        average = total_marks / student_count
        print(f"\nAverage Marks: {average:.2f}")
    else:
        print("\nNo student records found in the file.")

except FileNotFoundError:
    print("marks.txt not found. Please make sure the file exists in the same folder as this program.")
    