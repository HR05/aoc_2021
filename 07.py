import input_data

def part1(data):
    fuel_sum = -1
    for i in range(min(data), max(data)):
        tmp = 0
        for x in data:
            tmp += abs(i - x)
        
        if fuel_sum == -1 or tmp < fuel_sum: fuel_sum = tmp
            
    return fuel_sum


def part2(data):
    fuel_sum = -1
    for i in range(min(data), max(data)):
        tmp = 0
        for x in data:
            tmp += sum(range(abs(i - x) + 1))
        if fuel_sum == -1 or tmp < fuel_sum: fuel_sum = tmp

    return fuel_sum


if __name__ == "__main__":
    data = input_data.get(7)
    data = [int(x) for x in data[0].split(",")]
    print(f"Part 1: total fuel: {part1(data)}")
    print(f"Part 2: total fuel: {part2(data)}")