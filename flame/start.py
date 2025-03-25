import random
from vsmntdraw import init, get_matrix, draw, max_color, get_array

W = 30
H = 1
init(W, H, 30)

a = get_array()

a[0] = 100

draw(a)
