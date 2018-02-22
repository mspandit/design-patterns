import unittest
import abc
import re


# expression ::== literal | addition | subtraction | multiplication | division | '(' expression ')'
# addition ::== expression '+' expression
# subtraction ::== expression '-' expression
# multiplication ::== expression '*' expression
# division ::== expression '/' expression
# literal ::= [0-9]+


class AbstractExpression(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractExpression, self).__init__()
        
    @abc.abstractmethod
    def evaluate(self, string):
        pass


class Expression(AbstractExpression):
    def __init__(self):
        super(Expression, self).__init__()
    
    def evaluate(self, string):
        l = Literal().evaluate(string) 
        if l:
            return l
        if string[0] == '(' and string[-1] == ')':
            e = Expression().evaluate(string[1:-1])
            if e:
                return e
        a = Addition().evaluate(string)
        if a:
            return a
        s = Subtraction().evaluate(string) 
        if s:
            return s


class Literal(AbstractExpression):
    def __init__(self):
        super(Literal, self).__init__()
        
    def evaluate(self, string):
        if re.match('^[0-9]+$', string): 
            return int(string)
        else:
            return None


class Addition(AbstractExpression):
    def __init__(self):
        super(Addition, self).__init__()

    def evaluate(self, string):
        potentialAddends = string.split('+')
        if len(potentialAddends) > 1:
            for ix, addend in potentialAddends[0:-1]:
                lhs = Expression().evaluate('+'.join(potentialAddends[0:ix + 1]).strip())
                if lhs:
                    rhs = Expression().evaluate('+'.join(potentialAddends[ix + 1:]).strip())
                    if rhs:
                        return lhs + rhs
        return None


class Subtraction(AbstractExpression):
    def __init__(self):
        super(Subtraction, self).__init__()
    
    def evaluate(self, string):
        potentialSubtrahends = string.split('-')
        if len(potentialSubtrahends) > 1:
            for ix, subtrahend in potentialSubtrahends[0:-1]:
                lhs = Expression().evaluate('-'.join(potentialSubtrahends[0:ix + 1]).strip())
                if lhs:
                    rhs = Expression().evaluate('-'.join(potentialSubtrahends[ix + 1:]).strip())
                    if rhs:
                        return lhs - rhs
        return None


class TestMethods(unittest.TestCase):
    def test0(self):
        e = Expression()
        self.assertEqual(2, e.evaluate("(1 + 1)"))

    def test1(self):
        self.assertEqual(2, Expression().evaluate("1+1"))
        self.assertEqual(14, Expression().evaluate("12+ 2"))
    
    def test2(self):
        self.assertEqual(4, Expression().evaluate("5 - 1")) 

    def test3(self):
        self.assertEqual(10, Expression().evaluate("((4 + 5) + (5 - 4))"))


if __name__ == "__main__":
    unittest.main() 