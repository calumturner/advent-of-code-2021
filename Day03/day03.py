import operator

def part1(readings):
    reading_count= len(readings)
    bit_counts = ['1' if i.count('1') > reading_count/2 else '0' for i in zip(*readings)]

    gamma = "".join(bit_counts)
    epsilon = "".join('0' if bit=='1' else '1' for bit in bit_counts)
    print(f"gamma: {gamma}, epsilon: {epsilon}")
    print(f"gamma: {int(gamma, 2)}, epsilon: {int(epsilon, 2)}, power: {int(gamma, 2) * int(epsilon, 2)}")


def filter_rows_by_bit_criteria(readings, index, operator):
    most_common_threshold = len(readings) / 2
    bucketed_bits = list(zip(*readings))
    most_common_bit = '1' if operator(bucketed_bits[index].count('1'), most_common_threshold) else '0'

    return [readings[i] for i, item in enumerate(bucketed_bits[index]) if item == most_common_bit]


def part2(readings):
    o2_gen_rating = readings
    for x in range(len(readings[0])):
        o2_gen_rating = filter_rows_by_bit_criteria(o2_gen_rating, x , operator.ge)
        if len(o2_gen_rating) == 1:
            break


    co2_scrub_rating = readings
    for x in range(len(readings[0])):
        co2_scrub_rating = filter_rows_by_bit_criteria(co2_scrub_rating, x , operator.lt)
        if len(co2_scrub_rating) == 1:
            break

    print(f"o2: {int(o2_gen_rating[0], 2)}, co2: {int(co2_scrub_rating[0], 2)}, life support rating: {int(o2_gen_rating[0], 2) * int(co2_scrub_rating[0], 2)}")



with open("Day03/input.txt") as f:
    readings = [line.strip() for line in f.readlines()]

part2(readings)
