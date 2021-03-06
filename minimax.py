
import pygame


pygame.init()


HEIGHT = 800
WIDTH = 800
WHITE = (46,139,87)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
who_won = 0 
#[[0,0,-1],[-1,1,1],[1,0,-1]]
board = [[0,0,0],[0,0,0],[0,0,0]]
game_over = False
img_X = pygame.image.load("MiniMax_Tictactoe/X.png")
img_X = pygame.transform.scale(img_X,(200,200))
img_O = pygame.image.load("MiniMax_Tictactoe/O.png")
img_O = pygame.transform.scale(img_O,(200,200))
font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render("X WINS",False,("RED"),(0,0,0))
text2 = font.render("O WINS",False,("RED"),(0,0,0))
text3 = font.render("DRAW",False,("RED"),(0,0,0))
text4 = font.render("NEW GAME",False,("RED"),(0,0,0))

def display_board():
    margin = 5
    block_size = WIDTH //  3 - margin
    full_width,full_height = margin + block_size,margin + block_size
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(Screen, WHITE,[full_width * j + margin, full_height * i + margin, block_size, block_size])
            if board[i][j] == 1:
                Screen.blit(img_X,(full_width * j + 20, full_height * i + 20 ))
            if board[i][j] == -1:
                Screen.blit(img_O,(full_width * j + 20, full_height * i + 20 )) 


def possible_options():
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                possible_moves.append((i,j))
    return possible_moves
def new_game():
    global board, game_over
    board = [[0,0,0],[0,0,0],[0,0,0]]
    game_over = False
def game_over_screen():
    if who_won == 1:
        Screen.blit(text1,(350,810))
    elif who_won == -1:
        Screen.blit(text2,(350,810))
    else:
        Screen.blit(text3,(350,810))
    Screen.blit(text4,(330,850))


def print_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()
    print("---------------------------------")

def findBestMove() :
    bestVal = 1000
    bestMove = (-1, -1)
    drawMove = (0,0)
    moves = possible_options()
    for i,j in moves:  
        if board[i][j] == 0 :  
            board[i][j] = -1
            moveVal = minimax(board, 0, True)  
            board[i][j] = 0       
            if (moveVal == -1) :               
                bestMove = (i, j)
                bestVal = moveVal
                break 
            elif(moveVal == 0):
                drawMove = (i,j)

    print("Best Play goes to:", bestVal)
    if bestMove != (-1,-1):
        x = bestMove[0]
        y = bestMove[1]
        board[x][y] = -1
    else:
        x = drawMove[0]
        y = drawMove[1]
        board[x][y] = -1 



def minimax(board,depth,turn):

    if check_win() != None:
        return check_win()
        
   
    #minimizing play
    if turn == False:
        
        best_move = 1000
        for x in range(3):
            for y in range(3):
                if board[x][y] == 0:
                    board[x][y] = -1
                    #print_board()
                    best_move = min(best_move,minimax(board,depth+1,True))
                    board[x][y] = 0
            

       
        return best_move
    #maximizing play
    else:
        best_move = -1000
      
        for x in range (3):
            for y in range(3):
                if board[x][y] == 0:
                    board[x][y] = 1
                    #print_board()
                    best_move = max(best_move,minimax(board,depth+1,False))
                
                    board[x][y] = 0
            

        return best_move



        
def check_win():

    counter = 0
    if sum(board[0]) == 3 or sum(board[1]) == 3 or sum(board[2])  == 3:
        return 1
    if sum(board[0]) == -3 or sum(board[1]) == -3 or sum(board[2] ) == -3:
        return -1
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
        return 1
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
        return -1
    if board[0][0] + board[1][1] + board[2][2] == -3:
        return 1
    for i in range(3):
        
        if sum(([row[i] for row in board])) == 3:
            return 1
        if sum(([row[i] for row in board])) == -3:
            return -1
        if 0 not in board[i]:
            counter += 1 
    if counter == 3:
        return 0 


if __name__ == "__main__":
    Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("TIC_TAC_TOE")
    Clock = pygame.time.Clock()
    Screen.fill("black")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = list(pygame.mouse.get_pos())
                x = pos[0] // 261
                y = pos[1] // 261
                if event.button == 1:
                   if game_over == False:
                        board[y][x] = 1
                        who_won = check_win()
                        c =minimax(board,0,False)
                        print(c)
                        findBestMove()
                        
                   else:
                        mouse = pygame.mouse.get_pos()
                        if 333 <= mouse[0] <= 509 and 850 <= mouse[1] <= 878:
                            new_game()
                if event.button == 3:
                   if game_over == False:
                        board[y][x] = -1 
                        who_won = check_win()
                        b = minimax(board,0,True)
                        print(b)
        display_board()
        if game_over != False:
            game_over_screen()
        pygame.display.update()
        Clock.tick(60)
