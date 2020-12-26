
import os
import sys


print ('hello')


#import ray
#ray.init(address='auto', _redis_password='5241590000000000')



import logging
import time
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

count = 0
for i in range(300):
    time.sleep(4)
    count +=1
    print("TIME SECS : ", count)





#print("hi")
#
# class tmp_folder(object):
#
#     def __init__(self):
#         self.folder_name = self.create_folder_name()
#
#     def create_folder_name(self):
#
#         #create time tmp
#         from datetime import datetime
#         dateTimeObj = datetime.now()
#         time_stamp_tag = str(dateTimeObj.hour)\
#                          + str(dateTimeObj.minute) \
#                          + str(dateTimeObj.second)
#         return "tmp_" + time_stamp_tag
#
#     def create(self):
#         os.system("mkdir" + " " + self.folder_name)
# #
#
#
# ray.init()
# print("HI")
#
#

#
    #logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')
    # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
  #  tmp = tmp_folder()
   # tmp.create()



''' --------------------- Instructions ---------------------------

This test shows the simplest way Ray can be ditributed between a cluster of two machines.
The code executed on the first machine, should also utilize the cpus on the connected machine.

1. Starts the head of the cluster on machine_1:
ray start --head

2. connect with machine 2
ray start --address=<'192.168.0.51:6379'> --redis-password=<'5241590000000000'>

3. Check the dashboard that they are connected.

4. Run code on machine_1 (head) with ray initialization as shown:
ray.init(address='192.168.0.51:6379', _redis_password='5241590000000000')

Notes: if ERROR 110 is indictative of a firewall error. Turn off firewall

python versions must be the same # --version python
ray versions must be the same # --version ray
e.g conda install python=<3.6.9>  #to match python
# ---------------------------------------------------------------
'''
#
# import os
# import ray
# import time
#
# # initialize ray to head which should already be running, as described in instructions
# # ray.init(address='192.168.0.51:6379', _redis_password='5241590000000000')
# #
# ray.init()
# def printer():
#     print("INSIDE WORKER " + str(time.time()) + "  PID  :    " + str(os.getpid()))
#
#
# # decorators allow for futures to be created for parallelization
# @ray.remote
# def func_1():
#     count = 0
#     for i in range(100000000):
#         count += 1
#     printer()
#     return count
#
#
# @ray.remote
# def func_2():
#     count = 0
#     for i in range(100000000):
#         count += 1
#     printer()
#     return count
#
#
# @ray.remote
# def func_3():
#     count = 0
#     for i in range(100000000):
#         count += 1
#     printer()
#     return count
#
#
# def main():
#     start = time.time()
#     results = []
#
#     # append fuction futures
#     for i in range(10):
#         results.append(func_1.remote())
#         results.append(func_2.remote())
#         results.append(func_3.remote())
#
#     # run in parrallel and get aggregated list
#     a = ray.get(results)
#     b = 0
#
#     # add all values in list together
#     for j in range(len(a)):
#         b += a[j]
#     print(b)
#
#     # time to complete
#     end = time.time()
#     print(end - start)
#
#
# if __name__ == '__main__':
#     main()

# import time
# import ray
#
# def main():
#     print("INN")
#     ray.init()
#     print("INN2")
#     count = 0
#     for i in range(300):
#         time.sleep(1)
#         count +=1
#         print("TIME SECS : ", count)
#
# if __name__ == '__main__':
#     main()
