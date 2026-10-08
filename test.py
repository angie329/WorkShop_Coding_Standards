""" 
Module to manage student grades and basic 
academic records
"""
class Student:
    """Represents a student and their academic record"""
    def __init__(self, student_id, name):
        if not student_id or not name:
            print("Error: ID and name cannot be empty")
            self.student_id = "N/A"
            self.name = "No Name"
        else:
            self.student_id = student_id
            self.name = name
        self.grades = []
        self.is_passed = "Failed"
        self.honor_roll = False
        self.letter_grade = "F"

    def add_grades(self, grade):
        """Adds a grade to the student's record"""
        if not isinstance(grade, (int, float)):
            print(f"Error: The grade '{grade}' must be a number")
            return
        if not 0 <= grade <= 100:
            print(f"Error: The grade {grade} must be between 0 and 100")
            return
        self.grades.append(float(grade))

    def update_status(self):
        """Updates the letter grade, pass status, and honor roll"""
        average = self.calc_average()
        if average >= 90:
            self.letter_grade = "A"
        elif average >= 80:
            self.letter_grade = "B"
        elif average >= 70:
            self.letter_grade = "C"
        elif average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        self.is_passed = "Passed" if average >= 60 else "Failed"
        self.honor_roll = average >= 90

    def calc_average(self):
        """Calculates and returns the average of the grades"""
        if len(self.grades) == 0:
            return 0.0
        total = sum(self.grades)
        return total / len(self.grades)

    def remove_grade_by_index(self, index):
        """Removes a grade at the specified index"""
        if 0 <= index < len(self.grades):
            del self.grades[index]
            print("Grade removed by index")
        else:
            print("Error: Index out of bounds")

    def remove_grade_by_value(self, value):
        """Removes the first occurrence of a specific grade"""
        if value in self.grades:
            self.grades.remove(value)
            print("Grade removed by value")
        else:
            print("Error: Grade not found")

    def report(self):  # broken format
        """Prints a basic report of the student"""
        self.update_status()
        average = self.calc_average()
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Status: {self.is_passed}")
        print(f"Honor Roll: {self.honor_roll}")

def startrun():
    """Main execution function for basic testing"""
    student_a = Student("202212890", "Angie")
    student_a.add_grades(95.0)
    student_a.add_grades(85.5)
    student_a.add_grades(92.0)
    student_a.report()

    # Testing 1 ( Deleting grades)
    student_a.remove_grade_by_index(1)
    student_a.remove_grade_by_value(95.0)
    student_a.report()

    # Testing 2
    student_b = Student("", "")
    student_b.add_grades("Invalid")
    student_b.add_grades(150)

if __name__ == "__main__":
    startrun()
