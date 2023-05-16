import random
import pandas

names = ["Khesehang", "Amar", "Karuna", "Namrata"]

new_list = {name: random.randint(0, 100) for name in names}
# print(new_list)

passed_students = {student: value for (student, value) in new_list.items() if (value >= 60)}

student_dict = {
    "students": ["Khese", "Amar", "Karuna", "Namrata", "Pem"],
    "marks" : [80, 78, 85, 78, 84]
}

student_pandas = pandas.DataFrame(student_dict)

print(student_pandas)

# Pandas has itterrows() method for loooping rows
for (student, row) in student_pandas.iterrows():
    print(row.marks)