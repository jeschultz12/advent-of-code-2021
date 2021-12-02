with open('./data/day01puzzle.txt', 'r') as f:
    data = f.read().splitlines()
    
answer1 = sum(int(y) > int(x) for x, y in zip(data, data[1:]))

answer2 = 0
for (a1, a2, a3), (b1, b2, b3) in zip(zip(data, data[1:], data[2:]),
                                  zip(data[1:], data[2:], data[3:])):
    a = int(a1) + int(a2) + int(a3)
    b = int(b1) + int(b2) + int(b3)
    if b > a:
        answer2 += 1

print(f'Puzzle 1 Answer:  {answer1}')
print(f'Puzzle 2 Answer:  {answer2}')
