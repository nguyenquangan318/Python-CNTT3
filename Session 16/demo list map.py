grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"stt": 3, "id": "SV03", "name": "Trần Thị C", "info": (7.0, 9.0)},
    {"stt": 4, "id": "SV04", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

# Tạo ra danh sách chỉ chứa tên sinh viên
# ["Nguyễn Văn A", "Trần Thị B", "Trần Thị C", "Nguyễn Văn D"]
# Dùng vòng lặp for
names = []
for student in grade_book:
    names.append(student['name'])
print(names)

# Dùng phương thức map
# Dùng hàm bình thường
def get_name(student):
    return student['name']
names = list(map(get_name, grade_book))
print(names)
# Dùng hàm lambda
names = list(map(lambda student: student['name'], grade_book))
print(names)

# Dùng list comprehension
names = [student['name'] for student in grade_book]
print(names)