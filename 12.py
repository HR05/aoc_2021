import input_data

def dict_add(d: dict, key, value):
    if key in d:
        d[key].append(value)
        return
    d[key] = [value]

def remove_cave(cons: dict, cave: str) -> dict:
    new_cons = {}
    for key in cons:
        if key == cave: continue
        new_cons[key] = []
        for x in cons[key]:
            if x == cave: continue
            new_cons[key].append(x)
    return new_cons

def get_paths1(cons_list: list[dict], index: int, cave: str) -> list[list]:
    
    if cave == "end":
        return [["end"]]
    
    new_index = index

    if cave.islower():
        cons_list.append(remove_cave(cons_list[index], cave))
        new_index = len(cons_list) - 1

    paths = []

    for x in cons_list[index][cave]:
        for p in get_paths1(cons_list, new_index, x):
            p.insert(0, cave)
            paths.append(p)


    return paths

def get_paths2(cons_list: list[dict], small_caves: list[dict], index: int, cave: str, twice: bool) -> list[list]:
    
    if cave == "end":
        return [["end"]]
    
    cons_list.append(dict(cons_list[index]))
    small_caves.append(dict(small_caves[index]))

    new_index = len(cons_list) - 1

    if cave.islower():
        if small_caves[index][cave] == 1 and twice:
            return []
        if cave == "start" or twice:
            cons_list[new_index] = remove_cave(cons_list[index], cave)
        else:
            if small_caves[new_index][cave] < 1:
                small_caves[new_index][cave] += 1
            else:
                cons_list[new_index] = remove_cave(cons_list[index], cave)
                twice = True

    paths = []

    for x in cons_list[index][cave]:
        for p in get_paths2(cons_list, small_caves, new_index, x, twice):
            p.insert(0, cave)
            paths.append(p)


    return paths


def part1(data):
    cons = {}
    cons_list = []
    for line in data:
        x, y = line.split("-")
        dict_add(cons, x, y)
        dict_add(cons, y, x)
    cons_list.append(cons)
    
    paths = get_paths1(cons_list, 0, "start")

    return len(paths)


def part2(data):
    cons = {}
    cons_list = []
    small_caves = [{}]
    for line in data:
        x, y = line.split("-")
        dict_add(cons, x, y)
        dict_add(cons, y, x)

        if x.islower() and x not in small_caves[0]:
            small_caves[0][x] = 0

        if y.islower() and y not in small_caves[0]:
            small_caves[0][y] = 0

    cons_list.append(cons)

    paths = get_paths2(cons_list, small_caves, 0, "start", False)

    return len(paths)



if __name__ == "__main__":
    data = input_data.get(12)
    
    print(f"Part 1: paths count: {part1(data)}")
    print(f"Part 2: paths count: {part2(data)}")