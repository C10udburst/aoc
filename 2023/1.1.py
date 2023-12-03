infile = open('1.in', 'r').read()

calibration = 0

for line in infile.splitlines():
    line = filter(lambda x: x in '0123456789', line)
    line = list(line)
    calibration += int(line[0])*10 + int(line[-1])

print(calibration)