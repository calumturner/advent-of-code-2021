with open("Day06/input.txt") as f:
    fish = [int(item) for item in [line.strip().split(",") for line in f.readlines()][0]]

def part1(fish):
    print(f"Initial state: {fish}")
    for i in range(256):
        new_fish = []
        for f in range(len(fish)):
            if fish[f] == 0:
                new_fish.append(8)
                fish[f] = 6
            else:
                fish[f] -= 1
        fish = fish + new_fish
        print(f"Day {i+1} done")
    print(f"Total: {len(fish)}")

def part2(fish):
    fish_counts = [0,0,0,0,0,0,0,0,0]
    for f in fish:
        fish_counts[f] += 1
    
    for i in range(256):
        new_fish = fish_counts[0]
        for j in range(len(fish_counts) - 1):
            fish_counts[j] = fish_counts[j+1]
        fish_counts[6] += new_fish
        fish_counts[8] = new_fish
        print(f"Day {i+1} done: {fish_counts} {sum(fish_counts)}")
    print(f"Total: {sum(fish_counts)}")
        

part2(fish)