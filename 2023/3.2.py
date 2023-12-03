from string import digits
from itertools import product

infile = open('3.in', 'r').readlines()

def get(x, y):
    if x < 0 or y < 0:
        return '.'
    if y >= len(infile):
        return '.'
    line = infile[y].strip()
    if x >= len(line):
        return '.'
    return line[x]

def find_start(x, y):
    if get(x, y) not in digits:
        return (-1, -1)
    if get(x + 1, y) not in digits:
        return (x, y)
    return find_start(x + 1, y)

def left_number(x, y, visited):
    if (x, y) in visited:
        return None
    if get(x, y) not in digits:
        return None
    num = int(get(x, y))
    visited.add((x, y))
    num += (left_number(x - 1, y, visited) or 0) * 10
    return num
    

total_sum = 0
for y, line in enumerate(infile):
    for x, c in enumerate(line):
        if c != '*':
            continue
        numbers = []
        visited = set()
        for dx, dy in product([-1, 0, 1], repeat=2):
            nx, ny = find_start(x + dx, y + dy)
            num = left_number(nx, ny, visited)
            if num is not None:
                numbers.append(num)
            if len(numbers) > 2:
                break
            
        if len(numbers) == 2:
            total_sum += numbers[0] * numbers[1]
            
print(total_sum)
        