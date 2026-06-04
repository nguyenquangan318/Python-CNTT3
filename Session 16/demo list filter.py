grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV03", "name": "Trần Thị C", "info": (9.0, 9.0)},
    {"stt": 4, "id": "SV04", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

# Tạo ra danh sách chỉ chứa tên sinh viên có điểm trung bình > 8
# ["Trần Thị C", "Nguyễn Văn D"]
# Dùng vòng lặp for
names = []
for student in grade_book:
    avg = (student['info'][0] + student['info'][1]) / 2
    if avg > 8:
        names.append(student['name'])
print(names)

# Dùng phương thức filter
# Dùng hàm bình thường
def get_name(student):
    avg = (student['info'][0] + student['info'][1]) / 2
    return avg > 8
names = list(filter(get_name, grade_book))
print(names)
# Dùng hàm lambda
names = list(filter(lambda student: (student['info'][0] + student['info'][1]) / 2 > 8, grade_book))
print(names)

# Dùng list comprehension
names = [student['name'] for student in grade_book if (student['info'][0] + student['info'][1]) / 2 > 8]
print(names)

# Tổng điểm của tất cả sinh viên
total = sum([student['info'][0] + student['info'][1] for student in grade_book])
print(total)