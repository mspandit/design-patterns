import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Defines a common interface for RealSubject and Proxy so that a Proxy can be 
    used anywhere a RealSubject is expected.
    """
    def __init__(self):
        super(Subject, self).__init__()
        
    @abc.abstractmethod
    def request():
        pass


class Proxy(Subject):
    """
    Maintains a reference that lets the proxy access the real subject. Proxy
    may refer to a Subject if the RealSubject and Subject interfaces are the
    same.
    
    Provides an interface identical to Subject's so that a proxy can be 
    substituted for the real subject.
    
    Controls access to the real subject and may be responsible for creating and
    deleting it.
    
    Remote proxies are responsible for encoding a request and its arguments and
    for sending the encoded request to the real subject in a different address
    space.
    
    Virtual proxies may cache additional information about the real subject so
    that they can postpone accessing it.
    
    Protection proxies check that the caller has the access permissions required
    to perform a request.
    """
    def __init__(self, realSubject):
        super(Proxy, self).__init__()
        self.realSubject = realSubject
    
    def request():
        self.realSubject.request()


class RealSubject(Subject):
    """Defines the real object that the proxy represents"""
    def __init__(self):
        super(RealSubject, self).__init__()
    
    def request():
        pass