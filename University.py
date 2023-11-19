# hamarya done
import abc


class Course(abc.ABC):
    def __init__(self, name: str, instructor: str, content: str):
        self.name = name
        self.content = content
        self.instructor = instructor
        self.assignment = []


class Professor:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def create_course(self, course_name, instructor: str, content: str) -> Course:
        return Course(course_name, instructor, content)


class GraduateCourse(Course):
    def __init__(self, name: str, instructor: str, content: str):
        super().__init__(name, instructor, content)
        self.assignments = []

    def assign_assignment(self, name, description, due_date):
        self.assignments.append(Assignment(name, description, due_date))


class UnderGraduateCourse(Course):
    def __init__(self, name: str, instructor: str, content: str):
        super().__init__(name, instructor, content)
        self.assignments = []

    def assign_assignment(self, name, description, due_date):
        self.assignments.append(Assignment(name, description, due_date))


class Assignment(abc.ABC):

    def __init__(self, name: str, description: str, due_date: str):
        self.name = name
        self.description = description
        self.due_date = due_date


class ConcreteAssignment1(Assignment):
    def __init__(self, name: str, description: str, due_date: str, additional: str):
        super().__init__(name, description, due_date)
        additional = ' '


class ConcreteAssignment2(Assignment):
    def __init__(self, name: str, description: str, due_date: str, additional: str):
        super().__init__(name, description, due_date)
        additional = ' '


class Student:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.courses = []
        self.assignments = []

    def enroll_course(self, course: Course):
        self.courses.append(course.name)

    def complete_assignment(self, assignment: Assignment):
        print(f'{self.name} successfully completed "{assignment.name}" assignment ! ')
        self.assignments.append(assignment.name)

    def view_progress(self):
        print(f'{self.name}"s progress - Courses:{self.courses} , Assignments: {self.assignments} ')


professor = Professor('Mr. Tom', '+654646769846')
student = Student('Anne Smith', 'ann.smith2001@gmail.com')
crs1 = professor.create_course('Mathematics', 'a', 'linear algebra')
print(f'"{crs1.name}" course was created by the professor "{professor.name}" ')
student.enroll_course(crs1)
assignment1 = Assignment('as1', 'do smth', 'july 4')
assignment2 = Assignment('as2', 'do smth2', 'june 15')
student.complete_assignment(assignment1)
student.complete_assignment(assignment2)
print(f"{student.name} was enrolled in {student.courses} course(s)")
student.view_progress()
