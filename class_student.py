from class_human import Human


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

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.age == other.age and self.gender == other.gender

