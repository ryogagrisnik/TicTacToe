import turtle
turtle.speed(0)
turtle.hideturtle()
end_game = False


# initial board state
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

def draw_board():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    for i in range(4):
        turtle.forward(300)
        turtle.left(90)
    turtle.goto(0, 0)
    
    for i in range(1, 3):
        turtle.penup()
        turtle.goto(0 + i * 100, 0)
        turtle.pendown()
        turtle.goto(0 + i * 100, 300)
        turtle.penup()
        turtle.goto(0, 0 + i * 100)
        turtle.pendown()
        turtle.goto(300, 0 + i * 100)

def find_box_middle(x, y):
    for i in range(1, 4):
        if x > (i -1) * 100 and x < i * 100 :
            mid_x =  (i - 0.5) * 100
    for i in range(1, 4):
        if y > (i -1) * 100 and y < i * 100:
            mid_y = (i - 0.5) * 100
    return mid_x, mid_y

def check_win():
    board_full = True

    global end_game
    #we need to check for win conditions after every move, so we need to keep track of where the Xs and Os are placed and check if there are 3 in a row for either player. 
    state_dict = {'Completion1': [board[0][0], board[0][1], board[0][2]],
         'Completion2': [board[1][0], board[1][1], board[1][2]],
         'Completion3': [board[2][0], board[2][1], board[2][2]], 
         'Completion4': [board[0][0], board[1][0], board[2][0]],
         'Completion5': [board[0][1], board[1][1], board[2][1]],
         'Completion6': [board[0][2], board[1][2], board[2][2]],
         'Completion7': [board[0][0], board[1][1], board[2][2]],
         'Completion8': [board[0][2], board[1][1], board[2][0]]
        }
    for key in state_dict:
        if state_dict[key] == ['X' , 'X', 'X']:
            print('Player 1 Wins')
            turtle.pencolor('blue')
            turtle.write('PLAYER ONE WINS', move=False, align="left", font=("Times New Roman", 15, "normal"))
            end_game = True

            turtle.done
            return
        
        elif state_dict[key] == ['O' , 'O', 'O']:
            print('Player 2 Wins')
            turtle.pencolor('red')
            turtle.write('PLAYER TWO WINS', move=False, align="left", font=("Times New Roman", 15, "normal"))
            end_game = True
            turtle.done 
            return
    
    for row in board:
        if None in row:
            board_full = False
            continue 
    if board_full == True:
        print('Tie game')
        turtle.pencolor('green')
        turtle.write('TIE GAME', font=("Times New Roman", 15, "normal"))
        turtle.done
        return

#need to add functionality for players to click and place their X or O on the board, and also need to check for win conditions.
round_number = 1
def place_mark(x, y):
    global round_number, end_game
    if end_game == True:
        return
    
    #we're going to subdivide board into 9 parts and check which part of the board the click belongs to a place the respective mark there 
    locations = {'box1': (0, 0, 100, 100), 'box2': (100, 0, 200, 100), 'box3': (200, 0, 300, 100),
                 'box4': (0, 100, 100, 200), 'box5': (100, 100, 200, 200), 'box6': (200, 100, 300, 200),
                 'box7': (0, 200, 100, 300), 'box8': (100, 200, 200, 300), 'box9': (200, 200, 300, 300)}
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for i  in range(len(locations)):
        #loop through locations and see which box the click belongs to and place mark ther
        if x > locations['box' + str(i+1)][0] and x < locations['box' + str(i+1)][2] and y > locations['box' + str(i+1)][1] and y < locations['box' + str(i+1)][3]:
            
            if board[i//3][i%3] is not None:
                return
            
            if round_number % 2 == 0:
                ## now we need to make sure the x and o appear in the middle of box so we need to do find the middle of the box
                x,y  = find_box_middle(x, y)
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.pencolor('red')
                turtle.write('O', font=('Times New Roman', 40, 'normal'))
                #update board state
                board[i//3][i%3] = 'O'
                print(board)
                check_win()

                
            else:
                x,y = find_box_middle(x,y)
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.pencolor('blue')
                turtle.write('X', font=('Times New Roman', 40, 'normal'))
                #update board state
                board[i//3][i%3] = 'X'
                print(board)
                check_win()
            round_number += 1
            break
            
                   
draw_board()
turtle.onscreenclick(place_mark)
turtle.done()