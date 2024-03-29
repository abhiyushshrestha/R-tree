from rtree import RTree
from dataLoader import DataLoader
from sequentialSearch import SequentialSearch
import time

class QueryHandler():

    def __init__(self):
        self.loader = DataLoader()
        self.r_tree = RTree()
        self.seq_search = SequentialSearch()
        self.sequential_query_time = 0
        self.rtree_query_time = 0

    # Loading the given data points
    def datapoints_loader(self, datapoints_path):
        print("\n\nLoading data points...")
        start_time = time.time()
        points = self.loader.load_datapoints(datapoints_path)
        end_time = time.time()
        print("Data points loaded successfully!!!")
        return points

    # Loading all the queries
    def queries_loader(self, queries_path):
        print("\n\nLoading queries...")
        start_time = time.time()
        queries = self.loader.load_query(queries_path)
        end_time = time.time()
        print("Queries loaded successfully!!!")
        print("Time taken for loading queries: {} secs".format(end_time - start_time))
        return queries

    # Creating a R-tree index
    def create_rtree_index(self, points):
        print("\n\nCreating index for r-tree. Please wait for a while...")
        start_time = time.time()
        for index, point in points.iterrows():
            self.r_tree.insert(self.r_tree.root, point)
        end_time = time.time()
        print("Rtree index created successfully!!!")
        print("Time taken for building R-tree is : {} secs".format(end_time - start_time))

    # Sequential search
    def sequential_query(self, points, queries, single = False):
        print("\n\nSequential search:: Performing search. Please wait...")
        queries_result_sequential = []
        if single:
            # Sequential search for each query
            print("\n\nSequential search (only 1 query)::Performing search. Please wait...")
            start_time = time.time()
            q = {
                'x1': 17840,
                'x2': 18840,
                'y1': 13971,
                'y2': 14971
            }
            n = self.seq_search.sequential_search(points, q)
            end_time = time.time()
            queries_result_sequential.append(n)
            print("Sequential search::Query completed successfully!!!")
            print("Time taken for searching single query:", end_time - start_time)
            print("query result for sequential search (for 1 query) is : {} secs".format(queries_result_sequential))

        else:
            start_time = time.time()
            for index, query in queries.iterrows():
                n = self.seq_search.sequential_search(points, query)
                queries_result_sequential.append(n)
            end_time = time.time()
            self.sequential_query_time = end_time - start_time
            print("Sequential search::Query completed successfully!!!")
            print("Time taken for sequential query: ", self.sequential_query_time)
            print("Average time taken for sequential query: ", self.sequential_query_time / len(queries))
            print("Search result for Sequential search (all queries) is : {} secs".format(queries_result_sequential))

        return queries_result_sequential


    # Searching using R-trees
    def rtree_search(self, queries, single = False):
        print("\n\nR-tree:: Performing search. Please wait...")
        queries_result_rtree = []
        if single:
            # Searching using R-tree for each query
            print("\n\nR-tree (1 query) :: Performing search. Please wait...")
            start_time = time.time()
            q = {
                'x1': 17840,
                'x2': 18840,
                'y1': 13971,
                'y2': 14971
            }
            n = self.r_tree.query(self.r_tree.root, q)
            end_time = time.time()
            rtree_query_time = end_time - start_time
            queries_result_rtree.append(n)
            print("Rtree::Query completed successfully!!!")
            print("Total time taken for R-tree query:", rtree_query_time)
            print("query result for R-tree search (for 1 query) is : {} secs".format(queries_result_rtree))

        else:
            start_time = time.time()
            for index, query in queries.iterrows():
                n = self.r_tree.query(self.r_tree.root, query)
                queries_result_rtree.append(n)
            end_time = time.time()
            self.rtree_query_time = end_time - start_time
            print("Rtree::Query completed successfully!!!")
            print("Time taken for R-Tree query:", self.rtree_query_time)
            print("Average time taken for R-Tree query: ", self.rtree_query_time / len(queries))
            print("query result for R-tree search (for all query) is : {} secs".format(queries_result_rtree))

        return queries_result_rtree