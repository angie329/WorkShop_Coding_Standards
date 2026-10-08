class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "F"

    def add_grades(self, grade):
        self.grades.append(grade)

    def calc_average(self):
        if len(self.grades) == 0:
            return 0.0
        total = sum(self.grades)
        return total / len(self.grades)

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
