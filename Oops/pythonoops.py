
# def map():
#     material = 'house'
#     print(f'I build {material}')

# class map():
#     # Coustom execution
#     def __int__(self, material):
#         self.material = 'House'
#         print(f'I build {material}')
#     def adder(self):
#         x = 2+ 2
#         return x
#
#
# house1 = map('Big House')
# house2 = map('Small House')
# house3 = map('2Bhk')
# house4 = map('tower')

# house = map()
# house2 = map()
# house3 = map()
#
# house.material = 'newHouse'
# house.material2 = 'Vary Good house'
# print(house.material2)

# house2.material = 'newHouse'
# print(house.material)
#
# house3.material = 'newHouse'
# print(house.material)


# A sample Class with init methods
class Person:
    # init method or constructor
    def __init__(self, name, age):
        # this->name = name
        self.name = name
        self.age = age
    # Sample method
    def say_hi(self):
        print('Hello, my name is', self.name, self.age )

p1 = Person('Nikhil', 35)
p1.say_hi()


# print(p1.name)
# print(p1.age)
