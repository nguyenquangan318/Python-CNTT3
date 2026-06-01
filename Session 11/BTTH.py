product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True:
    choice = input('''===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
Lựa chọn của bạn: ''')
    match choice:
        case '1':
            if(product_list == []):
                print('Danh sách sản phẩm hiện đang trống.')
                continue
            print('Danh sách sản phẩm hiện tại:')
            for i, value in enumerate(product_list):
                print(f'{i + 1}. Mã SP: {value['product_id']} | Tên SP: {value['product_name']} | Giá: {value['price']} | Số lượng: {value['quantity']}')
        case '2':
            check = False
            input_id = input('Nhập mã sản phẩm: ').upper().strip()
            for product in product_list:
                if(product.get('product_id') == input_id):
                    print('Mã bị trùng')
                    check = True
                    break
            if(not check):
                input_name = input('Nhập tên sản phẩm: ')
                input_price = int(input('Nhập giá sản phẩm: '))
                input_quantity = int(input('Nhập số lượng sản phẩm'))
                if(input_price < 0 or input_quantity < 0):
                    print('giá và số lượng phải >= 0')
                    continue
                new_product = {
                    "product_id": input_id,
                    "product_name": input_name,
                    "price": input_price,
                    "quantity": input_quantity 
                }
                product_list.append(new_product)
        case '3':
            product_id = input('Nhập mã sản phẩm cần cập nhật')
            product_id = product_id.strip().upper()
            check = False
            # Duyệt từng sản phẩm
            for product in product_list:
                # Nếu có mã trùng với mã đã nhập
                if product_id == product.get('product_id'):
                    check = True
                    # Tiến hành cập nhật và thoát vòng lặp
                    input_name = input('Nhập tên sản phẩm: ')
                    input_price = int(input('Nhập giá sản phẩm: '))
                    input_quantity = int(input('Nhập số lượng sản phẩm'))
                    if(input_price < 0 or input_quantity < 0):
                        print('giá và số lượng phải >= 0')
                        break
                    product['product_name'] = input_name
                    product['price'] = input_price
                    product['quantity']= input_quantity
                    print('Cập nhật thành công')
                    break
            # Nếu hết vòng lặp mà vẫn chưa tìm thấy thì in thông báo
            if not check:
                print('Không tìm thấy sản phẩm')
        case '4':
            product_id = input('Nhập mã sản phẩm cần xóa')
            product_id = product_id.strip().upper()
            check = False
            for i, product in enumerate(product_list):
                if(product['product_id'] == product_id):
                    check = True
                    product_list.pop(i)
                    break
            if not check:
                print('Không tìm thấy sản phẩm cần xóa')
        case '5':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')