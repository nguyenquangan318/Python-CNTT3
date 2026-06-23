class Animal:
    def __init__(self, sound, name):
        self.sound = sound
        self.name = name
        
    def speak(self):
        print(self.sound)
        
class Dog(Animal):
    def __init__(self, sound, name, owner):
        super().__init__(sound, name)
        self.owner = owner
    
    def speak(self):
        print("Chú chó kêu")
        super().speak()
        
dog1 = Dog("Gâu Gâu", "Dug", "An")
dog2 = Dog("Meo Meo", "deg", "Dương")
dog1.speak()
dog2.speak()