class Student:
    def __init__(self, id, name, age = 18):
        self.__id = id
        self.age = age
        self.name = name
        
    def say_hello(self):
        print(f'Hello {self.name}')
        
    # def get_id(self):
    #     return self.__id
    @property
    def id(self):
        return self.__id
    
    # def set_id(self, new_id):
    #     self.__id = new_id
    @id.setter
    def id(self, new_id):
        self.__id = new_id
    
    @staticmethod
    def check_age(age):
        return age >= 18
    
s1 = Student(1, 'Nguyễn Văn A')
# age = int(input('Nhập tuổi'))
# if(Student.check_age(age)):
#     s2 = Student(2, 'Nguyễn Thị B', age)
s1.say_hello()
print(s1.id)
s1.id = 5
print(s1.id)
print(s1.name)
s1.name = 'Nguyễn Văn C'
print(s1.name)
