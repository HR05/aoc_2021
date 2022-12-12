import input_data
import matplotlib.pyplot as plt

def fold(poses: list[int, int], fold_pos: tuple[str, int]):
    map_coor = {"x": 0, "y": 1}
    coor = map_coor[fold_pos[0]]
    
    for pos in poses:
        if pos[coor] > fold_pos[1]:
            pos[coor] = fold_pos[1] - (pos[coor] - fold_pos[1])

    for pos in list(poses):
        while poses.count(pos) > 1:
            poses.remove(pos)


def part1(poses, folds):
    fold(poses, folds[0])
    
    return len(poses)

def part2(poses, folds):
    for fols_pos in folds:
        fold(poses, fols_pos)

    x = [pos[0] for pos in poses]
    y = [pos[1] for pos in poses]
    y = [max(y) - i for i in y]

    plt.plot(x, y, "o")
    plt.show()

    return len(poses)

if __name__ == "__main__":
    data = input_data.get(13)

    poses = []
    folds = []

    for line in data:
        if line.startswith("fold along"):
            line = line.replace("fold along ", "")
            folds.append((line.split("=")[0], int(line.split("=")[1])))
        elif line != "":
            poses.append([int(x) for x in line.split(",")])

    print(f"Part 1: dots count: {part1(poses, folds)}")
    print(f"Part 2: dots count: {part2(poses, folds)}")