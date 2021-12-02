with open('./data/day02puzzle.txt', 'r') as f:
    data = f.read().splitlines()
data = [x.split(' ') for x in data]

horizontal, depth = 0, 0
for command, extent in data:
    extent = int(extent)
    if command == 'down':
        depth += extent
    if command == 'up':
        depth -= extent
    if command == 'forward':
        horizontal += extent

answer1 = horizontal * depth

aim, horizontal, depth = 0, 0, 0
for command, extent in data:
    extent = int(extent)
    if command == 'down':
        aim += extent
    if command == 'up':
        aim -= extent
    if command == 'forward':
        horizontal += extent
        depth += aim * extent

answer2 = horizontal * depth

print(f'Puzzle 1 Answer:  {answer1}')
print(f'Puzzle 2 Answer:  {answer2}')
