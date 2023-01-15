import pygame, sys
import numpy as np

pygame.init()

#class Zaidimas():
plotis = 600
aukstis = 600
linijos_plotis = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_widht = 15
cross_widht = 25
space = 55

raudona = (255, 0, 0)
juoda = (0, 0, 0)
balta = (248, 248, 255)
zalia = (0,255,0)
#bg_color = (28, 170, 156)
linijos_spalva = (23, 145, 135)

screen = pygame.display.set_mode( (plotis, aukstis) )
pygame.display.set_caption("Zaidimas")
screen.fill(raudona)


board = np.zeros( (board_rows, board_cols) )

#pygame.draw.line(screen, raudona, (10, 10), (300, 300) 10)
def draw_lines():
    pygame.draw.line(screen, linijos_spalva, (0, 200), (600, 200), linijos_plotis)
    pygame.draw.line(screen, linijos_spalva, (0, 400), (600, 400), linijos_plotis)
    pygame.draw.line(screen, linijos_spalva, (200, 0), (200, 600), linijos_plotis)
    pygame.draw.line(screen, linijos_spalva, (400, 0), (400, 600), linijos_plotis)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, juoda, (int(col * 200 + 100), int(row * 200 + 100)), circle_radius, circle_widht)
            elif board[row][col] == 2:
                pygame.draw.line(screen, balta, (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 + space), cross_widht)
                pygame.draw.line(screen, balta, (col * 200 + space, row * 200 + space), (col * 200 + 200 - space, row * 200 + 200 - space), cross_widht)

def mark_square(row, col, zaidejas):
    board[row][col] = zaidejas

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    
    return True

def check_win(zaidejas):
    for col in range(board_cols):
        if board[0][col] == zaidejas and board[1][col] == zaidejas and board[2][col] == zaidejas:
            draw_vertical_winning_line(col, zaidejas)
            return True

    for row in range(board_rows):
        if board[row][0] == zaidejas and board [row][1] == zaidejas and board[row][2] == zaidejas:
            draw_horizontal_winning_line(row, zaidejas)        
            return True

        if board[2][0] == zaidejas and board[1][1] == zaidejas and board[0][2] == zaidejas:
            draw_asc_diagonal(zaidejas)
            return True

        if board[0][0] == zaidejas and board[1][1] == zaidejas and board[2][2] == zaidejas:
            draw_desc_diagonal(zaidejas)
            return True

        return False

def draw_vertical_winning_line(col, zaidejas):
    posX = col * 200 + 100

    if zaidejas == 1:
        color = juoda
    elif zaidejas == 2:
        color = balta

    pygame.draw.line(screen, color, (posX, 15), (posX, aukstis - 15), 15)

def draw_horizontal_winning_line(row, zaidejas):
    posY = row * 200 + 100

    if zaidejas == 1:
        color = juoda
    elif zaidejas == 2:
        color = balta

    pygame.draw.line(screen, color, (15, posY), (plotis - 15, posY), 15)

def draw_asc_diagonal(zaidejas):
    if zaidejas == 1:
        color = juoda
    elif zaidejas == 2:
        color = balta

    pygame.draw.line(screen, color, (15, aukstis - 15), (plotis - 15, 15), 15)

def draw_desc_diagonal(zaidejas):
    if zaidejas == 1:
        color = juoda
    elif zaidejas == 2:
        color = balta

    pygame.draw.line(screen, color, (15, 15), (plotis - 15, aukstis - 15), 15)

def restart():
        pass

draw_lines()

zaidejas = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            peleX = event.pos[0]
            peleY = event.pos[1]

            clicked_row = int(peleY // 200)
            clicked_col = int(peleX // 200)

            if available_square(clicked_row, clicked_col):
                if zaidejas == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    check_win(zaidejas)
                    zaidejas = 2

                elif zaidejas == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    check_win(zaidejas)
                    zaidejas = 1


                draw_figures()

        pygame.display.update()
