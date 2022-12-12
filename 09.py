import input_data

def get_lowest_points(data):
    for i, line in enumerate(data):
        for j, x in enumerate(line):
            high = [False, False, False, False]
            
            if i == 0: high[0] = True
            elif data[i-1][j] > x: high[0] = True

            if j == len(line)-1: high[1] = True
            elif data[i][j+1] > x: high[1] = True

            if i == len(data)-1: high[2] = True
            elif data[i+1][j] > x: high[2] = True

            if j == 0: high[3] = True
            elif data[i][j-1] > x: high[3] = True

            if all(high): yield int(x)

def get_lowest_points_as_indexes(data):
    for i, line in enumerate(data):
        for j, x in enumerate(line):
            high = [False, False, False, False]
            
            if i == 0: high[0] = True
            elif data[i-1][j] > x: high[0] = True

            if j == len(line)-1: high[1] = True
            elif data[i][j+1] > x: high[1] = True

            if i == len(data)-1: high[2] = True
            elif data[i+1][j] > x: high[2] = True

            if j == 0: high[3] = True
            elif data[i][j-1] > x: high[3] = True

            if all(high): yield (i, j)

def get_basin_count(data, basin, x, y):
    offsets = [{'x':0, 'y':-1}, {'x':1, 'y':0}, {'x':0, 'y':1}, {'x':-1, 'y':0}]
    
    count = 0
    new_poses = []
    for offset in offsets:
        pos = (x + offset['x'], y + offset['y'])
        if pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0]): continue
        
        value = int(data[pos[0]][pos[1]])
       
        if value < 9 and pos not in basin:
            basin.append(pos)
            new_poses.append(pos)
    
    for pos in new_poses:
        count += get_basin_count(data, basin, pos[0], pos[1])

    return count + 1


def part1(data):
    lowest_points = list(get_lowest_points(data))
    risk_level = sum([x + 1 for x in lowest_points])
    
    return risk_level

def part2(data):
    lowest_points_indexes = list(get_lowest_points_as_indexes(data))
    
    basins = []
    for pos in lowest_points_indexes:
        basin = [pos]
        basins.append(get_basin_count(data, basin, pos[0], pos[1]))

    product = 1
    
    for i in range(3):
        x = max(basins)
        product *= x
        index = basins.index(x)
        basins.pop(index)

    return product


if __name__ == "__main__":
    data = input_data.get(9)

    print(f"Part 1: risk level: {part1(data)}")
    print(f"Part 2: product of three bigest basins: {part2(data)}")