import abc

class Component(metaclass=abc.ABCMeta):
    """docstring for Component."""
    def __init__(self):
        super(Component, self).__init__()
        self.children = []

    @abc.abstractmethod
    def operation(self):
        pass

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_child(self, child_index):
        return self.children[child_index]


class Composite(Component):
    """docstring for Composite."""
    def __init__(self):
        super(Composite, self).__init__()

    def operation(self):
        for child in self.children:
            child.operation()


class Leaf(Component):
    """docstring for Leaf."""
    def __init__(self, arg):
        super(Leaf, self).__init__()

    def operation(self):
        # do something useful here.
        pass
