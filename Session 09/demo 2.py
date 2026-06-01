students = ['Huyền', 'Đạt', 'Dương', 'Huy']
# for i in range(len(students)):
#     print(students[i])
for student in students:
    print(student)
# 1.
# 2.
# ...
for i, student in enumerate(students, start = 3):
    print(f'{i+1}. {student}')