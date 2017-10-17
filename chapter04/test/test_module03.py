from mypackage.mymathlib import *

math_obj = 0

def setUpModule():
    """
    called once, before anything else in this module
    :return:
    """
    print("In setUpModule()...")
    global math_obj
    math_obj = mymathlib()

def tearDownModule():
    """
    called once, after everything else in this module
    :return:
    """
    print('In tearDownModule()...')
    global math_obj
    del math_obj

class TestClass02:

    @classmethod
    def setUpClass(cls):
        """
        called once, before any test in the class
        :return:
        """
        print("In setpClass()...")

    def setUp(self):
        """
        called before every test method
        :return:
        """
        print("\nIn setUp()...")

    def test_case01(self):
        print("In test_case01()...")
        assert math_obj.add(2,5) == 7

    def test_case02(self):
        print("In test_case02()...")

    def tearDown(self):
        """
        called once, after all tests, if setUpClass() successful
        :return:
        """
        print('\nIn tearDownClass()...')