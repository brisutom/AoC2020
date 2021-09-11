lines = [x.strip("\n") for x in open("input.txt").readlines()]
earliest = int(lines[0])
intervals = [int(x) for x in lines[1].replace("x,", "").split(",")]
departures = [(earliest // x + 1) * x for x in intervals]
wait_times = [x - earliest for x in departures]
min_wait = min(wait_times)
bus_id = intervals[wait_times.index(min_wait)]
print(bus_id * min_wait)
