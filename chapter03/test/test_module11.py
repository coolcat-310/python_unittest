import unittest

class testClass(unittest.TestCase):

    def testCase01(self):
        """
        This is a test method.....
        """
        print(self.id())
        print(self.shortDescription())
        self.fail()
