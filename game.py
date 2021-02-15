import pygame
import sys
import random

# Testikommentti

"""
Tetris
"""
# Init pygame and it's fonts
pygame.init()
pygame.font.init()

# Set global variables/constants
running = True
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 1200
PLAY_WIDTH, PLAY_HEIGHT = 600, 1200
BLOCK_SIZE = 30
FPS = 30

# Shapes
O = [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]

I = [[[0, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 0, 0],
      ],
     [[0, 0, 0, 0],
      [1, 1, 1, 1],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]
     ]

# Colors as RGB values
gray = (128, 128, 128)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

shapes = [O, I]
colors = [gray, black, red, green, blue]

grid = [[black for col in range(PLAY_WIDTH // BLOCK_SIZE)] for row in range(PLAY_HEIGHT // BLOCK_SIZE)]


class Tetris:
    def __init__(self):
        self.__window_width = WINDOW_WIDTH
        self.__window_height = WINDOW_HEIGHT
        self.__screen = pygame.display.set_mode(self.getSize())
        self.__objects = []

        pygame.display.set_caption("Tetris")

    def getSize(self):
        return self.__window_width, self.__window_height

    def getObjects(self):
        return self.__objects

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def drawWindow(self):
        self.__screen.fill(black)
        for obj in self.__objects:
            self.__screen.blit(obj.getSurface(), obj.getArea())
        pygame.display.flip()

    def drawGrid(self, grid):
        for col in range(len(grid)):
            for row in range(len(grid[col])):
                pygame.draw.rect(self.__screen, grid[col][row],
                                 (row * BLOCK_SIZE, col * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

    def addPiece(self):
        piece = Piece()
        self.__objects.append(piece)

    def addSidebar(self):
        sidebar = Sidebar()
        self.__objects.append(sidebar)


class Piece(object):
    rows = PLAY_HEIGHT // BLOCK_SIZE
    columns = PLAY_WIDTH // BLOCK_SIZE

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0


class Sidebar:
    def __init__(self):
        self.__surface = pygame.Surface((WINDOW_WIDTH - PLAY_WIDTH, WINDOW_HEIGHT))
        self.__area = self.__surface.get_rect()
        self.__area.top = 0
        self.__area.left = PLAY_WIDTH
        self.__surface.fill(gray)

    def getSurface(self):
        return self.__surface

    def getArea(self):
        return self.__area


if __name__ == "__main__":
    tetris = Tetris()
    tetris.addSidebar()

while running:
    tetris.eventHandler()
    tetris.drawWindow()
    tetris.drawGrid(grid)
    pygame.time.wait(100)
