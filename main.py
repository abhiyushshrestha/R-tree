import pandas as pd
from node import Node
from rtree import RTree
from dataLoader import DataLoader
from sequentialSearch import SequentialSearch
import time
import argparse


if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--points", type=str, required=True,
                    help="path to data points")
    ap.add_argument("-q", "--queries", type=str, required=True,
                    help="path to queries")
    args = vars(ap.parse_args())
    loader = DataLoader()
    r_tree = RTree()
    sequential_search = SequentialSearch()

    # Loading the given data points
    print("\n\nLoading data points...")
    start_time = time.time()
    points = loader.load_datapoints(args['points'])
    end_time = time.time()
    print("Data points loaded successfully!!!")


    # Loading all the queries
    print("\n\nLoading queries...")
    start_time = time.time()
    queries = loader.load_query(args['queries'])
    end_time = time.time()
    print("Queries loaded successfully!!!")
    print("Time taken for loading queries:", end_time - start_time)

    # Creating a R-tree index
    print("\n\nCreating index for r-tree...")
    start_time = time.time()
    for index, point in points.iterrows():
        r_tree.insert(r_tree.root, point)
    end_time = time.time()
    print("Rtree index created successfully!!!")
    print("Time taken for loading data points:", end_time - start_time)


    # Sequential search
    print("\n\nSequential search::Querying all queries...")
    queries_result = []
    start_time = time.time()
    for index, query in queries.iterrows():
        n = sequential_search.sequential_query(points, query)
        queries_result.append(n)
    end_time = time.time()
    print("Sequential search::Query completed successfully!!!")
    print("Time taken for query using sequential search:", end_time - start_time)
    print("Search result for Sequential search (all queries)::", queries_result)



    # Sequential search for each query
    print("\n\nSequential search::Querying 1 query...")
    start_time = time.time()
    q = {
        'x1': 17840,
        'x2': 18840,
        'y1': 13971,
        'y2': 14971
    }
    n = sequential_search.sequential_query(points, q)
    end_time = time.time()
    print("Sequential search::Query completed successfully!!!")
    print("Time taken for searching single query:", end_time - start_time)
    print("query result for sequential search (for 1 query)::", n)


    # Searching using R-tree
    print("\n\nQuerying all queries using r_tree indexing...")
    queries_result = []
    start_time = time.time()
    for index, query in queries.iterrows():
        n = r_tree.query(r_tree.root, query)
        queries_result.append(n)
    end_time = time.time()
    print("Rtree::Query completed successfully!!!")
    print("Time taken for loading data points:", end_time - start_time)
    print("query result for R-tree search (for all query)::", queries_result)

    # Searching using R-tree for each query
    print("\n\nQuerying 1 query using r_tree indexing...")
    start_time = time.time()
    n = r_tree.query(r_tree.root, q)
    end_time = time.time()
    print("Rtree::Query completed successfully!!!")
    print("Time taken for loading data points:", end_time - start_time)
    print("query result for R-tree search (for 1 query)::", n)

    # print("\nquery result for 10 different queries:", queries_result)
    # print("\ndata points::", r_tree.root.data_points)
    # print("\nchild nodes::", r_tree.root.child_nodes)
    # print("\nMBR::", r_tree.root.MBR)
    # print("\nparent::", r_tree.root.parent)



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



