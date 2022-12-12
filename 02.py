import input_data

data = input_data.get(2)

# ---------- Part 1 ----------
x = 0
depth = 0

for i in data:
    cmd, val = i.split(" ")
    val = int(val)
    if cmd == "forward":
        x += val
    elif cmd == "down":
        depth += val
    elif cmd == "up":
        depth -= val

print(f"Part 1: X: {x}; Depth: {depth}: Multiplied together: {x * depth}")


# ---------- Part 2 ----------
x = 0
depth = 0
aim = 0

for i in data:
    cmd, val = i.split(" ")
    val = int(val)
    if cmd == "forward":
        x += val
        depth += aim * val
    elif cmd == "down":
        aim += val
    elif cmd == "up":
        aim -= val

print(f"Part 2: X: {x}; Depth: {depth}: Multiplied together: {x * depth}")