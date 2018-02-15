import abc
import re
from decorator_elementary import Person, Character, Gryffindor, Slytherin, Ghost
from decorator_elementary import Role

class AbstractSpanishSpeaking(metaclass=abc.ABCMeta):
    def __init__(self, person):
        super(AbstractSpanishSpeaking, self).__init__()
        self.person = person
    
    @abc.abstractmethod
    def presentate(self):
        pass


class SpanishSpeaking(AbstractSpanishSpeaking):
    def __init__(self, person):
        super(SpanishSpeaking, self).__init__(person)

    def presentate(self):
        match = re.match(
            'My name is ([a-zA-Z ]*).\nI belong to House Gryffindor. We do what is right.', 
            self.person.introduce())
        if match:
            return "Me llamo %s. Pertenezco a la Casa Gryffindor. Hacemos lo correcto." % match.group(1)
        match = re.match('My name is ([a-zA-Z ]*).', self.person.introduce())
        if match:
            return "Me llamo %s." % match.group(1)


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
        shp = SpanishSpeaking(hp)
        self.assertEqual("Me llamo Harry Potter.", shp.presentate())

    def test_2(self):
        hp = Gryffindor(Character("Harry Potter"))
        self.assertEqual("My name is Harry Potter.\nI belong to House Gryffindor. We do what is right.", hp.introduce())
        shp = SpanishSpeaking(hp)
        self.assertEqual("Me llamo Harry Potter. Pertenezco a la Casa Gryffindor. Hacemos lo correcto.", shp.presentate())

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
