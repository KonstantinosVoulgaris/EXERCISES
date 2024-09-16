import random
import statistics
a=[random.randint(1 , 10000) for _ in range(1000)] 
print(a)
minimum = min(a)
median = statistics.median(a)
maximum = max(a)
print ("the_minimum_is:", minimum)
print ("the_median_is:", median)
print ("the_maximum_is:", maximum)
