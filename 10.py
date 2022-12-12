import input_data

def find_syntax_error(line):
    syntax_tree = []

    tags = {")": "(", "]": "[", "}": "{", ">": "<"}

    for x in line:
        if x in "([{<":
            syntax_tree.append(x)
        elif tags[x] == syntax_tree[-1]:
            syntax_tree.pop()
        else:
            return x

    return -1
            
def get_score(line):
    POINTS = {")": 1, "]": 2, "}": 3, ">": 4}

    syntax_tree = []

    tags = {"(": ")", "[": "]", "{": "}", "<": ">"}

    for x in line:
        if x in "([{<":
            syntax_tree.append(x)
        else:
            syntax_tree.pop()

    completion = [tags[x] for x in syntax_tree]
    completion.reverse()

    score = 0

    for x in completion:
        score *= 5
        score += POINTS[x]

    return score


def part1(data):
    POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
    
    err_score = 0
    
    for line in data:
        err_chr = find_syntax_error(line)

        if err_chr == -1: continue

        err_score += POINTS[err_chr]

    return err_score

        

def part2(data):
    scores = []

    for line in data:
        if find_syntax_error(line) != -1: continue
        
        scores.append(get_score(line))

    scores.sort()

    return scores[len(scores) // 2]


if __name__ == "__main__":
    data = input_data.get(10)

    print(f"Part 1: syntax error score: {part1(data)}")
    print(f"Part 2: middle score: {part2(data)}")