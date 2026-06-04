grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV03", "name": "Trần Thị C", "info": (7.0, 9.0)},
    {"stt": 4, "id": "SV04", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]
# name_list = grade_book[0]['name'].split()
# print(f'Họ: {name_list[0]}, tên đệm: {name_list[1]}, tên: {name_list[2]}')
# full_name = " ".join(name_list)
# print(f'Họ và tên: {full_name}')

def print_student():
    print('---DANH SÁCH SINH VIÊN---')
    for student in grade_book:
        # print(f'{student['id']:<7} | {student['name']:<20} | {student['info'][0]:<10} | {student['info'][1]:<10}')
        print('{id:<7} | {name:<20} | {info[0]:<10} | {info[1]:<10}'.format_map(student))
print_student()