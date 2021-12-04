import numpy as np

with open("Day04/input.txt") as f:
    readings = [line.strip() for line in f.readlines()]

bingo_numbers = readings[0].split(",")

bingo_cards = []
temp_bingo_card = []

for line in readings[2:]:
    if(line == ""):
        bingo_cards.append(np.vstack(temp_bingo_card))
        temp_bingo_card = []
    else:
        temp_bingo_card.append(np.fromstring(line, dtype=int, sep=' '))
bingo_cards.append(np.vstack(temp_bingo_card))

bingo_scores = [ np.ones((5, 5), dtype=int) for i in range(len(bingo_cards)) ]
completed = []
for number in bingo_numbers:
    if(len(completed) == len(bingo_cards)):
        break
    for i in range(len(bingo_cards)):
        if(i in completed):
            continue
        if(np.isin(number, bingo_cards[i])):
            coords = list(zip(*np.where(bingo_cards[i] == int(number))))[0]
            bingo_scores[i][coords[0], coords[1]] = 0
            rows_sum = np.sum(bingo_scores[i] ,axis=0)
            if(np.isin(0, rows_sum)):
                print(f"bingo card: {i} number: {number} total: {np.sum(bingo_scores[i] * bingo_cards[i]) * int(number)}")
                completed.append(i)
                continue
                

            column_sum = np.sum(bingo_scores[i] ,axis=1)
            if(np.isin(0, column_sum)):
                print(f"bingo card: {i} number: {number} total: {np.sum(bingo_scores[i] * bingo_cards[i]) * int(number)}")
                completed.append(i)
                continue
