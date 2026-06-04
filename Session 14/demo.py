# first_num = 10
def sum(first_num = 0, second_num = 0):
    '''Hàm tính tổng 2 số

    Args:
        first_num (int): Số thứ nhất
        second_num (int): số thứ hai

    Returns:
        int: Tổng của 2 số
    '''
    print(f'Tổng của {first_num} và {second_num} là {first_num+second_num}')
    return first_num + second_num

return_value = sum(5)
# print(first_num)
print(return_value)