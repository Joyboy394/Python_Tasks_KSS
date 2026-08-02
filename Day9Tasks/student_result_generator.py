class Result:
    def calculate_result(self, subject1, subject2, subject3=None):
        if subject3 is None:
            total = subject1 + subject2
            average = total / 2
            print(f"Marks: {subject1}, {subject2}")
        else:
            total = subject1 + subject2 + subject3
            average = total / 3
            print(f"Marks: {subject1}, {subject2}, {subject3}")

        print(f"Total: {total}, Average: {average:.2f}")


result1 = Result()

print("Result with two subjects:")
result1.calculate_result(80, 90)

print("\nResult with three subjects:")
result1.calculate_result(80, 90, 85)
