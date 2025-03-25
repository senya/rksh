import sys
import atexit
import pygame


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

        pygame.init()
        self.screen = pygame.display.set_mode((self.w * scale, self.h * scale))
        self.clock = pygame.time.Clock()

    def get_matrix(self):
        return [[0] * self.w for _ in range(self.h)]

    def get_array(self):
        return [0] * self.w

    def draw(self, matrix):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit1")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("quit")
                    pygame.quit()
                    sys.exit()

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
        print(self.clock.tick(20))


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
    assert d is not None
    return d.draw(matrix)


def max_color():
    return len(pal) - 1


def finalize():
    print("stop")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("quit")
                    pygame.quit()
                    sys.exit()
        clock.tick(20)

atexit.register(finalize)
