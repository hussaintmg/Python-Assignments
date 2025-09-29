class Father:
    def skills(self):
        return "Scientist"

class Mother:
    def skills(self):
        return "Freelancer"

class Child(Father, Mother):
    def skills(self):
        return f"{Father.skills(self)} and {Mother.skills(self)}"


c = Child()
print(c.skills())
