import input_data
import math

def fill_bin(binary, length):
    return (length - len(binary)) * '0' + binary

class Packet:
    def __init__(self, version: int, type_id: int) -> None:
        self.version = version
        self.type_id = type_id


class OperatorPacket(Packet):
    def __init__(self, version: int, type_id: int, length_type_id: int, subpackets_length: int) -> None:
        self.length_type_id = length_type_id
        self.subpackets_length = subpackets_length
        self.subpackets = []
        super().__init__(version, type_id)

    @property
    def value(self):
        values_of_subpackets = [packet.value for packet in self.subpackets]
        if self.type_id == 0:
            return sum(values_of_subpackets)
        elif self.type_id == 1:
           return math.prod(values_of_subpackets)
        elif self.type_id == 2:
            return min(values_of_subpackets)
        elif self.type_id == 3:
            return max(values_of_subpackets)
        elif self.type_id == 5:
            return int(values_of_subpackets[0] > values_of_subpackets[1])
        elif self.type_id == 6:
            return int(values_of_subpackets[0] < values_of_subpackets[1])
        elif self.type_id == 7:
            return int(values_of_subpackets[0] == values_of_subpackets[1])

    @property
    def version_sum(self):
        return sum([packet.version_sum for packet in self.subpackets]) + self.version

    def add_packet(self, packet: Packet) -> None:
        self.subpackets.append(packet)

    def to_binary(self):
        version = fill_bin(bin(self.version)[2:], 3)
        type_id = fill_bin(bin(self.type_id)[2:], 3)
        subpackets_length = fill_bin(bin(self.subpackets_length), 15 if self.length_type_id == 0 else 1) 
        header = f"{version}{type_id}{self.length_type_id}{subpackets_length}"
        
        binary_subpackets = "".join([packet.to_binary() for packet in self.subpackets])

        return header + binary_subpackets

    def print(self, padding: str="") -> None:
        print(f"{padding}OperatorPacket({self.version=}, {self.type_id=}, {self.value=})")
        for packet in self.subpackets:
            packet.print(padding + "    ")

class ValuePacket(Packet):
    def __init__(self, version: int, type_id: int, value: int) -> None:
        self.value = value
        self.version_sum = version
        super().__init__(version, type_id)

    def to_binary(self):
        version = fill_bin(bin(self.version)[2:], 3)
        type_id = fill_bin(bin(self.type_id)[2:], 3)

        binary_value = ""
        value = bin(self.value)[2:]
        # continue ...

    def print(self, padding: str) -> None:
        print(f"{padding}ValuePacket({self.version=}, {self.type_id=}, {self.value=})")


class Parser:
    def __init__(self, input: str) -> None:
        self.input = input
        self.bits_parsed = 0
        self.packets = []

    def parsed_bits(self, count: int) -> None:
        self.input = self.input[count:]
        self.bits_parsed += count

    def parse(self) -> Packet:
        return self.parse_packet()

    def parse_packet(self) -> Packet:
        version = int(self.input[:3], 2)
        type_id = int(self.input[3:6], 2)
        self.parsed_bits(6)
        
        if type_id != 4:
            packet = self.parse_operator_packet(version, type_id)
        else:
            packet = self.parse_value_packet(version)

        self.packets.append(packet)
        return packet


    def parse_operator_packet(self, version: int, type_id: int) -> OperatorPacket:
        length_type = int(self.input[0])

        if length_type == 0:
            subpackets_len = int(self.input[1:16], 2)
            self.parsed_bits(16)
        elif length_type == 1:
            subpackets_len = int(self.input[1:12], 2)
            self.parsed_bits(12)

        packet = OperatorPacket(version, type_id, length_type, subpackets_len)

        prev_bits_parsed = self.bits_parsed

        while subpackets_len > 0:
            packet.add_packet(self.parse_packet())
            if length_type == 0:
                subpackets_len -= self.bits_parsed - prev_bits_parsed
                prev_bits_parsed = self.bits_parsed
            elif length_type == 1:
                subpackets_len -= 1

        return packet


    def parse_value_packet(self, version: int) -> ValuePacket:
        not_last = True
        binary_value = ""

        while not_last:
            not_last = bool(int(self.input[0]))
            binary_value += self.input[1:5]
            self.parsed_bits(5)

        return ValuePacket(version, 4, int(binary_value, 2))


def part1(data):
    parser = Parser(data)
    packet = parser.parse()

    sum_of_versions = 0

    for packet in parser.packets:
        sum_of_versions += packet.version
        
    return packet.version_sum

def part2(data):
    parser = Parser(data)
    packet = parser.parse()

    packet.print()

    return packet.value


if __name__ == "__main__":
    data = input_data.get(16)[0]
    binary_data = ""
    
    for i in range(len(data)):
        binary_int = bin(int(data[i], 16))[2:]
        binary_data += fill_bin(binary_int, 4)
    
    print(f"Part 1: {part1(binary_data)}")
    print(f"Part 2: {part2(binary_data)}")