grade_book = [
    {"stt": 1, "id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"stt": 2, "id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]
id = len(grade_book)

def display_grades(book):
    print('--- BẢNG ĐIỂM HỌC SINH ---')
    print(f'{'Mã sv':<7} | {'Tên học sinh':<20} | {'Điểm Toán':<10} | {'Điểm Anh':<10} | {'ĐTB'}')
    print('-'*70)
    for student in book:
        math, eng = student['info']
        avg = (math + eng) / 2
        print(f'{student['id']:<7} | {student['name']:<20} | {math:<10} | {eng:<10} | {avg}')
   
   
def add_student(book):
    check = False
    while True:
        input_id = input("Nhập mã sinh viên")
        for student in book:
            if input_id == student['id']:
                check = True
                print('Mã sinh viên đã tồn tại')
                break
        if not check:
            break
    input_name = input('Nhập tên sinh viên')
    input_math = float(input('Nhập điểm toán'))
    input_eng = float(input('Nhập điểm anh'))
    book.append({
        "stt": book[len(book) - 1]['id'] + 1,
        "id": input_id,
        "name": input_name,
        "info": (input_math, input_eng)
    })
 
while True:
    choice = input('''=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5): ''')
    match choice:
        case '1':
            display_grades(grade_book)
        case '5':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')