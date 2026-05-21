# for i in range(5):
#     print(f'Vòng ngoài lần thứ {i}')
#     for j in range(3):
#         print(f'Vòng trong lần thứ {j}')
#     print()


# Cho người dùng nhập chiều dài và chiều rộng
# In ra hình chữ nhật sử dụng dấu *
# width = int(input('Nhập chiều dài: '))
# height = int(input('Nhập chiều rộng: '))
# 4,3
# ****
# ****
# ****
# for i in range(height):
#     for j in range(width):
#         print('*', end = ' ')
#     print()


height = int(input('Nhập chiều cao tam giác: '))
# height = 5
# *
# **
# ***
# ****
# *****
for i in range(height):
    # In 1 dòng
    for j in range(i+1):
        print('*', end='')
    print()
    
# *****
# ****
# ***
# **
# *
for i in range(height):
    for j in range(height - i):
        print('*', end='')
    print()
    
    
#    *
#   **
#  ***
# ****
#*****
# C1:
for i in range(height):
    for j in range(height - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        print('*', end='')
    print()
# C2:
for i in range(1, height+1):
    print(' ' * (height - i) + '*' * i)
# C3:
for i in range(height):
    for j in range(height):
        if(j >= height - i - 1):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()