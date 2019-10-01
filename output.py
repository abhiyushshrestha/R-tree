class Output():

    @staticmethod
    def save_as_txt(results, filename = "output/query_result.txt"):
        with open(filename, "w") as f:
            for result in results:
                f.write(str(result) + "\n")