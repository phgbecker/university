class Person(object):
    __id = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Person.__id
        Person.__id += 1
