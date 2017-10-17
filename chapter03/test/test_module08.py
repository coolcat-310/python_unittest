
import unittest
import test_me


class TestClass09(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(test_me.add(2,3), 5)
        print('In testCase01()')

    def testCase02(self):
        self.assertEqual(test_me.mul(2,3), 6)
        print('In testCase02()')

    def testCase03(self):
        self.assertEqual(test_me.div(10,2),5)
        print('In testCase03()')