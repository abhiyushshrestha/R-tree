import pandas as pd
from node import Node
from rtree import RTree
from dataLoader import DataLoader
from sequentialSearch import SequentialSearch
import time
import argparse
from queryHandler import QueryHandler
from output import Output


if __name__ == "__main__":

    handler = QueryHandler()
    o = Output()

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--points", type=str, required=True,
                    help="path to data points")
    ap.add_argument("-q", "--queries", type=str, required=True,
                    help="path to queries")
    args = vars(ap.parse_args())

    points = handler.datapoints_loader(args['points'])
    queries = handler.queries_loader(args['queries'])

    handler.create_rtree_index(points)
    queries_result_sequential = handler.sequential_search(queries, points)
    queries_result_rtree = handler.rtree_search(queries)

    o.save_as_txt(queries_result_sequential, "queries_result_sequential.txt")
    o.save_as_txt(queries_result_rtree, "queries_result_rtree.txt")









