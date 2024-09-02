# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.

# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
#
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
#
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.

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
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            print(f'Student {student.first_name} {student.last_name} has been removed from the group.')
        else:
            print(f'Student with last name {last_name} not found.')

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(f'{student.first_name} {student.last_name}' for student in self.group)
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(st1)
print(st2)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
