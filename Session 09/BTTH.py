branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True:
    choice = input('''===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): ''')
    match choice:
        case '1':
            print('--- BÁO CÁO DOANH THU TỔNG HỢP ---')
            print(f'{'Tên Cơ Sở':<30}| {'Doanh Thu':<15}| {'Trạng Thái':<10}')
            print('-'*65)
            for i, branch in enumerate(branch_names):
                print(f'{branch:<30}| {daily_revenues[i]:<15}| {'Đạt' if target_achieved[i] else 'Không đạt':<10}')
            print('-'*65)
            print(f'=> TỔNG DOANH THU TOAN VUNG: {sum(daily_revenues)} VND')
        case '2':
            max_revenue = max(daily_revenues)
            min_revenue = min(daily_revenues)
            max_index = daily_revenues.index(max_revenue)
            min_index = daily_revenues.index(min_revenue)
            max_branch = branch_names[max_index]
            min_branch = branch_names[min_index]
            print(f'''--- THỐNG KE CO SỞ NOI BAT
- Cơ sở co doanh thu CAO NHẬT: {max_branch} ({max_revenue})
- Cơ sở có doanh thu THẤP NHẤT: {min_branch} ({min_revenue})''')
        case '3':
            failed_branches = []
            for i, target in enumerate(target_achieved):
                if not target:
                    failed_branches.append(branch_names[i])
            print(f'''DANH SACH CO SO CAN HO TRO TRA CỨU ĐƯỢC
{failed_branches}''')
        case '4':
            print('Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!')
            break
        case _:
            print('[Loi] Lua chon khong hợp le, vui long nhap lai số từ 1 đen 4!')