import pandas as pd
from nodeManager import NodeManager
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
        :return: a dataframe of the queries coordinates with four columns : x_min, x_max, y_min, y_max
        """

        query_points = open(queries_path, "r")
        query_coordinates = query_points.readlines()
        x_min = []
        x_max = []
        y_min = []
        y_max = []
        for i in range(len(query_coordinates)):
            # for i in range(100):
            x_min.append(int(query_coordinates[i].split()[0]))
            x_max.append(int(query_coordinates[i].split()[1]))
            y_min.append(int(query_coordinates[i].split()[2]))
            y_max.append(int(query_coordinates[i].split()[3]))

        queries = pd.DataFrame({'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max, })
        return queries