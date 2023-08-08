# Exercise
class kattle:
    # Universal Attribute
    # Class Attribute
    power_src = 'Electricity'
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch(self):
        self.on = True


kenWood = kattle('kenWood', 100)
melton = kattle('Melton', 20)

print(kenWood.make)
print(melton.make)
print(kenWood.on)

kenWood.switch()
print(kenWood.on)

print('X'*20)

print(kattle.__dict__)
print(kenWood.__dict__)
print(melton.__dict__)
print('X'*20)

kenWood.model = 2019
print(kattle.__dict__)
print(kenWood.__dict__)
print(melton.__dict__)

print('X'*20)
kattle.power_src = 'Solar'

print(melton.power_src)
print(kenWood.power_src)

print(kattle.__dict__)

melton.power_src = 'DC'
print(kattle.__dict__)
print(kenWood.__dict__)
print(melton.__dict__)