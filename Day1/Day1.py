

with open("input.txt") as f:
    readings = [int(i) for i in f.readlines()]

def part1(readings):
    previous = readings[0]
    increase_count = 0
    for reading in readings[1:]:
        if(previous < reading):
            increase_count += 1
        previous = reading
    print(increase_count)



def part2(readings):
    increase_count = 0
    for window_index in range(len(readings)-3):
        first_window_total = sum([readings[window_index], readings[window_index+1], readings[window_index+2]])
        second_window_total = sum([readings[window_index+1], readings[window_index+2], readings[window_index+3]])
        if(first_window_total < second_window_total):
            increase_count += 1
    print(increase_count)

part2(readings)