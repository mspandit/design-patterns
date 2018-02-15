class Facade(object):
    """
    Knows which subsystem classes are responsible for a request.
    Delegates client requests to appropriate subsystem objects.
    """
    def __init__(self):
        super(Facade, self).__init__()

        