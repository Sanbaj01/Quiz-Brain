class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grage = grade  # 0 to 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.student) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        pass


s1 = Student("Sanbaj", 23, 85)
s2 = Student("Samir", 20, 95)
s3 = Student("Manish", 21, 70)

course = Course("BIT", 4)
print(Course.add_student(s1))
Course.add_student(s2)
Course.add_student(s3)
print(course.students)

