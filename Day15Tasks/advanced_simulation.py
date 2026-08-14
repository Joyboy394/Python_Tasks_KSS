import math
import random
import numpy as np
import pandas as pd


# 1. OOP to represent a Student
class Student:
    """Represents an individual student and handles grade calculation."""

    def __init__(self, student_id: str, mark: float):
        self.student_id = student_id
        self.mark = mark
        self.grade = self._assign_grade()

    # 2. Conditions to assign grades
    def _assign_grade(self) -> str:
        if self.mark >= 90:
            return "A+"
        elif self.mark >= 80:
            return "A"
        elif self.mark >= 70:
            return "B"
        elif self.mark >= 60:
            return "C"
        elif self.mark >= 50:
            return "D"
        else:
            return "F"

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "mark": round(self.mark, 2),
            "grade": self.grade,
        }


class ExamSimulationSystem:
    """Manages the full simulation pipeline from generation to report export."""

    def __init__(self, num_students: int = 50):
        self.num_students = num_students
        self.students = []
        self.results_df = None

    def run_simulation(self):
        # 3. Generate random marks using random and store in a NumPy array
        # Simulating a realistic distribution (Mean=72, Std=15) clipped to [0, 100]
        raw_marks = [
            min(100.0, max(0.0, random.gauss(72, 15)))
            for _ in range(self.num_students)
        ]
        marks_array = np.array(raw_marks)

        # 4. Use loops to construct Student objects
        for i, mark in enumerate(marks_array, start=101):
            student_id = f"STU-{i}"
            student = Student(student_id, mark)
            self.students.append(student)

        # 5. Convert results to Pandas DataFrame
        self.results_df = pd.DataFrame([s.to_dict() for s in self.students])

    # 6. Use math module for extra statistical calculations
    def calculate_math_stats(self) -> dict:
        if self.results_df is None:
            raise ValueError("Simulation must be run before calculating stats.")

        marks = self.results_df["mark"].tolist()
        n = len(marks)
        mean = sum(marks) / n

        # Variance and Standard Deviation via math.sqrt
        variance = sum((x - mean) ** 2 for x in marks) / n
        std_dev = math.sqrt(variance)

        # Square root transformation example (e.g., curved adjustment check)
        rms = math.sqrt(sum(x**2 for x in marks) / n)

        return {
            "total_students": n,
            "mean_mark": round(mean, 2),
            "std_deviation": round(std_dev, 2),
            "root_mean_square": round(rms, 2),
            "highest_mark": max(marks),
            "lowest_mark": min(marks),
        }

    # 7. Save report to file with Error Handling using try-except
    def export_report(self, filename: str = "exam_report.txt"):
        try:
            stats = self.calculate_math_stats()
            grade_counts = self.results_df["grade"].value_counts().to_dict()

            with open(filename, "w", encoding="utf-8") as f:
                f.write("=" * 45 + "\n")
                f.write("       EXAM RESULTS & SUMMARY REPORT       \n")
                f.write("=" * 45 + "\n\n")

                f.write("--- STATISTICAL SUMMARY (math module) ---\n")
                for key, val in stats.items():
                    f.write(f"{key.replace('_', ' ').title()}: {val}\n")

                f.write("\n--- GRADE DISTRIBUTION ---\n")
                for grade, count in sorted(grade_counts.items()):
                    f.write(f"Grade {grade}: {count} student(s)\n")

                f.write("\n--- DETAILED STUDENT RECORDS ---\n")
                f.write(self.results_df.to_string(index=False))

            print(f"✅ Report successfully generated and saved to '{filename}'.")

        except IOError as e:
            print(f"❌ File I/O Error: Failed to write report. {e}")
        except Exception as e:
            print(f"❌ Unexpected error occurred during report export: {e}")


# --- Execution ---
if __name__ == "__main__":
    try:
        # Initialize and execute simulation
        simulator = ExamSimulationSystem(num_students=30)
        simulator.run_simulation()

        # Generate output file
        simulator.export_report("final_exam_report.txt")

    except Exception as err:
        print(f"❌ Critical Failure: {err}")
        