class GrandParent:
    def family_name(self):
        print("Family Name: Khan")

class Parent(GrandParent):
    def occupation(self):
        print("Occupation: Engineer")

class Child(Parent):
    def hobby(self):
        print("Hobby: Painting")


c = Child()
c.family_name()
c.occupation()
c.hobby()
