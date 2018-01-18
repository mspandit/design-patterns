import abc


class NamedEntity(metaclass=abc.ABCMeta):
    def __init__(self, name, implementation):
        super(NamedEntity, self).__init__()
        self.name = name
        self.implementation = implementation


class Chatter(NamedEntity):
    def __init__(self, name, implementation):
        super(Chatter, self).__init__(name, implementation)

    def get_response(self, prompt):
        self.implementation.listen_to(prompt)
        return self.implementation.get_response()


class ChatterImplementor(metaclass=abc.ABCMeta):
    def __init__(self):
        super(ChatterImplementor, self).__init__()

    @abc.abstractmethod
    def listen_to(self, prompt):
        pass

    @abc.abstractmethod
    def get_response(self):
        pass


class HumanChatter(ChatterImplementor):
    def __init__(self):
        super(HumanChatter, self).__init__()

    def listen_to(self, prompt):
        print(prompt)

    def get_response(self):
        return input()


class BotChatter(ChatterImplementor):
    def __init__(self):
        super(BotChatter, self).__init__()

    def listen_to(self, _):
        pass

    def get_response(self):
        return "I'm sorry Dave, I'm afraid I can't do that."


import unittest

class TestMethods(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(TypeError):
            c = ChatterImplementor()

    def test_1(self):
        def get_named_entity():
            return Chatter("John Doe", HumanChatter())
        c = get_named_entity()
        self.assertEqual("Fine, thanks!", c.get_response("Hello, how are you?"))

    def test_2(self):
        def get_named_entity():
            return Chatter("Bot 101", BotChatter())
        c = get_named_entity()
        self.assertEqual("I'm sorry Dave, I'm afraid I can't do that.", c.get_response("Hello, how are you?"))


if __name__ == '__main__':
    unittest.main()
