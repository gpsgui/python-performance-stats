''' This module defines all operations, classes and functions needed for performance measurements'''
import time
import psutil

class performance_stats():
    ''' This class drives all measurements '''
    def __init__(self, track_time = True, track_memory = False, track_cpu = False):
        self.config = {
            "track_time" : track_time,
            "track_memory" : track_memory,
            "track_cpu" : track_cpu
            }
    def tic(self):
        self.initial_time = time.time()
        return self.initial_time 
    def toc(self):
        self.final_time = time.time()
        print("Elapsed time : " + str(self.final_time  - self.initial_time) + " ms")

initial_time = time.time()
final_time = 0

def tic():
    initial_time = time.time()
    return initial_time

def toc():
    final_time = time.time()
    print("Elapsed time : " + str(final_time  - initial_time) + " s")
    return final_time
