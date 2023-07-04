class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My fullname: {self.fullname}, age: {self.age}, {self.is_married}.')


class Student(Person):
    def __init__(self, fullname, age, is_married, **marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_average_grade(self):
        summa = 0
        num = self.marks.values()
        for v in num:
            summa += int(v)
        aver = summa / len(num)
        print(f'Average grade is {aver}')


class Teacher(Person):
    salary = 25000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_salary(self):
        if self.experience > 3:
            for i in range(self.experience - 3):
                self.salary += (self.salary * 5) / 100
        print(f'зарплата Учителя за {self.experience} (года)лет опыта : {int(self.salary)}')


def create_students():
    students = []
    student1 = Student('Denis Lukyanov', 17,'is not married',russian=4, english=5, math=5, kyrgyz_lang=4, biology=4)
    student2 = Student('Nadirov Diyar', 17,'is not married',russian=3, english=4, math=3, kyrgyz_lang=4, biology=3)
    student3 = Student('Akbashev,Amir', 17,'is not married',russian=5, english=5, math=5, kyrgyz_lang=5, biology=5)
    students = [student1,student2,student3]
    return students


person = Person('Lukyanov Denis', 17, 'is not married')
person.introduce_myself()
print()

student = Student('Melisbekov Nuraaly', 18, 'is not married', russian=4, english=5, math=4, kyrgyz_lang=5, biology=3)
student.introduce_myself()
student.get_average_grade()
print()

print('Information about Teachers:')
teacher = Teacher('Alena Alexandrovna', 50, 'is married', 5)
teacher.introduce_myself()
teacher.get_salary()
print()

print(create_students())
student_list = create_students()
for i in create_students():
    print()
    i.introduce_myself()
    for n,v in i.marks.items():
        print(f'Предмет {n} > Оценка {v}')
    i.get_average_grade()
