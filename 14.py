import input_data

def insert(polymer: dict[str: int], insertions: dict[str, str]):
    new_polymer = {key: 0 for key in polymer}

    for x in polymer:
        inserted = insertions[x]
        new_polymer[x[0] + inserted] += polymer[x]
        new_polymer[inserted + x[1]] += polymer[x]
    
    return new_polymer


def simulate(template, insertions, steps):
    polymer = {key: 0 for key in insertions}

    for i in range(len(template)-1):
        polymer[template[i:i+2]] += 1

    for _ in range(steps):
        polymer = insert(polymer, insertions)

    counts = {}

    for x in polymer:
        counts[x[0]] = 0
        if template[0] == x[0]: counts[x[0]] = 1

    for x in polymer:
        counts[x[1]] += polymer[x]

    most_common = 0
    least_common = 4 ** steps

    for x in counts:
        if counts[x] > most_common:
            most_common = counts[x]
        
        if counts[x] < least_common:
            least_common = counts[x]

    return most_common - least_common


if __name__ == "__main__":
    data = input_data.get(14)

    template = data[0]

    data.pop(0)
    data.pop(0)

    insertions = {}

    for line in data:
        insertions[line.split(" -> ")[0]] = line.split(" -> ")[1]


    print(f"Part 1: {simulate(template, insertions, 10)}")
    print(f"Part 2: {simulate(template, insertions, 40)}")