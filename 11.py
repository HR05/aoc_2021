import input_data

def increase_by_1(data):
    for line in data:
        for i, _ in enumerate(line):
            line[i] += 1

def flash(data, flashed, x, y):
    flashes = 0
    flashed.append((x, y))
    
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y: continue
            if i < 0 or i > len(data)-1 or j < 0 or j > len(data[0])-1: continue

            data[i][j] += 1
            
            if data[i][j] > 9 and (i, j) not in flashed:
                flashes += flash(data, flashed, i, j)


    return flashes + 1

def check_flashes(data):
    flashes = 0
    flashed = []
    for i, line in enumerate(data):
        for j, x in enumerate(line):
            if x > 9 and (i, j) not in flashed:
                flashed.append((i, j))
                flashes += flash(data, flashed, i, j)

    return flashes

def check_if_flasched(data):
    for line in data:
        for i, x in enumerate(line):
            if x > 9:
                line[i] = 0



def part1(data, steps):
    sim_data = [[int(x) for x in line] for line in data]
    flashes = 0
    for _ in range(steps):
        increase_by_1(sim_data)
        flashes += check_flashes(sim_data)
        check_if_flasched(sim_data)

    return flashes

def part2(data):
    max_flashes = len(data) * len(data[0])
    flashes = 0

    iteration = 0

    sim_data = [[int(x) for x in line] for line in data]
    while flashes != max_flashes:
        iteration += 1
        increase_by_1(sim_data)
        flashes = check_flashes(sim_data)
        check_if_flasched(sim_data)

    return iteration



if __name__ == "__main__":
    data = input_data.get(11)
    
    print(f"Part 1: total flashes: {part1(data, 100)}")
    print(f"Part 2: flash at the same time: {part2(data)}")