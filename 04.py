import input_data

def compute_score(board, number):
    sum_of_unmarked = 0
    for row in board:
        for x in row:
            if not x["marked"]:
                sum_of_unmarked += x["value"]
    return sum_of_unmarked * number

def mark_number(number):
        # check all numbers of the boards and mark it if it's the same
        for board in boards:
            for row in board:
                for x in row:
                    if x["value"] == number:
                        x["marked"] = True
                    
def print_board(board):
    for row in board:
        for x in row:
            if x["marked"]:
                print(f"[{x['value']}]", end="")
            else:
                print(f"({x['value']})", end="")
        print()


def part1(numbers, boards):
    for number in numbers:
        mark_number(number)
        # check if there is a winner
        for board in boards:
            for row in board:
                marked = 0
                for x in row:
                    if x["marked"]: marked += 1
                if marked == 5:
                    return compute_score(board, number)
            for i in range(len(board)):
                marked = 0
                for row in board:
                    if row[i]["marked"]: marked += 1
                if marked == 5:
                    return compute_score(board, number)


def part2(numbers, boards):
    winners = []
    winner_count = 0
    for number in numbers:
        mark_number(number)
        for index, board in enumerate(boards):
            for row in board:
                marked = 0
                for x in row:
                    if x["marked"]: marked += 1
                if marked == 5 and index not in winners:
                    winners += [index]
                    winner_count += 1
                    if winner_count == len(boards):
                        return compute_score(board, number)
            for i in range(len(board)):
                marked = 0
                for row in board:
                    if row[i]["marked"]: marked += 1
                if marked == 5 and index not in winners:
                    winners += [index]
                    winner_count += 1
                    if winner_count == len(boards):
                        return compute_score(board, number)


if __name__ == "__main__":
    data = input_data.get(4)
    bingo_numbers = [int(x) for x in data[0].split(",")]
    boards = []
    board = []
    for line in data[2:]:
        if line == "":
            boards += [board]
            board = []
            continue
        board += [[{"value": int(x), "marked": False} for x in line.split()]]
    boards += [board]

    print(f"Part 1: final score: {part1(bingo_numbers, boards)}")
    print(f"Part 2: final score: {part2(bingo_numbers, boards)}")