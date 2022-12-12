import input_data

class Probe:
    def __init__(self, target_area: list[list[int]]) -> None:
        self.target_area_x, self.target_area_y = target_area
        self.longest_x = -min(self.target_area_x) if min(self.target_area_x) < 0 else max(self.target_area_x)
        self.deepest_y = min(self.target_area_y)
        self.reset()

    def get_max_y_velo(self) -> int:
        if self.deepest_y < 0:
            return -self.deepest_y - 1
        return max(self.target_area_y)

    def get_max_y(self) -> int:
        y = 0
        y_velo = self.get_max_y_velo()
        for i in range(y_velo):
            y += y_velo - i
        return y

    def get_all_init_velo(self) -> list[tuple[int, int]]:
        velocities = []
        for x in range(max(self.target_area_x) + 1):
            for y in range(min(self.target_area_y), -min(self.target_area_y)):
                if self.will_be_in_target_area(x, y):
                    velocities.append((x, y))

        return velocities

    def will_be_in_target_area(self, x_velo: int, y_velo: int) -> bool:
        self.reset()
        self.x_velo = x_velo
        self.y_velo = y_velo

        while not self.is_over_target_area():
            if self.is_in_target_area():
                return True
            self.next_step()

        return False

    def is_in_target_area(self) -> bool:
        if self.x in self.target_area_x and self.y in self.target_area_y:
            return True
        return False

    def reset(self) -> None:
        self.x_velo, self.y_velo, self.x, self.y = 0, 0, 0, 0

    def is_over_target_area(self) -> bool:
        if abs(self.x) > self.longest_x or self.y < self.deepest_y:
            return True
        return False

    def next_step(self) -> None:
        self.x += self.x_velo
        self.y += self.y_velo
        self.x_velo -= 1 if self.x_velo > 0 else 0
        self.y_velo -= 1

def part1(area):
    probe = Probe(area)
    return probe.get_max_y()

def part2(area):
    probe = Probe(area)
    return len(probe.get_all_init_velo())

if __name__ == "__main__":
    data = input_data.get(17)
    
    data = data[0].replace("target area: x=", "")
    data = data.replace(" y=", "")

    area = []

    for coor in data.split(","):
        n1, n2 = [int(x) for x in coor.split("..")]
        area.append(list(range(n1, n2 + 1)))

    print(f"Part 1: {part1(area)}")
    print(f"Part 2: {part2(area)}")