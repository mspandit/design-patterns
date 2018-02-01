import abc


class Visitor(metaclass=abc.ABCMeta):
    """
    Declares a Visit operation for each class of ConcreteElement in the object
    structure. The operation's name and signature identifies the class that
    sends the visit request to the visitor. That lets the visitor determine the
    concrete class of the element being visited. Then the visitor can access the
    element directly through its particular interface.
    """
    def __init__(self):
        super(Visitor, self).__init__()

    @abc.abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abc.abstractmethod
    def visit_concrete_element_b(self, element):
        pass


class ConcreteVisitor1(Visitor):
    """
    Implements each operation declared by Visitor. Each operation implements a
    fragment of the algorithm defined for the corresponding class of object in
    the structure. ConcreteVisitor provides the context for the algorithm and
    stores its local state. This state often accumulates results during the
    traversal of the structure.
    """
    def __init__(self):
        super(ConcreteVisitor1, self).__init__()

    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass


class ConcreteVisitor2(Visitor):
    """
    Implements each operation declared by Visitor. Each operation implements a
    fragment of the algorithm defined for the corresponding class of object in
    the structure. ConcreteVisitor provides the context for the algorithm and
    stores its local state. This state often accumulates results during the
    traversal of the structure.
    """
    def __init__(self):
        super(ConcreteVisitor2, self).__init__()

    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass


class Element(metaclass=abc.ABCMeta):
    """Defines an Accept operation that takes a visitor as an argument."""
    def __init__(self):
        super(Element, self).__init__()

    @abc.abstractclass
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    """Implements an Accept operation that takes a visitor as an argument."""
    def __init__(self):
        super(ConcreteElementA, self).__init__()

    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(Element):
    """Implements an Accept operation that takes a visitor as an argument."""
    def __init__(self):
        super(ConcreteElementA, self).__init__()

    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)
