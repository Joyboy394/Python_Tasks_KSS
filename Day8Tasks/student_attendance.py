name = input("Enter student name: ")

with open("attendance.txt", "a") as file:
    file.write(name + "\n")

print("\nAttendance recorded successfully!")

print("\nContents of attendance.txt:")
with open("attendance.txt", "r") as file:
    print(file.read())
    