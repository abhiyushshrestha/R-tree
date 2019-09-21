class SequentialSearch():

    def __init__(self):
        pass

    def sequential_query(points, query):
        result = 0
        for index, point in points.iterrows():
            print(index)
            if query['x1'] <= point['x'] <= query['x2'] and query['y1'] <= point['y'] <= query['y2']:
                result = result + 1
        return result