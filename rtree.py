from node import  Node
import sys
import math

B = 4
class RTree(object):
    def __init__(self):
        self.root = Node()

    def query(self, node, query):
        num = 0
        if node.check_leaf():
            for point in node.data_points:
                if self.is_covered(point, query):
                    num = num + 1
            return num
        else:
            for child in node.child_nodes:
                if self.is_intersect(child, query):
                    num = num + self.query(child, query)
            return num

    def is_intersect(self, node, query):
        # if two mbrs are intersected, then:
        # |center1_x - center2_x| <= length1 / 2 + length2 / 2 and:
        # |center1_y - center2_y| <= width1 / 2 + width2 / 2
        center1_x = (node.MBR['x_max'] + node.MBR['x_min']) / 2
        center1_y = (node.MBR['y_max'] + node.MBR['y_min']) / 2
        length1 = node.MBR['x_max'] - node.MBR['x_min']
        width1 = node.MBR['y_max'] - node.MBR['y_min']
        center2_x = (query['x_max'] + query['x_min']) / 2
        center2_y = (query['y_max'] + query['y_min']) / 2
        length2 = query['x_max'] - query['x_min']
        width2 = query['y_max'] - query['y_min']
        if abs(center1_x - center2_x) <= length1 / 2 + length2 / 2 and\
                abs(center1_y - center2_y) <= width1 / 2 + width2 / 2:
            return True
        else:
            return False

    def is_covered(self, point, query):
        x_min, x_max, y_min, y_max = query['x_min'], query['x_max'], query['y_min'], query['y_max']
        if x_min <= point['x'] <= x_max and y_min <= point['y'] <= y_max:
            return True
        else:
            return False

    def insert(self, u, p):
        if u.check_leaf():
            self.add_data_point(u, p)
            if u.check_overflow():
                self.handle_overflow(u)
        else:
            v = self.choose_subtree(u, p)
            self.insert(v, p)
            self.update_mbr(v)


    # return the child whose MBR requires the minimum increase in calculate_perimeter to cover p
    def choose_subtree(self, u, p):
        if u.check_leaf():
            return u
        else:
            min_increase = sys.maxsize
            best_child = None
            for child in u.child_nodes:
                if min_increase > self.calc_perimeter_increase(child, p):
                    min_increase = self.calc_perimeter_increase(child, p)
                    best_child = child
            # return self.choose_subtree(best_child, p)
            return best_child

    def calc_perimeter_increase(self, node, p):
        # new calculate_perimeter - original calculate_perimeter = increase of calculate_perimeter
        origin_mbr = node.MBR
        x_min, x_max, y_min, y_max = origin_mbr['x_min'], origin_mbr['x_max'], origin_mbr['y_min'], origin_mbr['y_max']
        increase = (max([x_min, x_max, p['x']]) - min([x_min, x_max, p['x']]) +
                    max([y_min, y_max, p['y']]) - min([y_min, y_max, p['y']])) - node.calculate_perimeter()
        return increase

    def handle_overflow(self, u):
        u1, u2 = self.split(u)
        # if u is root, create a new root with s1 and s2 as its' children
        if u.check_root():
            new_root = Node()
            self.add_child(new_root, u1)
            self.add_child(new_root, u2)
            self.root = new_root
            self.update_mbr(new_root)
        # if u is not root, delete u, and set s1 and s2 as u's parent's new children
        else:
            w = u.parent
            # copy the information of s1 into u
            w.child_nodes.remove(u)
            self.add_child(w, u1)
            self.add_child(w, u2)
            if w.check_overflow():
                self.handle_overflow(w)
            self.update_mbr(w)

    def split(self, u):
        # split u into s1 and s2
        best_s1 = Node()
        best_s2 = Node()
        best_perimeter = sys.maxsize
        # u is a leaf node
        if u.check_leaf():
            m = u.data_points.__len__()
            # create two different kinds of divides
            divides = [sorted(u.data_points, key=lambda data_point: data_point['x']),
                       sorted(u.data_points, key=lambda data_point: data_point['y'])]
            for divide in divides:
                for i in range(math.ceil(0.4 * B), m - math.ceil(0.4 * B) + 1):
                    s1 = Node()
                    s1.data_points = divide[0: i]
                    self.update_mbr(s1)
                    s2 = Node()
                    s2.data_points = divide[i: divide.__len__()]
                    self.update_mbr(s2)
                    if best_perimeter > s1.calculate_perimeter() + s2.calculate_perimeter():
                        best_perimeter = s1.calculate_perimeter() + s2.calculate_perimeter()
                        best_s1 = s1
                        best_s2 = s2

        # u is a internal node
        else:
            # create four different kinds of divides
            m = u.child_nodes.__len__()
            divides = [sorted(u.child_nodes, key=lambda child_node: child_node.MBR['x_min']),
                       sorted(u.child_nodes, key=lambda child_node: child_node.MBR['x_max']),
                       sorted(u.child_nodes, key=lambda child_node: child_node.MBR['y_min']),
                       sorted(u.child_nodes, key=lambda child_node: child_node.MBR['y_max'])]
            for divide in divides:
                for i in range(math.ceil(0.4 * B), m - math.ceil(0.4 * B) + 1):
                    s1 = Node()
                    s1.child_nodes = divide[0: i]
                    self.update_mbr(s1)
                    s2 = Node()
                    s2.child_nodes = divide[i: divide.__len__()]
                    self.update_mbr(s2)
                    if best_perimeter > s1.calculate_perimeter() + s2.calculate_perimeter():
                        best_perimeter = s1.calculate_perimeter() + s2.calculate_perimeter()
                        best_s1 = s1
                        best_s2 = s2

        for child in best_s1.child_nodes:
            child.parent = best_s1
        for child in best_s2.child_nodes:
            child.parent = best_s2

        return best_s1, best_s2

    def add_child(self, node, child):
        node.child_nodes.append(child)
        child.parent = node
        # self.update_mbr(node)
        if child.MBR['x_min'] < node.MBR['x_min']:
            node.MBR['x_min'] = child.MBR['x_min']
        if child.MBR['x_max'] > node.MBR['x_max']:
            node.MBR['x_max'] = child.MBR['x_max']
        if child.MBR['y_min'] < node.MBR['y_min']:
            node.MBR['y_min'] = child.MBR['y_min']
        if child.MBR['y_max'] > node.MBR['y_max']:
            node.MBR['y_max'] = child.MBR['y_max']

    def add_data_point(self, node, data_point):
        node.data_points.append(data_point)
        # self.update_mbr(node)
        if data_point['x'] < node.MBR['x_min']:
            node.MBR['x_min'] = data_point['x']
        if data_point['x'] > node.MBR['x_max']:
            node.MBR['x_max'] = data_point['x']
        if data_point['y'] < node.MBR['y_min']:
            node.MBR['y_min'] = data_point['y']
        if data_point['y'] > node.MBR['y_max']:
            node.MBR['y_max'] = data_point['y']

    def update_mbr(self, node):
        # print("update_mbr")
        x_list = []
        y_list = []
        if node.check_leaf():
            x_list = [point['x'] for point in node.data_points]
            y_list = [point['y'] for point in node.data_points]
        else:
            x_list = [child.MBR['x_min'] for child in node.child_nodes] + [child.MBR['x_max'] for child in node.child_nodes]
            y_list = [child.MBR['y_min'] for child in node.child_nodes] + [child.MBR['y_max'] for child in node.child_nodes]
        new_mbr = {
            'x_min': min(x_list),
            'x_max': max(x_list),
            'y_min': min(y_list),
            'y_max': max(y_list)
        }
        node.MBR = new_mbr
