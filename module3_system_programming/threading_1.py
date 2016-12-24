import threading
import time

def fun(i):
	print "Greeting %s Yeah ! I am %s" % (i,threading.currentThread().getName())
	print "Sleeping for %i seconds" % i
	time.sleep(i)
	return

threads = []

for i in range(5):
	t = threading.Thread(name='Yo Thread',target=fun,args=(i,))
	t.setDaemon(True)
	threads.append(t)
	t.start()


