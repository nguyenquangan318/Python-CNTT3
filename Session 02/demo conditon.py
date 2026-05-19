math_score = float(input('Nhập điểm toán'))
# physic_score = float(input('Nhập điểm lý'))
# lit_score = float(input('Nhập điểm văn'))

# Nếu một trong 3 điểm < 5 thì in ra 'Không đủ điều kiện thi'
# if math_score < 5 or physic_score < 5 or lit_score < 5:
#     print('Không đủ điều kiện thi')
# else:
#     print('Đủ điều kiện thi')
    
# Nếu điểm toán < 5 thì in ra 'Yếu toán'
# Nếu 5 < điểm toán < 7 thì in ra 'TB toán'
# Nếu 7 < điểm toán < 8 thì in ra 'khá toán'
# Nếu điểm toán > 8 thì in ra 'Gỏi toán'
# if math_score < 5:
#     print('Yếu toán')
# elif math_score < 7:
#     print('TB toán')
# elif math_score < 8:
#     print('Khá toán')
# else: print('Giỏi toán')


# Nếu điểm toán = 5 thì in ra 'Yếu toán'
# Nếu điểm toán = 7 thì in ra 'TB toán'
# Nếu  điểm toán = 8 thì in ra 'khá toán'
# Nếu điểm toán = 9 hoặc 10 thì in ra 'Gỏi toán'
match math_score:
    case 5:
        print('Yếu toán')
    case 7:
        print('TB toán')
    case 8:
        print('Khá toán')
    case 9 | 10:
        print('Giỏi toán')
    case _:
        print('Đề bài không có dữ liệu')