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

def is_symbol(s):
    return s not in digits and s != '.' and s != '\n'

total_sum = 0
for y, line in enumerate(infile):
    number = 0
    has_symbol = False
    for x, c in enumerate(line):
        if c in digits:
            number *= 10
            number += int(c)
            
            for dx, dy in product([-1, 0, 1], repeat=2):
                    has_symbol = has_symbol or is_symbol(get(x + dx, y + dy))
        else:
            if has_symbol:
                total_sum += number
            number = 0
            has_symbol = False
    if has_symbol:
        total_sum += number
    
print(total_sum)
            