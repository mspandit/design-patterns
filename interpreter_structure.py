import abc


class AbstractExpression(metaclass=abc.ABCMeta):
    """
    Declares an abstract Interpret operation that is common to all nodes in the
    abstract syntax tree.
    """
    def __init__(self):
        super(AbstractExpression, self).__init__()

    @abc.abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(AbstractExpression):
    """
    Implements an interpret operation associated with terminal symbols in the 
    grammar.
    An instance is required for every terminal symbol in a sentence
    """
    def __init__(self):
        super(TerminalExpression, self).__init__()

    def interpret(self, context):
        pass


class NonterminalExpression(AbstractExpression):
    """
    One such class is required for every rule R ::= R1R2...Rn in the grammar.
    Maintains instance variables of type AbstractExpression for each of the
    symbols R1 through Rn
    Implements the Interpret operation for nonterminal symbols in the grammar.
    Interpret typically calls itself recursively on the variables representing 
    R1 through Rn
    """
    def __init__(self):
        super(NonterminalExpression, self).__init__()

    def interpret(self, context):
        pass


class Context(object):
    """Contains information that's global to the interpreter"""
    def __init__(self):
        super(Context, self).__init__()


class Client(object):
    """
    Builds (or is given) an abstract syntax tree representing a particular
    sentence in the language that the grammar defines. The abstract syntax
    tree is assembled from instances of the NonterminalExpression and 
    TerminalExpression classes. 
    Invokes the Interpret operation.
    """
    def __init__(self, arg):
        super(Client, self).__init__()
        self.arg = arg
        