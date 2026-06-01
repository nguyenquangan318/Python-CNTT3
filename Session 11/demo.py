gender = ('Nam','Nữ','Khác')
a,b,c = gender

student = {
    'id': 1,
    'full_name': 'Nguyen Van A'
}
# print(student['id'])
# print(student.get('id1', 'Sinh viên chưa có id'))

student['email'] = 'A@gmail.com'
print(student)
student['full_name'] = 'Nguyen Thi B'
print(student)

student.pop('email')
print(student)
del student['id']
print(student)

for key in student.keys():
    print(key)
    
for value in student.values():
    print(value)
    
print(student.items())
for key, value in student.items():
    print(key, value)