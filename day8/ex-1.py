import math

test_h = int(input('Height of the wall: '))
test_w = int(input('Width of the wall: '))
coverage = 5


def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / coverage)
    print(f'{cans} required to paint the wall')


paint_calc(height=test_h, width=test_w, cover=coverage)
