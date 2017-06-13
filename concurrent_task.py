import os
import time
import threading
import multiprocessing

NUM_WOKERS=4

def only_sleep():
	'''Do nothing, wait for a timer to expire'''
	print 'PID:%s, Process Name: %s, Thread Name: %s'%(os.getpid(),
														multiprocessing.current_process().name,
														threading.current_thread().name)
	time.sleep(1)

def crunch_number():
	'''Do some computations'''
	print 'PID: %s, Process Name: %s, Thread Name: %s'%\
			(os.getpid(),
			 multiprocessing.current_process().name,
			 threading.current_thread().name)

	x=0
	while x< 10000000:
		x+=1

#Run tasks serially

start_time = time.time()
for _ in range(NUM_WOKERS):
	only_sleep()

end_time = time.time()

print 'Serial time=', end_time-start_time

#Run tasks using threads
start_time = time.time()
threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WOKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time=time.time()
print 'Thread times==', end_time-start_time


#Run tasks using processes

start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WOKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time=time.time()
print 'Parallel time=', end_time-start_time


#Run tasks serially
start_time=time.time()
for _ in range(NUM_WOKERS):
	crunch_number()

end_time=time.time()
print 'Serial time=', end_time-start_time

#Run task concurrent using thread
start_time=time.time()
threads = [threading.Thread(target=crunch_number) for _ in range(NUM_WOKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time=time.time()

print 'Threads time==',end_time-start_time

#Run tasks parallel using process
start_time=time.time()
processes = [multiprocessing.Process(target=crunch_number) for _ in range(NUM_WOKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time=time.time() 
print 'Process times==', end_time-start_time