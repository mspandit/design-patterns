class Context(object):
    """docstring for Context."""
    def __init__(self, strategy):
        super(Context, self).__init__()
        self.strategy = strategy


class Strategy(object):
    """docstring for Strategy."""
    def __init__(self):
        super(Strategy, self).__init__()

    def algorithm_interface(self):
        raise Exception("Not implemented in abstract class.")


class ConcreteStrategyA(object):
    """docstring for ConcreteStrategyA."""
    def __init__(self):
        super(ConcreteStrategyA, self).__init__()

    def algorithm_interface(self):
        # Execute algorithm using strategy A
        pass


class ConcreteStrategyB(object):
    """docstring for ConcreteStrategyB."""
    def __init__(self):
        super(ConcreteStrategyB, self).__init__()

    def algorithm_interface(self):
        # Execute algorithm using strategy B
        pass
