class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90,89,78,67,99)
    
    # def __str__(self):
    #     return f"Student's name is {self.name} and his/her average grade is {self.average()}"
    

    # Runs only if str is commented out
    def __repr__(self) -> str:
        return f"<Student (name:{self.name}, grades:{self.grades})"
    
    def average(self):
        return sum(self.grades)/len(self.grades)


student = Student()
print(student)
print(student.name)
print(student.grades)
print(student.average())