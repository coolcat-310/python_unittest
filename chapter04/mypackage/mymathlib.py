class mymathlib:
    def __init__(self):
        """
        constructor for this class
        """
        print('creating object : ' + self.__class__.__name__)

    def add(self, x, y):
        return x+y

    def mul(self, x, y):
        return x*y

    def div(self, x, y):
        return x/y

    def sub(self, x, y):
        return x - y

    def __del__(self):
        """
        destructor of the class
        :return:
        """
        print('destroying object: ' + self.__class__.__name__)