''' This module defines all operations, classes and functions needed for performance measurements'''
import time
import psutil

class perf_spy():
    ''' This class drives all measurements '''
    initial_time = time.time()
    def __init__(self, track_time = True, track_memory = False, track_cpu = False):
        #self.initial_time = time.time()
        self.config = {
            "track_time" : track_time,
            "track_memory" : track_memory,
            "track_cpu" : track_cpu
            }
    # def tic(self):
    #     self.initial_time = time.time()
    #     return self.initial_time 
    # def toc(self):
    #     self.final_time = time.time()
    #     print("Elapsed time : " + str(self.final_time  - self.initial_time) + " ms")

def tic():
    global initial_time
    initial_time = time.time()
    return initial_time 
def toc():
    global initial_time
    global final_time 
    final_time = time.time()
    print("Elapsed time : " + str(final_time  - initial_time) + " ms")
