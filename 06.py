import input_data

def simulate(data, period):
    days_to_reproduce = [0 for i in range(9)]
    for day in data:
        days_to_reproduce[day] += 1
    
    for i in range(period):    
        new_days_to_reproduce = [0 for i in range(9)]
        for day, count in enumerate(days_to_reproduce):
            if day == 0:
                new_days_to_reproduce[8] = count
                new_days_to_reproduce[6] = count
            else:
                new_days_to_reproduce[day - 1] += count
        days_to_reproduce = new_days_to_reproduce

    return sum(days_to_reproduce)


if __name__ == "__main__":
    data = input_data.get(6)
    data = [int(n) for n in data[0].split(",")]
    print(f"Part 1: amount of laternfishes: {simulate(data, 80)}")
    print(f"Part 2: amount of laternfishes: {simulate(data, 256)}")