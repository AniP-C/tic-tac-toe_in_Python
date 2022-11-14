import pygame , sys
import numpy as np
# initialising the gane
pygame.init()

# defining constants
WIDTH = 600
HEIGHT = 600


RED = (255, 0, 0)
BG_COLOR = (28,178,156)


# radius of circle
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
CROSS_COLOR = (66, 66, 66)
CIRCLE_COLOR = (239, 231, 200)

# making the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# making parameters for the board
BOARD_ROWS = 3
BOARD_COLS = 3


# title in ppygame
pygame.display.set_caption('TIC TAC TOE')

# color and width of lines
LINE_COLOR = (23, 145 , 135)
LINE_WIDTH = 15

# colors in pygame
screen.fill(BG_COLOR)


#  board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
# print(board)

# drawing the line
# pygame.draw.line(screen, RED , (10,10) , (300, 300) , 10)

# function to draw lines
def draw_lines ():
    # 1st horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600, 200), LINE_WIDTH)
    
    # 2nd horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600, 400), LINE_WIDTH)
    
    #  1st vertical line
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200, 600), LINE_WIDTH)
    
    # 2nd vertical line
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400, 600), LINE_WIDTH)
    



#  function to mark the squares
def mark_square(row, col , player):
    board[row][col] = player
    

# function to draw figures
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] ==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col *200 + 100), int(row*200 + 100)) ,CIRCLE_RADIUS, CIRCLE_WIDTH )

            elif board[row][col] ==2 :
                pygame.draw.line(screen , CROSS_COLOR, (col*200 + SPACE, row *200 + 200 - SPACE), (col*200 +200 - SPACE, row*200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,  (col *200 + SPACE, row*200 + SPACE), (col*200 + 200 - SPACE, row*200 + 200 -SPACE), CROSS_WIDTH)

# function to make available empty squares
def available_square(row, col):
    return board[row][col] == 0

# above one and below one both the logic is same
    # if board[row][col] == 0:
    #     return True
    # else:
    #     False


# function to check is board full
def is_board_full ():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


# to check if player won
def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col , player)
            return True
            
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
        
        
    #  asc diagonal win check
    if board [ 2][ 0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonals(player)
        return True
    
    #  desc diagonal win check
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonals(player)
        return True  
    
    return False
                
            
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100
    
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color  = CROSS_COLOR
    
    pygame.draw.line(screen, color , (posX, 15), (posX, HEIGHT-15), 15)
    
    
    
    
def draw_horizontal_winning_line (row , player):
    posY = row *200 +100
    if player ==1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color , (15, posY), (WIDTH-15, posY) , 15)
        
        
        
def draw_asc_diagonals(player):
    if player ==1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color , (15, HEIGHT-15), (WIDTH - 15, 15), 15)






def draw_desc_diagonals(player):
    if player ==1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
        
        
    pygame.draw.line(screen, color , (15,15), (WIDTH - 15 , HEIGHT-15), 15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=  0
    
    
    
# print(is_board_full())
# for row in range(BOARD_ROWS):
#     for col in range(BOARD_COLS):
#         mark_square(row, col , 1)
        
# print(is_board_full())
# print(board)
player = 1
game_over = False
draw_lines()
# main loop
while True:
    
    # screen kese quite hogi , uska code hai
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        # getting mouse coordinates 
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] #for x coordinate
            mouseY = event.pos[1] # for y coordinate
            
            clicked_row = int(mouseY //200)
            clicked_col = int(mouseX //200)
            
            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col , 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                    
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
            
            
            
                draw_figures()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r :
                restart()
            
            
            
            
    # updating the screen
    pygame.display.update()


