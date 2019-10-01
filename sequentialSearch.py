class SequentialSearch():

    def __init__(self):
        pass

    def sequential_search(self, points, query):
        result = 0
        for index, point in points.iterrows():
            if query['x_min'] <= point['x'] <= query['x_max'] and query['y_min'] <= point['y'] <= query['y_max']:
                result = result + 1
        return result