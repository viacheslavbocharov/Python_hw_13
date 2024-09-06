import sys
sys.path.insert(0, 'modules.zip')


from custom_errors import OverCrowderError
from class_student import Student
from class_group import Group


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 20, 'John', 'Doe', 'AN150')
gr = Group('PD1')
print(f'st1 = st2? - {st1 == st2}')
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

