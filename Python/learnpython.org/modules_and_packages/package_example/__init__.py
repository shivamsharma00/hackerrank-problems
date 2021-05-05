class Person:
    name = 'shivam'
    age = 10

    def __init__(self, name):
        print('in superclass {}'.format(name))

    @staticmethod
    def new(self):
        print("hello")

# class man(Person):
#     # pass
#     def __init__(self, name):
#         super(self).__init__(name)
#         # super(name)

# my = man("sharma")


# p1 = Person("Shivam")
# print()
# print(repr(p1))
# print()
# print(p1.__dir__())
# print()
# print(dir(p1))
# print()
# print(type(p1).__dict__)


# print(my.name)
# print(isinstance(my, Person))
# my.new()
# 
# del my


class Number:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value