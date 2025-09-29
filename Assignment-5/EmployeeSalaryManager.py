class Employee:
    def __init__(self, name, salary=0):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive!")

    def show_details(self):
        print(f"Name: {self.__name}, Salary: {self.__salary}")


emp = Employee("Ahmed", 50000)
print(emp.get_name())
emp.show_details()
emp.set_salary(60000)
emp.show_details()
emp.set_salary(-1000)
