# Nếu số nhập vào là 1 thì in 'Xin chào'
# số nhập vào là 0 thì in 'Tạm biệt'
# Đến khi nào nhập 0 thì dừng
# number = 1
# while number != 0:
#     number = int(input('Nhập 0 hoặc 1'))
#     if number == 1:
#         print('Xin chào')
#     elif number == 0:
#         print('Tạm biệt')
#     else:
#         print('Không hợp lệ')

# In menu và thực hiện chức năng:
# ---MENU---
# 1. Nhập tên
# 2. Xóa tên
# 3. Thoát
# Chọn 1 thì sau khi nhập tên in 'Xin chào ...'
# Chọn 2 thì in 'Tạm biệt ...', sau đó xóa trắng tên
number = 0
while number != 3:
    print(" -- MENU --")
    print("1. Nhập tên")
    print("2. Xóa tên")
    print("3. Thoát")
    number = int(input('Nhập vào lựa chọn của bạn: (Từ 1 - 3)'))
    match number:
        case 1:
            name = input("Nhập tên cần thêm: ")
            print(f"Xin chào {name}")
        case 2:
            print(f"Tạm biệt {name}")
            name = ""
        case 3: 
            print("Đã thoát")
        case _:
            print("Lựa chọn không hợp lệ!!!")