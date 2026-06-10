try:
    number = int(input('Nhập số:'))
    print(10 / number)
except ValueError:
    print(f'Lỗi: {ValueError}')
except:
    print('Lỗi không xác định')
else:
    print('Chương trình không có lỗi')