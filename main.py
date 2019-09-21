import pandas as pd
from node import Node
from rtree import RTree
from dataLoader import DataLoader
import time


if __name__ == "__main__":
    r_tree = RTree()
    loader = DataLoader()
    # point = {
    #     'x': 34,
    #     'y': 35
    # }
    #
    # rt.insert(rt.root, point)
    # print("data points::", rt.root.data_points)
    # print("child nodes::", rt.root.child_nodes)
    # print("MBR::", rt.root.MBR)
    # print("parent::", rt.root.parent)


    print("\nLoading datapoints...")
    start_time = time.time()
    points = loader.load_datapoints()
    end_time = time.time()
    print("\nData points loaded successfully!!!")
    print("\nTime taken for loading data points:", end_time - start_time)


    print("\nCreating index for r-tree...")
    start_time = time.time()
    for index, point in points.iterrows():
        r_tree.insert(r_tree.root, point)
    end_time = time.time()
    print("\nRtree index created successfully!!!")
    print("\nTime taken for loading data points:", end_time - start_time)


    queries_result = []
    print("\nLoading queries...")
    start_time = time.time()
    queries = loader.load_query()
    end_time = time.time()
    print("\nQueries loaded successfully!!!")
    print("\nTime taken for loading data points:", end_time - start_time)

    print("\nQuerying each queries...")
    start_time = time.time()
    for index, query in queries.iterrows():
        n = r_tree.query(r_tree.root, query)
        queries_result.append(n)
    end_time = time.time()
    print("\nQuery completed successfully!!!")
    print("\nTime taken for loading data points:", end_time - start_time)

    print("\nquery result for 10 different queries:", queries_result)
    print("\ndata points::", r_tree.root.data_points)
    print("\nchild nodes::", r_tree.root.child_nodes)
    print("\nMBR::", r_tree.root.MBR)
    print("\nparent::", r_tree.root.parent)



q = {
    'x1': 17840,
    'x2': 18840,
    'y1': 13971,
    'y2': 14971
}

q = {
    'x1': 33451,
    'x2': 34451,
    'y1': 29693,
    'y2': 30693
}
q = {
    'x1': 7187,
    'x2': 8187,
    'y1': 56997,
    'y2': 57997
}



