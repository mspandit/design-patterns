class Memento(object):
    """
    Stores internal state of the Originator object. The memento may store as 
    much or as little of the originator's internal state as necessary at its 
    originator's discretion. 
    
    Protects against access by objects other than the originator. Mementos have 
    effectively two interfaces. Caretaker sees a narrow interface to Memento--it 
    can only pass the memento to other objects. Originator, in contrast, sees a 
    wide interface, one that lets it access all the data necessary to restore 
    itself to its previous state. Ideally, only the originator that produced the 
    memento would be permitted to access the memento's internal state.
    """
    def __init__(self, state=None):
        super(Memento, self).__init__()
        self.state = state
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state


class Originator(object):
    """
    Creates a memento containing a snapshot of its current internal state. Uses 
    the memento to restore its internal state.
    """
    def __init__(self, state=None):
        super(Originator, self).__init__()
        self.state = state

    def setMemento(self, memento):
        self.state = memento.getState()
    
    def createMemento(self):
        return Memento(self.state)


class Caretaker(object):
    """
    Is responsible for the memento's safekeeping. Never operates on or examines 
    the contents of a memento.
    """
    def __init__(self):
        super(Caretaker, self).__init__()
        