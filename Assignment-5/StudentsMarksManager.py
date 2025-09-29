class Student:
    def __init__(self, name, roll_no, marks=0):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks


student = Student("Ali", 101)
print(student.get_name())
print(student.get_roll_no())
print(student.get_marks())
student.set_marks(85)
print(student.get_marks())
student.set_marks(120)
