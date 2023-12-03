infile = open('1.in', 'r').read()

digitmap = {
    'o': {
        'n': {
            'e': 1,
        }
    },
    't': {
        'w': {
            'o': 2,
        },
        'h': {
            'r': {
                'e': {
                    'e': 3,
                }
            }
        }
    },
    'f': {
        'o': {
            'u': {
                'r': 4,
            }
        },
        'i': {
            'v': {
                'e': 5,
            }
        }
    },
    's': {
        'i': {
            'x': 6,
        },
        'e': {
            'v': {
                'e': {
                    'n': 7,
                }
            }
        }
    },
    'e': {
        'i': {
            'g': {
                'h': {
                    't': 8,
                }
            }
        }
    },
    'n': {
        'i': {
            'n': {
                'e': 9,
            }
        }
    },
    'z': {
        'e': {
            'r': {
                'o': 0,
            }
        }
    },
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

calibration = 0

for line in infile.splitlines():
    numbers = []
    for char in line:
        for i, v in enumerate(numbers):
            if type(v) == dict:
                numbers[i] = numbers[i].get(char)
        numbers.append(digitmap.get(char))
        numbers = list(filter(lambda x: x is not None, numbers))
    numbers = list(filter(lambda x: type(x) == int, numbers))
    calibration += int(numbers[0])*10 + int(numbers[-1])
    
print(calibration)