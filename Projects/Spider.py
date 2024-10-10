class Animal:
    def __init__(self, arms, legs):
        self._arms = arms
        self._legs = legs
    def limbs(self):
        return self._arms + self._legs

spider = Animal(4, 4)
print(f'Total limbs are {spider.limbs()}')
