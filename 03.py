import input_data

data = input_data.get(3)


# ---------- Part 1 ----------
bits = [[0, 0] for i in range(len(data[0]))]

for line in data:
    for i, bit in enumerate(line):
        bits[i][int(bit)] += 1

gamma = ""
epsilon = ""

for bit in bits:
    if bit[0] > bit[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(f"Part 1: gamma: 0b{gamma}, {int(gamma, base=2)}; epsilon: 0b{epsilon}, {int(epsilon, base=2)}; product: {int(gamma, base=2) * int(epsilon, base=2)}")


# ---------- Part 2 ----------
oxygen = data
co2 = data

def filter_list(numbers, i, common):
    if len(numbers) == 1:
        return numbers
        
    bit = [0, 0]
    filter = 1
    for line in numbers:
        bit[int(line[i])] += 1
    
    if common and bit[0] > bit[1]:
        filter = 0
    if not common and bit[0] <= bit[1]:
        filter = 0
    
    filtered_numbers = []
    for line in numbers:
        if int(line[i]) == filter:
            filtered_numbers += [line]

    return filtered_numbers

    

for i in range(len(data[0])):
    oxygen = filter_list(oxygen, i, True)
    co2 = filter_list(co2, i, False)

oxygen = oxygen[0]
co2 = co2[0]
    

print(f"Part 2: oxygen: 0b{oxygen}, {int(oxygen, base=2)}; co2: 0b{co2}, {int(co2, base=2)}; product: {int(oxygen, base=2) * int(co2, base=2)}")