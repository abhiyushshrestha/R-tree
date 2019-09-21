import pandas as pd
from node import Node
from rtree import RTree

class DataLoader():

    def __init__(self):
        pass
        self.rt = RTree()

    def load_datapoints(self, points_path):

        """
        This function loads the the data points from text file and convert into suitable dataframe format
        :return: a dataframe of the points with two columns: x and y
        """

        points = open(points_path, "r")
        lines = points.readlines()
        lines = lines[1:]
        x = []
        y = []
        for i in range(len(lines)):
        # for i in range(100):
            x.append(int(lines[i].split()[1]))
            y.append(int(lines[i].split()[2]))

        points = pd.DataFrame({'x': x, 'y': y})
        return points

    def load_query(self, queries_path):

        """
        This function loads the given text file queries and convert them into suitable dataframe format
        :return: a dataframe of the queries coordinates with four columns : x1, x2, y1, y2
        """

        query_points = open(queries_path, "r")
        query_coordinates = query_points.readlines()
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        for i in range(len(query_coordinates)):
            # for i in range(100):
            x1.append(int(query_coordinates[i].split()[0]))
            x2.append(int(query_coordinates[i].split()[1]))
            y1.append(int(query_coordinates[i].split()[2]))
            y2.append(int(query_coordinates[i].split()[3]))

        queries = pd.DataFrame({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, })
        return queries