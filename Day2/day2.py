
with open("input.txt") as f:
    commands = [(command[0], int(command[1])) for command in [i.split(" ") for i in f.readlines()]]

def part1(commands):
    depth = 0
    horizontal = 0

    for command in commands:
        if(command[0] == 'forward'):
            horizontal += command[1]
        elif(command[0] == 'down'):
            depth += command[1]
        elif(command[0] == 'up' and depth > command[1]):
            depth -= command[1]
    print(f'depth: {depth}, hortizontal: {horizontal}, total: {depth * horizontal}')
            

def part2(commands):
    depth = 0
    horizontal = 0
    aim = 0

    for command in commands:
        if(command[0] == 'forward'):
            horizontal += command[1]
            depth += aim * command[1]
        elif(command[0] == 'down'):
            aim += command[1]
        elif(command[0] == 'up'):
            aim -= command[1]
    print(f'depth: {depth}, hortizontal: {horizontal}, total: {depth * horizontal}')
part2(commands)