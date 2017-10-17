import unittest
import math


class Testclass01(unittest.TestCase):

    def testCase01(self):
        mystr = 'ASHWIN'
        myint = 999
        self.assertTrue(isinstance(mystr, str))
        self.assertTrue(isinstance(myint, int))

    def testCase02(self):
        self.assertFalse(isinstance(math.pi, int))

if __name__ == '__main__':
    unittest.main()