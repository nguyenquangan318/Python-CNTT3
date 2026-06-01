choice = ''
raw_input = "  nGuyen vaN aN ; 2004  "
while choice != '4':
    choice = input('''
    ===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
    1. Hiển thị chuỗi dữ liệu gốc
    2. Chuẩn hóa Họ tên và tính Tuổi
    3. Tạo Mã ID và Email tự động
    4. Thoát chương trình
    =====================================
    Nhập lựa chọn của bạn (1-4):
    ''')
    match choice:
        case '1':
            print(raw_input)
        case '2':
            full_name = raw_input.split(';')[0]
            full_name = full_name.strip()
            full_name = full_name.title()
            birth_year = raw_input.split(';')[1]
        # case 3:
        case '4':
            print('Thoát chương trình')
        case _:
            print('Lựa chọn không hợp lệ')