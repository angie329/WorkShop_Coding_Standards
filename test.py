""" 
Module to manage student grades and basic 
academic records
"""
class Student:
    """Represents a student and their academic record"""
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "F"

    def add_grades(self, grade):
        """Adds a grade to the student's record"""
        self.grades.append(grade)

    def calc_average(self):
        """Calculates and returns the average of the grades"""
        if len(self.grades) == 0:
            return 0.0
        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        """Checks if the student belongs to the honor roll"""
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Deletes a grade by its index safely"""
        if index < len(self.grades):
            del self.grades[index]

    def report(self):  # broken format
        """Prints a basic report of the student"""
        print(f"ID: {self.student_id}")
        print(f"Name is: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Final Grade = {self.letter}")


def startrun():
    """Main execution function for basic testing"""
    a = Student("202212890", "Angie")
    a.add_grades(100)
    a.add_grades(50)  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()

if __name__ == "__main__":
    startrun()
