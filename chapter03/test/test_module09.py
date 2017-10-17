
import unittest

from mypackage.mymathlib import *

math_object = 0

def setUpModule():
    """
    Called once, before anything else in the module
    :return:
    """
    print('In setUpModule()...')
    global math_object
    math_object = mymathlib()

def tearDownModule():
    """
    Called once, after everything else in the module
    :return:
    """
    print('In tearDownModule()')
    global math_object
    del math_object

class testClass10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Called only once, before any test in the class
        :return:
        """
        print("IN setUpClass()...")

    def setUp(self):
        """
        Called once before every test method
        :return:
        """
        print('In setup()...')

    def testCase01(self):
        print('In testCase01()...')
        self.assertEqual(math_object.add(2,5), 7)

    def testCase02(self):
        print('In testCase02()...')

    def tearDown(self):
        """
        Called once after every test method
        :return:
        """
        print('In tearDown()...')

    @classmethod
    def tearDownClass(cls):
        """
        called only once, after all test in the class
        :return:
        """
        print('In tearDownClass()...')