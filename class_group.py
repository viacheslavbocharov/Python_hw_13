from custom_errors import OverCrowderError


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