import time


class AlgorithmHelper(object):

    def get_solve_time(func):
        """
        Decorator that calculates the solve time.

        Keyword arguments:
        func -- We will get the execution time of this function.
        """
        def wrapper(*arg):
            start_time = time.clock()
            res = func(*arg)
            solved_time = time.clock() - start_time
            print("Solved in: %2.4f sec" % solved_time)
            #return solved_time
            return res
        return wrapper