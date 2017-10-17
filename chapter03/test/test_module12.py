import unittest
import sys

class testClass13(unittest.TestCase):

    @unittest.skip("Demo unittest skipping")
    def testCase01(self):
        self.fail("FATAL")

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def testCase02(self):
        # Windows specific testing
        pass

    @unittest.skipUnless(sys.platform.startswith('linux'), 'requires linux')
    def testCase03(self):
        # linux specific testing
        pass



