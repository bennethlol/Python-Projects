class Animal:
    def __init__(self, arms, legs, speed):
        self._arms = arms
        self._legs = legs
        self._speed = 5
    def limbs(self):
        return self._arms + self._legs
    def compareSpeed(self, animal2):
       return self._speed > animal2._speed
           

spider = Animal(4, 4, 10)
millipede = Animal(100, 200, 15)
print(f'Total limbs are {spider.limbs()}')
print(f'Total limbs are {millipede.limbs()}')

if spider.compareSpeed(millipede):
    print('Spiders are faster')
else:
    print('Millipedes are faster')