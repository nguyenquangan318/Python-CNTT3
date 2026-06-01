saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "inactive"
    }
]

while True:
    choice = input('''===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
    1. Xem danh sách sổ tiết kiệm
    2. Mở sổ tiết kiệm mới
    3. Cập nhật thông tin sổ tiết kiệm
    4. Tất toán hoặc xóa sổ tiết kiệm
    5. Tính lãi dự kiến khi đến hạn
    6. Kiểm tra điều kiện rút trước hạn
    7. Thoát chương trình
    Lựa chọn của bạn: ''')
    match choice:
        case '5':
            # Nhập mã sổ tiết kiệm và chuẩn hóa
            input_id = input('Nhập mã sổ tiết kiệm cần tính lãi').strip().upper()
            check = False
            # Tìm sổ cần tính lãi
            for account in saving_accounts:
                if account['account_id'] == input_id:
                    check = True
                    # Kiểm tra trạng thái sổ
                    if(account['status'] == 'active'):
                        # Tính lãi và hiển thị tổng tiền
                        interest = account['balance']*account['interest_rate']/100*account['term_months']/12
                        total = account['balance'] + interest
                        print(f'Tiền lãi: {interest}, tiền thực nhận: {total}')      
                    else:
                        # In thông báo nếu sổ inactive
                        print('Trạng thái sổ không active')
                    break
            if not check:
                # In thông báo nếu không tìm thấy
                print('Không tìm thấy sổ tiết kiệm')
        case '6':
            # Nhập mã sổ tiết kiệm và chuẩn hóa
            input_id = input('Nhập mã sổ tiết kiệm cần tính lãi').strip().upper()
            check = False
            # Tìm sổ cần rút trước hạn
            for account in saving_accounts:
                if account['account_id'] == input_id:
                    check = True
                    # Kiểm tra trạng thái sổ
                    if(account['status'] == 'active'):
                        # Nhập số tháng
                        month = int(input('Nhập số tháng thực gửi: '))
                        # Kiểm tra số tháng nguyên dương, nhỏ hơn thực gửi
                        if(month > 0 and month < account['term_months']):
                            # Tính số tiền lãi và tổng tiền
                            # Số tiền gửi * Lãi suất năm / 100 * Kỳ hạn gửi / 12
                            interest = account['balance']*0.5/100*month/12
                            total = account['balance'] + interest
                    else:
                        # In thông báo nếu sổ inactive
                        print('Trạng thái sổ không active')
                    break
            if not check:
                # In thông báo nếu không tìm thấy
                print('Không tìm thấy sổ tiết kiệm')
        case '7':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')