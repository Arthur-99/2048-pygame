import pygame as pg
import sys
from pygame.locals import *
from cmd2048 import *

pg.init()

# screen setting
width = height = 500
screen = pg.display.set_mode((width, height))
screen.fill((80, 80, 80))

# fps setting
FPS = 30
clock = pg.time.Clock()

# font setting
font = pg.font.Font('PAPYRUS.ttf', width // sz // 3)


# drawing function
def draw_board(arr):
    cell_width = width / sz
    cell_height = height / sz

    for i in range(sz):
        for j in range(sz):
            if arr[i][j] != 0:
                # draw rect
                pg.draw.rect(screen, (255, 100, 80), (j * cell_width + 2,
                                                      i * cell_height + 2, cell_width - 3, cell_height - 3))

                # write text
                text = font.render(str(board[i][j]), True, (255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = ((j+0.5) * cell_width,
                                    (i+0.5) * cell_height)
                screen.blit(text, text_rect)


init()


# mainloop
while not lose(board) and not win(board):
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print(chr(event.key))
            if event.key == K_ESCAPE or event.key == K_q:
                pg.quit()
                sys.exit()

            update(chr(event.key))
            # print(board)

    # drawing
    screen.fill((80, 80, 80))
    draw_board(board)
    pg.display.flip()


# drawing win or lose pattern
font = pg.font.Font('PAPYRUS.ttf', 60)
if lose(board):
    text = font.render("You lose!", True, (200, 200, 200))
else:
    text = font.render("You win!", True, (200, 200, 200))


text_rect = text.get_rect()
text_rect.center = (width / 2, height / 2)
screen.blit(text, text_rect)
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print(chr(event.key))
            if event.key == K_ESCAPE or event.key == K_q:
                pg.quit()
                sys.exit()
    pg.display.flip()
