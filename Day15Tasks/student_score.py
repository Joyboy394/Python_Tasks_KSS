import math

# Sample data: list of tuples (Name, Marks)
students = [("A", 45), ("B", 80), ("C", 55), ("D", 30), ("E", 90)]

# 1. Convert data into a dictionary
student_dict = dict(students)
print("Student Dictionary:", student_dict)

# 2. Loop + condition to find students scoring above 50
above_50 = []
for name, marks in student_dict.items():
    if marks > 50:
        above_50.append((name, marks))

print("Students scoring above 50:", above_50)

# 3. Use math module to calculate average
total = sum(student_dict.values())
average = total / len(student_dict)
# math.floor / math.ceil demonstrate use of the math module
rounded_avg = math.floor(average * 100) / 100  # truncate to 2 decimals

print("Average marks:", rounded_avg)

# 4. Store results in a text file
with open("student_results.txt", "w") as f:
    f.write("Student Dictionary:\n")
    for name, marks in student_dict.items():
        f.write(f"{name}: {marks}\n")

    f.write("\nStudents scoring above 50:\n")
    for name, marks in above_50:
        f.write(f"{name}: {marks}\n")

    f.write(f"\nAverage marks: {rounded_avg}\n")

print("\nResults written to student_results.txt")
