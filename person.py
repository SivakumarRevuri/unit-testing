
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __test_method(self):
        print('Person call')

    def _test_method(self):
        print('protected method')
        self.__test_method()



if __name__ == '__main__':
    p = Person(name = 'Moksha', age=19)
    print(p.name, p.age)

    p._test_method()