class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def __str__(self):
        return (f"Student: {self.first_name} {self.last_name}, Age: {self.age}, "
                f"Average score: {self.average_grade:.2f}")

student = Student("Mykola", "Ivanov", 20, 4.5)

print(f"Before average score changes:\n{student}")

student.update_average_grade(4.8)

print(f"After average score changes:\n{student}")