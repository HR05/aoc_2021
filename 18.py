import input_data

class Pair:
    def __init__(self, input="[0, 0]", parent=None) -> None:
        self.left = None
        self.right = None
        self.parent = parent
        self.parse(input)

    def parse(self, input: str) -> None:
        brackets = []
        for i, x in enumerate(input):
            if x == "[":
                brackets.append(i)
            elif x == "]":
                brackets.pop()
            elif x == ",":
                if len(brackets) == 1:
                    split = i
            
        self.left = self.get_pair_or_value(input[1:split])
        self.right = self.get_pair_or_value(input[split+1:-1])

    def get_pair_or_value(self, input: str):
        if "[" in input:
            return Pair(input, self)
        return int(input)

    # add a number to the first regular number in this direction
    def add(self, direction: str, number: int):
        opposite_direction: str = "left" if direction == "right" else "right"
        pair: Pair = self
        parent: Pair = self.parent
        while parent.__getattribute__(direction) == pair:
            pair = parent
            parent = parent.parent
            if parent == None: return

        if type(parent.__getattribute__(direction)) == int:
            parent.__setattr__(direction, parent.__getattribute__(direction) + number)
        else:
            pair = parent.__getattribute__(direction)
            while type(pair.__getattribute__(opposite_direction)) == Pair:
                pair = pair.__getattribute__(opposite_direction)
            pair.__setattr__(opposite_direction, pair.__getattribute__(opposite_direction) + number)

    def explode(self) -> None:
        self.add("left", self.left)
        self.add("right", self.right)
        if self.parent.left == self:
            self.parent.left = 0
        else:
            self.parent.right = 0

    def split(self, side: str) -> None:
        half_number = self.__getattribute__(side) / 2
        self.__setattr__(side, Pair(f"[{int(half_number)},{int(half_number + 0.6)}]", self))

    def splited(self, side) -> bool:
        if self.__getattribute__(side) > 9:
            self.split(side)
            return True
        return False

    def reduced(self, nested: int = 0) -> bool:
        if nested == 4:
            self.explode()
            return True
        
        if type(self.left) == Pair:
            if self.left.reduced(nested + 1):
                return True
        elif self.splited("left"):
            return True
            
        if type(self.right) == Pair:
            if self.right.reduced(nested + 1):
                return True
        elif self.splited("right"):
            return True

        return False
            
    def __repr__(self) -> str:
        return f"[{self.left},{self.right}]"

    def __add__(self, other):
        return Pair(f"[{self},{other}]")

    def __radd__(self, other):
        return Pair(f"[{self},{other}]")

def part1(pairs):
    pair: Pair = pairs[0]
    for i in range(1, len(pairs)):
        pair += pairs[i]
        while pair.reduced():
            pass #print(pair)

    return pair

if __name__ == "__main__":
    data = input_data.get(18)

    pairs = []

    for pair in data:
        pairs.append(Pair(pair))
    
    print(f"Part 1: {part1(pairs)}")
    #print(f"Part 2: {part2(area)}")