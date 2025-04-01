import random

from vsmntdraw import init, get_matrix, draw, max_color

W = H = 128

init(W, H, 6)

a = get_matrix()

while True:
    for x in range(0, 100, 1):
        a[H - 1][x] = random.choice([0, max_color()])

    draw(a)
