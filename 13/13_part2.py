lines = [x.strip("\n") for x in open("input.txt").readlines()]
intervals = [x for x in lines[1].split(",")]

r = []
m = []
for i, bus_id in enumerate(intervals):
    try:
        bus_id = int(bus_id)
        m.append(str(bus_id))
        r.append(str(bus_id - i))
    except ValueError:
        pass

r[0] = "0"
# put this into wolfram alpha
print("ChineseRemainder[{", ",".join(r), "}, {", ",".join(m), "}]")
