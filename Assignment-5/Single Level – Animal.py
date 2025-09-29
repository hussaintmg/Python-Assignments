class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

a = Animal()
a.make_sound()

d = Dog()
d.make_sound()
