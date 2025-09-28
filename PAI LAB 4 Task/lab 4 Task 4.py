class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_student(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")


class Marks(Student):
    def __init__(self, student_id, name, marks_coal, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)
        self.marks_coal = marks_coal
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print(f"Algorithms: {self.marks_coal}")
        print(f"Data Science: {self.marks_dataScience}")
        print(f"Calculus: {self.marks_calculus}")


class Result(Marks):
    def __init__(self, student_id, name, marks_coal, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_coal, marks_dataScience, marks_calculus)

    def display_result(self):
        total = self.marks_coal + self.marks_dataScience + self.marks_calculus
        avg = total / 3
        print(f"Total Marks: {total}")
        print(f"Average Marks: {avg:.2f}")


# Main function
student1 = Result("S101", "Masoom", 85, 90, 78)

student1.display_student()
student1.display_marks()
student1.display_result()
