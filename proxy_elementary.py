import unittest
import os
import time
import abc
from multiprocessing import Process, Queue


class AbstractFile(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractFile, self).__init__()
    
    @abc.abstractmethod
    def contents(self):
        pass


class File(AbstractFile):
    def __init__(self, filename):
        super(File, self).__init__()
        self.filename = filename
    
    def contents(self):
        f = open(self.filename, mode="r")
        contents = f.read()
        f.close()
        return contents


class ProxiedFile(AbstractFile):
    def __init__(self, filename):
        super(ProxiedFile, self).__init__()
        self.realFile = File(filename)
        self.cont = self.realFile.contents()
        
    def contents(self):
        return self.cont


def readContent(ppf):
    ppf.queue.put(ppf.realFile.contents())


class ParallelProxiedFile(AbstractFile):
    def __init__(self, filename):
        super(ParallelProxiedFile, self).__init__()
        self.cont = ""
        self.realFile = File(filename)
        self.queue = Queue()
        self.contentReading = Process(target=readContent, args=(self,))
        self.contentReading.start()

    def contents(self):
        self.cont = self.queue.get()
        self.contentReading.join()
        return self.cont
        

NUM_TEST_FILES = 30

class TestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for filenum in range(NUM_TEST_FILES):
            f = open("testfile%d" % filenum, mode='w')
            f.write("XO" * filenum * 1024 * 1024)
            f.close()
    
    def assert_all(self, files):
        for filenum, f in enumerate(files):
            self.assertEqual(2 * filenum * 1024 * 1024, len(f.contents()))
    
    def test0(self):
        start_time = time.time()
        files = [File("testfile%d" % filenum) for filenum in range(NUM_TEST_FILES)]
        self.assert_all(files)
        end_time = time.time()
        print("test0 took %f seconds" % (end_time - start_time))
    
    def test1(self):
        start_time = time.time()
        files = [ProxiedFile("testfile%d" % filenum) for filenum in range(NUM_TEST_FILES)]
        self.assert_all(files)
        end_time = time.time()
        print("test1 took %f seconds" % (end_time - start_time))

    def test2(self):
        start_time = time.time()
        files = [ParallelProxiedFile("testfile%d" % filenum) for filenum in range(NUM_TEST_FILES)]
        self.assert_all(files)
        end_time = time.time()
        print("test2 took %f seconds" % (end_time - start_time))
    
    @classmethod
    def tearDownClass(cls):
        for filenum in range(NUM_TEST_FILES):
            os.remove("testfile%d" % filenum)


if __name__ == "__main__":
    unittest.main()