
B = 4

class Node(object):
    def __init__(self):
        self.id = 0
        # for internal nodes
        self.child_nodes = []
        # for leaf nodes
        self.data_points = []
        self.parent = None
        self.MBR = {
            'x1': -1,
            'y1': -1,
            'x2': -1,
            'y2': -1,
        }

    def perimeter(self):
        # only calculate the half perimeter here
        return (self.MBR['x2'] - self.MBR['x1']) + (self.MBR['y2'] - self.MBR['y1'])

    def is_underflow(self):
        if self.is_leaf():
            if self.data_points.__len__() < math.ceil(B / 2):
                return True
            else:
                return False
        else:
            if self.child_nodes.__len__() < math.ceil(B / 2):
                return True
            else:
                return False

    def is_overflow(self):
        if self.is_leaf():
            if self.data_points.__len__() > B:
                return True
            else:
                return False
        else:
            if self.child_nodes.__len__() > B:
                return True
            else:
                return False

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def is_leaf(self):
        if self.child_nodes.__len__() == 0:
            return True
        else:
            return False
