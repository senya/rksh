import random

from vsmntdraw import init, get_matrix, draw, max_color

W = H = 128

init(W, H, 6)

a = get_matrix()

while True:
    for x in range(20, 100, 1):
        a[H - 1][x] = a[H - 2][x] = (
            random.randint(0, 1) * max_color()
        )

    for y in range(H - 2):
        for x in range(1, W - 1):
            mid = (a[y + 1][x] + a[y + 1][x - 1] + a[y + 1][x + 1] + a[y + 2][x]) // 4
            if mid > 0:
                mid -= 1

            a[y][x] = mid

    for x in range(W):
        a[H - 1][x] = a[H - 2][x] = 0

    draw(a)
