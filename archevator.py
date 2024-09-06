import zipfile

zip_file_name = 'modules.zip'

# Файли для архівування (окрім main.py)
files_to_zip = [
    'class_group.py',
    'class_human.py',
    'class_student.py',
    'custom_errors.py'
]

# Створюємо ZIP-архів і додаємо до нього файли
with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
    for file in files_to_zip:
        zip_file.write(file)

print(f'{zip_file_name} створено успішно!')
