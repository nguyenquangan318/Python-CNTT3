# for biến_chạy in range(start, stop, step):

# In ra các số từ 5 - 0
for i in range(5, -1, -1):
    print(i)
    
# Từ 1 - 20
# Nếu chia hết cho 3, in 'Số ... chia hết cho 3'
# Nếu chia hết cho 5, in 'Số ... chia hết cho 5'
# Nếu chia hết cho 3 và 5, in 'Số ... chia hết cho 3 và 5'
for i in range(3, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Số {i} chia hết cho 3 và 5")
    elif i % 3 == 0:
        print(f"Số {i} chia hết cho 3")
    elif i % 5 == 0:
        print(f"Số {i} chia hết cho 5")