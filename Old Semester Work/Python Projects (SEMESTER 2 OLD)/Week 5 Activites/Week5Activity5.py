class Person:
    def __init__(self,name,hair):
        self.name = name
        self.hair = hair
    def haircolor(self):
        return self.hair
    def personname(self):
        return self.name

p1 = Person('Kenneth', 'black')
print('My name is',p1.personname(),'and the color of my hair is',p1.haircolor())