class InvalidMarksException(Exception):
    pass

class InvalidAgeException(Exception):
    pass


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = 0
        self.age = 0

    def setMarks(self, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksException("Marks should be between 0 to 100")
        else:
            self.marks = marks

    def setAge(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeException("Age should be between 0 to 120")
        else:
            self.age = age


s = Student("Manasvi", 101)

try:
    s.setMarks(85)
    s.setAge(22)

    print("Name:", s.name)
    print("Roll No:", s.roll_no)
    print("Marks:", s.marks)
    print("Age:", s.age)

except InvalidMarksException as e:
    print(e)

except InvalidAgeException as e:
    print(e)