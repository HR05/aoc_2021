import input_data

data = [int(x) for x in input_data.get(1)]

# ---------- Part 1 ----------
largerMeasurements = 0

for i, x in enumerate(data):
    if i+1 == len(data): break
    if x < data[i+1]:
        largerMeasurements += 1

print(f"Part 1(Larger measurements): {largerMeasurements}")


# ---------- Part 2 ----------
largerMeasurements = 0

for i, _ in enumerate(data):
    if i+3 == len(data): break
    currentWindow = data[i] + data[i+1] + data[i+2]
    nextWindow = data[i+1] + data[i+2] + data[i+3]
    if currentWindow < nextWindow:
        largerMeasurements += 1

print(f"Part 2(Larger three-measurements): {largerMeasurements}")