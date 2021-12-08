import numpy as np

with open("Day07/input.txt") as f:
    raw_sub_positions = [int(item) for item in [line.strip().split(",") for line in f.readlines()][0]]


sub_positions = np.array(raw_sub_positions)
med = round(np.average(sub_positions))

def calculate_total_fuel_usage_part_1(target, sub_positions):
    total = 0
    for pos in sub_positions:
        total += abs(pos - target)
    return total

def calculate_total_fuel_usage_part_2(target, sub_positions):
    total = 0
    for pos in sub_positions:
        total += np.sum(list(range(abs(pos - target)+1)))
    return total

total = calculate_total_fuel_usage_part_2(med, sub_positions)
print(total)
