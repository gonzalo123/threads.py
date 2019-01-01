import time
from queue import Queue
import threading

start_time = time.time()

queue = Queue()


def sleeper(seconds):
    time.sleep(seconds)
    queue.put(seconds)


threads = []
for s in (1, 2, 3):
    t = threading.Thread(target=sleeper, args=(s,))
    threads.append(t)
    t.start()

for one_thread in threads:
    one_thread.join()

total = 0
while not queue.empty():
    total = total + queue.get()

end_time = time.time()

total_time = end_time - start_time
print("Total time: {:.3} seconds. Sum: {}".format(total_time, total))
