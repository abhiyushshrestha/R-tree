
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
            'x_min': -1,
            'y_min': -1,
            'x_max': -1,
            'y_max': -1,
        }

    def calculate_perimeter(self):
        # only calculate the half calculate_perimeter here
        return (self.MBR['x_max'] - self.MBR['x_min']) + (self.MBR['y_max'] - self.MBR['y_min'])

    def check_underflow(self):
        if self.check_leaf():
            if self.data_points.__len__() < math.ceil(B / 2):
                return True
            else:
                return False
        else:
            if self.child_nodes.__len__() < math.ceil(B / 2):
                return True
            else:
                return False

    def check_overflow(self):
        if self.check_leaf():
            if self.data_points.__len__() > B:
                return True
            else:
                return False
        else:
            if self.child_nodes.__len__() > B:
                return True
            else:
                return False

    def check_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def check_leaf(self):
        if self.child_nodes.__len__() == 0:
            return True
        else:
            return False
