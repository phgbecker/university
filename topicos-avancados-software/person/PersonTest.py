import unittest
from person.Person import Person


class PersonTest(unittest.TestCase):

    def given_person_when_new_instance_then_is_equals(self):
        name = "John Doe"
        age = 21

        person = Person(name, age)

        self.assertEqual(person.name, name)
        self.assertEqual(person.age, age)

    def given_persons_when_new_instance_then_id_is_equals(self):
        john = Person("John Doe", 21)
        jane = Person("Jane Doe", 18)

        self.assertEqual(john.id, 1)
        self.assertEqual(jane.id, 2)


if __name__ == '__main__':
    unittest.main()
