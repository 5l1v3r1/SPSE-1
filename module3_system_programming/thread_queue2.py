import threading
import Queue
import time

class WorkerThread(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue = queue
	def run(self):
		print "In WorkerThread"
		while True:
			counter = self.queue.get()
			print "Ordered to sleep for %d seconds!" % counter
			time.sleep(counter)
			print "Finished Sleeping for %d seconds" % counter
			self.queue.task_done()
			

queue = Queue.Queue()

for i in range(5):
	print "Creating WorkerThread :%d" %i
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "WorkerThread %d Created" %i

for j in range(0,5,2):
	queue.put(j)
	queue.put(j+1)

queue.join()

print "All tasks over"
