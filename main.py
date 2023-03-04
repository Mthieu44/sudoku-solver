import pygame
import sys
from fonctions import solve_sudoku
pygame.init()

size = (360, 360)
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 40)
grid = [[0 for _ in range(9)] for _ in range(9)]
initial_grid = [[i for i in j] for j in grid]


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = x//40
            y = y//40
            if event.button == 1:
                grid[y][x] = grid[y][x] + 1 if grid[y][x] < 9 else 0
            if event.button == 3:
                grid[y][x] = grid[y][x] - 1 if grid[y][x] > 0 else 9
            
            initial_grid = [[i for i in j] for j in grid]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = [[0 for _ in range(9)] for _ in range(9)]
            if event.key == pygame.K_RETURN:
                grid = solve_sudoku(grid)

    screen.fill("white")

    for i in range(9):
        for j in range(9):
            if grid[j][i] != 0:
                if initial_grid[j][i] == 0:
                    text = font.render(str(grid[j][i]), True, (255, 0, 0))
                else:
                    text = font.render(str(grid[j][i]), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (i * 40 + 20, j * 40 + 21)
                screen.blit(text, text_rect)

    for i in range(0, 10):
        if i % 3 == 0 and i != 0:
            pygame.draw.line(screen, "black", (i*40, 0), (i*40, 360), 3)
            pygame.draw.line(screen, "black", (0, i*40), (360, i*40), 3)
        else:
            pygame.draw.line(screen, "black", (i*40, 0), (i*40, 360))
            pygame.draw.line(screen, "black", (0, i*40), (360, i*40))

    pygame.display.flip()
