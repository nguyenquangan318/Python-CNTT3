students = [{'id':'SV001', 'name':'Nguyen Van A', 'math':8.5, 'physic':7.0, 'chemis':9.0, 'avg':8.17, 'ranking':'Giỏi'}]

def display_students():
    print('DANH SACH SINH VIEN')
    print(f'{'id':<7}| ten |')
    for s in students:
        print(f'{s['id']:<7} | {s['name']}, {s['math']}, {s['physic']}, {s['chemis']}, {s['avg']}, {s['ranking']}')

def ranking(avg):
    if avg < 5:
        return 'Yếu'
    elif avg < 7:
        return 'TB'
    elif avg < 8:
        return 'Khá'
    else:
        return 'Giỏi'

def add_student():
    id = input('Nhập mã sinh viên')
    
    name = input('Nhập tên sinh viên')
    
    math = float(input('Nhập điểm toán'))
    physic = float(input('Nhập điểm lý'))
    chemis = float(input('Nhập điểm hóa'))
    
    avg = (math + physic + chemis) / 3
    students.append({
        'id': id,
        'name': name,
        'math': math,
        'physic': physic,
        'chemis': chemis,
        'avg': avg,
        'ranking': ranking(avg)
    })

def display_statistic():
    great_count = 0
    good_count = 0
    avg_count = 0
    weak_count = 0
    for s in students:
        if s['ranking'] == 'Giỏi':
            great_count += 1
        elif s['ranking'] == 'Khá':
            good_count += 1
        elif s['ranking'] == 'TB':
            avg_count += 1
        else:
            weak_count += 1
    print(f'Giỏi: {great_count}, Khá: {good_count}, TB: {avg_count}, Yếu: {weak_count}')

while True:
    choice = input('''1.Hiển thị danh sách sinh viên
2. Tiếp nhận sinh viên
3. Cập nhật kết quả học tập
4. Xoá sinh viên 
5. Tìm kiếm sinh viên theo mã
6. Tìm kiếm sinh viên theo tên
7. Thống kê
8. Thoát
Lựa chọn của bạn: ''')
    match choice:
        case '1':
            display_students()
        case '2':
            add_student()
        case '6':
            display_statistic()
        case '8':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')