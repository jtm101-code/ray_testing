import os
import ray
import time
#import sklearn
#import tensorflow
import sklearn
from xgboost.sklearn import XGBClassifier

#initialize ray to head which should already be running, as described in instructions
#ray.init(address='auto', _redis_password='5241590000000000')
ray.init()
def printer():
    print("INSIDE WORKER " + str(time.time()) +"  PID  :    "+  str(os.getpid()))


# decorators allow for futures to be created for parallelization
@ray.remote        
def func_1():
    model = XGBClassifier()
    count = 0
    for i in range(100000000):
        count += 1
    printer()
    return count
        
        
@ray.remote        
def func_2():
    #model = XGBClassifier()
    count = 0
    for i in range(100000000):
        count += 1
    printer()
    return count

    
@ray.remote
def func_3():
    count = 0
    for i in range(100000000):
        count += 1
    printer()
    return count

def main():
    model = XGBClassifier()

    start = time.time()
    results = []
    
    #append fuction futures
    for i in range(10):
        results.append(func_1.remote())
        results.append(func_2.remote())
        results.append(func_3.remote())
        
    #run in parrallel and get aggregated list
    a = ray.get(results)
    b = 0
    
    #add all values in list together
    for j in range(len(a)):
        b += a[j]
    print(b)
    
    #time to complete
    end = time.time()
    print(end - start)
    
    
if __name__ == '__main__':
    main()

