# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача.
#
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента

class OverCrowderError(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return(
            f'Full name: {self.first_name} {self.last_name}\n'
            f'Age: {self.age}\n'
            f'Gender: {self.gender}'
        )


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (
            f'Student full name: {self.first_name} {self.last_name}\n'
            f'Age: {self.age}\n'
            f'Gender: {self.gender}\n'
            f'Records: {self.record_book}\n'
        )


class Group:

    def __init__(self, number):
        self.number = number
        self.__group = set()

    def add_student(self, student):
        if len(self.__group) < 10:
            self.__group.add(student)
        else:
            raise OverCrowderError("It can be only 10 students in a group")

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.__group.remove(student)
            print(f'Student {student.first_name} {student.last_name} has been removed from the group.')
        else:
            print(f'Student with last name {last_name} not found.')

    def find_student(self, last_name):
        for student in self.__group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(f'{student.first_name} {student.last_name}' for student in self.__group)
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 20, 'John', 'Doe', 'AN150')
gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    for i in range(8):
        gr.add_student(Student('Male', 22, f'Student{i}', f'LastName{i}', f'AN1{i}'))
    gr.add_student(st3)
except OverCrowderError as e:
    print(f'Error: {e}')

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')  # No error!
