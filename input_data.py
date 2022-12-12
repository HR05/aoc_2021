def get(day) -> list[str]:
    AOC_HOME = "C:/Users/Hannes/Desktop/files/aoc_2021"
    with open(f"{AOC_HOME}/input/{day}.txt") as f:
        content = f.read()
        lines = content.splitlines()
        return lines