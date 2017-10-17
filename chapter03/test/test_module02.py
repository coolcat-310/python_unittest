import unittest
import inspect

class TestClass02(unittest.TestCase):

    def testCase02(self):
        print("\nRunning Test Method : " + inspect.stack() [0][3])

    def testCase01(self):
        print("\nRunning Test Method: " + inspect.stack() [0][3])

if __name__ == '__main__':
    unittest.main(verbosity=2)