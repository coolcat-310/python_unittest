import unittest
import inspect

def add(x,y):
    print('We\'re a custom made function: ' + inspect.stack()[0][3])
    return x + y

class TestClass03(unittest.TestCase):

    def testCase01(self):
        print("\nRunning test method: "+ inspect.stack()[0][3])
        self.assertEqual(add(2,3), 5)

    def testCase02(self):
        print("\nRunning test method: " + inspect.stack()[0][3])
        num = 3.14
        self.assertTrue(isinstance(num, float))

    def testCase03(self):
        print("\nRunning test method: " + inspect.stack()[0][3])
        self.assertEqual(add(2, 2), 5)

    def testCase04(self):
        print("\nRunning test method: " + inspect.stack()[0][3])
        num = 3.14
        self.assertTrue(isinstance(num, int))

if __name__ == '__main__':
    unittest.main(verbosity=2)