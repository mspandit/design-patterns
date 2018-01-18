import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self):
        super(Person, self).__init__()

    @abc.abstractmethod
    def introduce(self):
        pass


class Character(Person):
    def __init__(self, name):
        super(Character, self).__init__()
        self.name = name

    def introduce(self):
        return "My name is %s." % self.name


class Role(Person, metaclass=abc.ABCMeta):
    def __init__(self, character):
        super(Role, self).__init__()
        self.character = character

    def introduce(self):
        return self.character.introduce()


class Gryffindor(Role):
    def __init__(self, character):
        super(Gryffindor, self).__init__(character)

    def introduce(self):
        return "%s\nI belong to House Gryffindor. We do what is right." % self.character.introduce()


class Hufflepuff(Role):
    def __init__(self, character):
        super(Hufflepuff, self).__init__(character)

    def introduce(self):
        return "%s\nI belong to House Hufflepuff. We do what is kind." % self.character.introduce()


class Ravenclaw(Role):
    def __init__(self, character):
        super(Ravenclaw, self).__init__(character)

    def introduce(self):
        return "%s\nI belong to House Ravenclaw. We do what is wise." % self.character.introduce()


class Slytherin(Role):
    def __init__(self, character):
        super(Slytherin, self).__init__(character)

    def introduce(self):
        return "%s\nI belong to House Slytherin. We do what is necessary." % self.character.introduce()


class Ghost(Role):
    def __init__(self, character):
        super(Ghost, self).__init__(character)

    def introduce(self):
        return "%s\nI am a ghost. Boo!" % self.character.introduce()


import unittest

class TestMethods(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(TypeError):
            s = Person()
        with self.assertRaises(TypeError):
            s = Role()

    def test_1(self):
        hp = Character("Harry Potter")
        self.assertEqual("My name is Harry Potter.", hp.introduce())

    def test_2(self):
        hp = Gryffindor(Character("Harry Potter"))
        self.assertEqual("My name is Harry Potter.\nI belong to House Gryffindor. We do what is right.", hp.introduce())

    def test_3(self):
        dm = Slytherin(Character("Draco Malfoy"))
        self.assertEqual("My name is Draco Malfoy.\nI belong to House Slytherin. We do what is necessary.", dm.introduce())

    def test_4(self):
        nhn = Gryffindor(Ghost(Character("Nearly Headless Nick")))
        self.assertEqual("My name is Nearly Headless Nick.\nI am a ghost. Boo!\nI belong to House Gryffindor. We do what is right.", nhn.introduce())

    def test_5(self):
        nhn = Ghost(Gryffindor(Character("Nearly Headless Nick")))
        self.assertEqual("My name is Nearly Headless Nick.\nI belong to House Gryffindor. We do what is right.\nI am a ghost. Boo!", nhn.introduce())


if __name__ == '__main__':
    unittest.main()
