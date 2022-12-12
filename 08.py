import input_data

def sort_str(string):
    new_string = ""
    for i in range(97, 122):
        for j in range(len(string)):
            if chr(i) == string[j]:
                new_string += string[j]
    return new_string

def get_same_chars(str1, str2):
    same_chars = 0
    for x in str1:
        for y in str2:
            if x == y:
                same_chars += 1
    return same_chars

def get_patterns_by_len(line):
    patterns = {i: [] for i in range(2, 8)}
    for l in line:
        for x in l:
            sorted_str = sort_str(x)
            if sorted_str not in patterns[len(x)]:
                patterns[len(x)].append(sorted_str)
    return patterns

def get_ouput_of_line(line):
    patterns_by_len = get_patterns_by_len(line)
    patterns = {}

    for x in range(10):
        patterns[x] = ""

    unique_patterns = {2: "", 3: "", 4: "", 7: ""}

    for l in line:
        for x in l:
            for key in unique_patterns:
                if key == len(x):
                    unique_patterns[key] = sort_str(x)

    patterns[1] = unique_patterns[2]
    patterns[4] = unique_patterns[4]
    patterns[7] = unique_patterns[3]
    patterns[8] = unique_patterns[7]
    for x in patterns_by_len[6]:
        if get_same_chars(patterns[1], x) == 1:
            patterns[6] = x
            patterns_by_len[6].remove(x)
    for x in patterns_by_len[5]:
        if get_same_chars(patterns[6], x) == 5:
            patterns[5] = x
            patterns_by_len[5].remove(x)
    for x in patterns_by_len[6]:
        if get_same_chars(patterns[5], x) == 5:
            patterns[9] = x
            patterns_by_len[6].remove(x)
    patterns[0] = patterns_by_len[6][0]
    for x in patterns_by_len[5]:
        if get_same_chars(patterns[1], x) == 1:
            patterns[2] = x
            patterns_by_len[5].remove(x)
    patterns[3] = patterns_by_len[5][0]

    return {patterns[i]: i for i in patterns}


def part1(data):
    output = [x.split(" | ")[1].split() for x in data]
    count = 0
    for l in output:
        for x in l:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                count += 1
    
    return count

def part2(data):
    data = [[x.split() for x in line.split(" | ")] for line in data]

    sum_of_output = 0

    for line in data:
        patterns = get_ouput_of_line(line)
        output = [sort_str(x) for x in line[1]]
        digits = ""
        for x in output:
            digits += str(patterns[x])

        sum_of_output += int(digits)

    return sum_of_output


if __name__ == "__main__":
    data = input_data.get(8)

    print(f"Part 1: unique digits: {part1(data)}")
    print(f"Part 2: sum of output: {part2(data)}")