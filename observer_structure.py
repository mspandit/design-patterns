import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Knows its observers. Any number of Observer objects may observe a subject. 
    Provides an interface for attaching and detaching Observer objects.
    """
    def __init__(self):
        super(Subject, self).__init__()
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class ConcreteSubject(Subject):
    """
    Stores state of interest to ConcreteObserver objects. Sends a notification 
    to its observers when its state changes.
    """
    def __init__(self, state=None):
        super(ConcreteSubject, self).__init__()
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


class Observer(metaclass=abc.ABCMeta):
    """
    Defines an updating interface for objects that should be notified of 
    changes in a subject.
    """
    def __init__(self):
        super(Observer, self).__init__()
    
    @abc.abstractmethod
    def update(self):
        pass


class ConcreteObserver(Observer):
    """
    Maintains a reference to a ConcreteSubject object. Stores state that should 
    stay consistent with the subject's. Implements the Observer updating 
    interface to keep its state consistent with the subject's.
    """
    def __init__(self, subject):
        super(ConcreteObserver, self).__init__()
        self.subject = subject

    def update(self):
        # Optionally retrieve state from subject.
        pass
        