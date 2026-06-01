full_name = 'nguyen van a'
# print(full_name[0])

# string_name[start : stop : step]
date_of_birth = '30/04/2026'
date = 0
month = 0
year = 0
date = date_of_birth[:2]
# date = date_of_birth[0:2:1]
month = date_of_birth[3:5]
year = date_of_birth[6:12:1]
reverse = date_of_birth[::-1]
print(date)
print(month)
print(year)
print(reverse)