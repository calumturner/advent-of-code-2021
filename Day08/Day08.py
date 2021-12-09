with open("Day08/input.txt") as f:
    readings = [line.strip() for line in f.readlines()]


def part1(entry):
    _, output = entry
    count = 0
    for digit in output.split(" "):
        if(len(digit) in [2,4,3,7]):
            count += 1
    return count

total = 0
for line in readings:
    total += part1(line.split(" | "))
print(f"part 1: {total}")


def part2(line):
    signals, output = line.split(" | ")
    signals = signals.split()
    signals.sort(key=len)
    one = ''.join(sorted(signals[0]))
    seven = ''.join(sorted(signals[1]))
    four = ''.join(sorted(signals[2]))
    eight = ''.join(sorted(signals[9]))
    fives = signals[3:6]
    sixs = signals[6:9]
    for i in range(len(fives)):
        if len(set(fives[i]) - set(seven)) == 2:
            three = ''.join(sorted(fives[i]))
            del fives[i]
            break
    
    for i in range(len(sixs)):
        if len(set(sixs[i]) - set(three)) == 1:
            nine = ''.join(sorted(sixs[i]))
            del sixs[i]
            break
    
    for i in range(len(sixs)):
        if len(set(sixs[i]) - set(one)) == 4:
            zero = ''.join(sorted(sixs[i]))
            del sixs[i]
            break
    six = ''.join(sorted(sixs[0]))

    for i in range(len(fives)):
        if len(set(nine) - set(fives[i])) == 2:
            two = ''.join(sorted(fives[i]))
            del fives[i]
            break
    five = ''.join(sorted(fives[0]))

    mapping = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }

    result = ''
    for digit in output.split(' '):
        result += mapping.get(''.join(sorted(digit)))
    print(f'result: {result}')
    return int(result)

total = 0
for line in readings:
    total += part2(line)
print(f"part 2: {total}")

# Order of operations
# 3 = 5s - 7
# 9 = 6s - 3
# 0 = 6s - 1
# 6 = last 6
# 2 = 9 - 5s
# 5 = last 5

# Segment count
# 1 = 2 letters
# 7 = 3 letters
# 4 = 4 letters

# 2 = 5 letters
# 3 = 5 letters
# 5 = 5 letters

# 0 = 6 letters
# 6 = 6 letters
# 9 = 6 letters

# 8 = 7 letters