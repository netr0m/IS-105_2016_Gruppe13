import timeit

class Search:
    def __init__(self):
        pass
    
    def search_fast(self):
        for item in self.prepare:
            if item == self.bazinga:
                return True
            return False
    
    def search_slow(self):
        return_value = False
        for item in self.prepare:
            if item == self.bazinga:
                return_value = True
        return return_value
    
    def run_search_fast(self, num):
        # Run a fast search
        benchmark = timeit.Timer(self.search_fast)
        time = benchmark.timeit(num)
        avg = float(time) / num                     # The average time to run through
        
        print ("Search_fast took ", time, " seconds to run through " + str(num) + " number of times")
        print ("The average time is " + str(avg))
        
        return avg
    
    def run_search_slow(self, num):
        # Run a slow search
        benchmark = timeit.Timer(self.search_slow)
        time = benchmark.timeit(num)
        avg = float(time) / num
        
        print ("Search_slow took ", time, " seconds to run through " + str(num) + " number of times")
        print ("The average time is " + str(avg))
        
        return avg
    
    def run_search(self, num):
        # Run both the search test methods
        self.run_search_fast(num)
        self.run_search_slow(num)