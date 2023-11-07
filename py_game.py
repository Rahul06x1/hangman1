import pygame
import sys
from life import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 20
GRID_WIDTH = 7
GRID_HEIGHT = 7


def generate_grid(surface, matrix):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            cell = matrix[row][col]
            if cell == ALIVE:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(surface, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Conway's Game of Life")

    matrix = [
        [DEAD, DEAD, DEAD, DEAD, ALIVE, ALIVE, ALIVE],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
        [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        generate_grid(screen, matrix)
        pygame.display.update()
        pygame.time.delay(200)
        matrix = update_matrix(matrix)
        pygame.time.Clock()


if __name__ == "__main__":
    main()
