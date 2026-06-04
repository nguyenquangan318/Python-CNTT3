grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV03", "name": "Trần Thị C", "info": (9.0, 9.0)},
    {"stt": 4, "id": "SV04", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

def print_student():
    print('---DANH SÁCH SINH VIÊN---')
    for student in grade_book:
        # print(f'{student['id']:<7} | {student['name']:<20} | {student['info'][0]:<10} | {student['info'][1]:<10}')
        print('{id:<7} | {name:<20} | {info[0]:<10} | {info[1]:<10}'.format_map(student))
names = [student['name'] for student in grade_book]
names.sort()
print(names)
# Sắp xếp danh sách sinh viên theo tên
grade_book.sort(key = lambda student: student['name'], reverse=True)
print_student()
# Sắp xếp danh sách sinh viên theo điểm trung bình
grade_book.sort(key = lambda student: (student['info'][0] + student['info'][1]) / 2, reverse=True)
grade_asc = sorted(grade_book, key = lambda student: (student['info'][0] + student['info'][1]) / 2)
print_student()