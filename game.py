from IPython.display import clear_output
import random

def choose_first():
    number = random.randint(1,2)
    if(number==1):
        print("player 1 goes first")
        return 'player 1'
    else:
        print("player 2 goes first")
        return 'player 2'

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def full_board_check(board):
    for i in range(len(board)):
        if board[i] ==' ': 
            return False   
    return True       


def space_check(board, position):
    return board[position] == ' '

def replay():
    answer = input("want to play again? (y or n)")
    if answer =='y':
        return True
    else:
        return False

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def place_marker(board, marker, position):

    board[position] = marker

def display_board(board):
    
    print('\n'*100)
    
     
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ' '
    while(marker !='X' and marker !='O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

        if(marker=="X"):
            print("Player1 has X") 
            player1=marker
            player2 = 'O'
           
        if(marker=="O"):
            print("Player1 has O")
            player1=marker
            player2 = 'X'
           
    return(player1, player2)


while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
           
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


