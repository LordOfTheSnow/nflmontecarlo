class Division(object):
    """represents a division"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def debug(self):
        print(self.__dict__)
