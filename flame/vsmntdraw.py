import random
import sys
import atexit
import pygame

pygame.init()

pal = (
    [(r, 0, 0) for r in range(0, 255, 5)]
    + [(255, g, 0) for g in range(0, 255, 3)]
    + [(255, 255, b) for b in range(0, 200, 5)]
)


class Draw:
    def __init__(self, w, h, scale):
        self.w = w
        self.h = h
        self.scale = scale
        self.should_exit = False

        self.screen = pygame.display.set_mode((self.w * scale, self.h * scale))
        self.clock = pygame.time.Clock()

    def get_matrix(self):
        return [[0] * self.w for _ in range(self.h)]

    def get_array(self):
        return [0] * self.w

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.should_exit = True

    def draw(self, matrix = None):
        self.clock.tick(20)

        self.handle_events()
        if self.should_exit:
            sys.exit()

        if matrix:
            if isinstance(matrix[0], int):
                for x in range(0, self.w):
                    pygame.draw.rect(
                        self.screen,
                        pal[matrix[x]],
                        (x * self.scale, 0, self.scale, self.scale),
                    )
            else:
                for y in range(0, self.h):
                    for x in range(0, self.w):
                        pygame.draw.rect(
                            self.screen,
                            pal[matrix[y][x]],
                            (x * self.scale, y * self.scale, self.scale, self.scale),
                        )

        pygame.display.flip()


d = None


def init(w, h, scale):
    global d
    assert d is None
    d = Draw(w, h, scale)


def get_matrix():
    assert d is not None
    return d.get_matrix()

def get_array():
    assert d is not None
    return d.get_array()


def draw(matrix):
    global d

    if d is None:
        if isinstance(matrix[0], int):
            w = len(matrix)
            h = 1
        else:
            h = len(matrix)
            w = len(matrix[0])
        scale = max(1, 1024 // max(w, h))
        d = Draw(w, h, scale)

    return d.draw(matrix)

def рисовать(matrix):
    draw(matrix)


def max_color():
    return len(pal) - 1


def случайный_цвет():
    return random.randint(0, max_color())


def finalize():
    assert d is not None
    while not d.should_exit:
        d.handle_events()
    pygame.quit()

atexit.register(finalize)
