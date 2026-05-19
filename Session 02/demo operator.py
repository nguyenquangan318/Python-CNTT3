first_number = float(input('Nhập số thứ nhất: '))
second_number = float(input('Nhập số thứ hai: '))

# Tính tổng của 2 số đã nhập và in ra kết quả
print(f'kết quả là {first_number + second_number}')

# in ra kết quả so sánh xem số thứ 
# nhất có lớn hơn số thứ hai không?
print(first_number > second_number)

# in ra kết quả số thứ nhất lẻ và số thứ hai chẵn
# hoặc cả 2 số lớn hơn 10
print((first_number % 2 == 1 and second_number % 2 == 0) or (first_number > 10 and second_number > 10))