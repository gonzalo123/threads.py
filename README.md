## Playing with threads and Python

Today I want to play a little bit with Python and threads. This kind of post are one kind of cheat sheet that I like to publish, basically to remember how do do things. 

I don't like to use threads. They are very powerful but, as uncle Ben said: Great power comes great responsibility. I prefer decouple process with queues instead using threads, but sometimes I need to use them. Let's start

First I will build a simple script without threads. This script will append three numbers (1, 2 and 3) to a list and it will sum them. The function that append numbers to the list sleeps a number of seconds equals to the number that we're appending.

```python
import time

start_time = time.time()

total = []


def sleeper(seconds):
    time.sleep(seconds)
    total.append(seconds)


for s in (1, 2, 3):
    sleeper(s)

end_time = time.time()

total_time = end_time - start_time

print("Total time: {:.3} seconds. Sum: {}".format(total_time, sum(total)))

```

The the outcome of the script is obviously 6 (1 + 2 + 3) and as we're sleeping the script a number of seconds equals to the the number that we're appending our script, it takes 6 seconds to finish.

Now we're going to use a threading version of the script. We're going to do the same, but we're going to use one thread for each append (with the same sleep function)

```python
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
```

The outcome of our script is 6 again, but now it takes 3 seconds (the highest sleep).
