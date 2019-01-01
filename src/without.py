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
