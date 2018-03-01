import unittest
import os
import fsevents # after `pip install macfsevents`
import time


class Observer(object):
    """docstring for Observer"""
    def __init__(self, filename):
        super(Observer, self).__init__()
        self.filename = filename
        f = open(self.filename, mode="r")
        self.contents = f.read()
        f.close()
        self.fsobserver = fsevents.Observer()
        self.fsobserver.start()
        
        def callback(event):
            if self.filename in event.name:
                f = open(self.filename, mode="r")
                self.contents = f.read()
                f.close()
        
        self.stream = fsevents.Stream(callback, '.', file_events=True)
        self.fsobserver.schedule(self.stream)

    def stop(self):
        self.fsobserver.unschedule(self.stream)
        self.fsobserver.stop()


class TestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        f = open("test.config", mode="w")
        f.write("test")
        f.close()
    
    def test_0(self):
        """Just ensure setUpClass and tearDownClass work."""
        self.assertEqual(True, True)
    
    def test_1(self):
        o = Observer("test.config")
        time.sleep(1)
        self.assertEqual("test", o.contents) 
        f = open("test.config", mode="w")
        f.write("altered")
        f.close()
        time.sleep(1)
        self.assertEqual("altered", o.contents)
        o.stop() 
    
    @classmethod
    def tearDownClass(cls):
        os.remove("test.config")


if __name__ == "__main__":
    unittest.main() 
