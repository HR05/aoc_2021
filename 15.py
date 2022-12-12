import input_data

def get_next_coor(data, coord):
    offsets  = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for offset in offsets:
        x = coord[0][0] + offset[0]
        y = coord[0][1] + offset[1]

        if not 0 <= x < len(data[0]): continue
        if not 0 <= y < len(data): continue

        yield ((x, y), coord[1] + data[y][x])

def prove_num(x):
    if x < 10:
        return x

    return x % 9

        
def part1(data):
    start = (0, 0)
    end = (len(data[0])-1, len(data)-1)

    lowest_risk_level = None

    coords = [(start, 0)]

    visited_coords = {}

    while len(coords) != 0:
        next_coords = []
        for coord in coords:
            if coord[0] == end:
                if lowest_risk_level == None or coord[1] < lowest_risk_level:
                    lowest_risk_level = coord[1]
            elif coord[0] not in visited_coords or coord[1] < visited_coords[coord[0]]:
                visited_coords[coord[0]] = coord[1]
                next_coords += list(get_next_coor(data, coord))
                    
        coords = next_coords
        print(lowest_risk_level)


    return lowest_risk_level

def part2(data):
    new_data = []

    for i in range(5):
        for j in range(5):
            for k in range(len(data)):
                if j == 0:
                    new_data.append([prove_num(x + i) for x in data[k]])
                else:
                    new_data[k + i * len(data)] += [prove_num(x + i + j) for x in data[k]]

    return part1(new_data)


if __name__ == "__main__":
    data = input_data.get(15)
    data = [[int(x) for x in line] for line in data]

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")