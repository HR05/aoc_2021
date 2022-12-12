import input_data

def get_line_hor_or_ver(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    
    if x1 == x2:
        if y1 > y2: y1, y2 = y2, y1
        return [(x1, y) for y in range(y1, y2 + 1)]
    elif y1 == y2:
        if x1 > x2: x1, x2 = x2, x1
        return [(x, y1) for x in range(x1, x2 + 1)]
    return []

def get_line(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    if x1 == x2:
        if y1 > y2: y1, y2 = y2, y1
        return [(x1, y) for y in range(y1, y2 + 1)]
    elif y1 == y2:
        if x1 > x2: x1, x2 = x2, x1
        return [(x, y1) for x in range(x1, x2 + 1)]

    if x1 < x2 and y1 < y2:
        return [(x, y) for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1))]
    elif x1 > x2 and y1 > y2:
        return [(x, y) for x, y in zip(range(x2, x1 + 1), range(y2, y1 + 1))]
    elif x1 > x2 and y1 < y2:
        return [(x1 - x, y) for x, y in zip(range(x1 - x2 + 1), range(y1, y2 + 1))]
    elif x1 < x2 and y1 > y2:
        return [(x, y1 - y) for x, y in zip(range(x1, x2 + 1), range(y1 - y2 + 1))]
    

def part1(positions):
    area = {}
    for pos in positions:
        for point in get_line_hor_or_ver(pos[0], pos[1]):
            if str(point) in area:
                area[str(point)] += 1
            else:
                area[str(point)] = 1
    
    overlapping_points = 0
    for point in area:
        if area[point] >= 2:
            overlapping_points += 1

    return overlapping_points


def part2(positions):
    area = {}
    for pos in positions:
        for point in get_line(pos[0], pos[1]):
            if str(point) in area:
                area[str(point)] += 1
            else:
                area[str(point)] = 1
    
    overlapping_points = 0
    for point in area:
        if area[point] >= 2:
            overlapping_points += 1
    
    return overlapping_points


if __name__ == "__main__":
    data = input_data.get(5)
    positions = [[tuple(int(val) for val in pos.split(",")) for pos in line.split(" -> ")] for line in data]
    print(f"Part 1: overlapping points: {part1(positions)}")
    print(f"Part 2: overlapping points: {part2(positions)}")