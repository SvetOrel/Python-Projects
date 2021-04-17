import random


def display_board(board):

    print(' {} | {} | {}'.format(board[0], board[1], board[2]))
    print('----------')
    print(' {} | {} | {}'.format(board[3], board[4], board[5]))
    print('----------')
    print(' {} | {} | {}'.format(board[6], board[7], board[8]))
    print()


def player_input():
    player = input('Player 1: Do you want to be X or O ? ').upper()
    while player != 'X' and player != 'O':
        print('Your input was Wrong! Please try again!')
        player = input("Player 1: Do you want to be X or O ? ").upper()

    if player == 'X':
        return ('X','O')

    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position - 1] = marker
    return board


def win_check(board,marker):
    if board[0] == marker and board[1] == marker and board[2] == marker or \
       board[3] == marker and board[4] == marker and board[5] == marker or \
       board[6] == marker and board[7] == marker and board[8] == marker or \
       board[0] == marker and board[3] == marker and board[6] == marker or \
       board[1] == marker and board[4] == marker and board[7] == marker or \
       board[2] == marker and board[5] == marker and board[8] == marker or \
       board[0] == marker and board[4] == marker and board[8] == marker or \
       board[2] == marker and board[4] == marker and board[6] == marker:
        return True
    else:
        return False


def choose_first():
    player_num = random.randint(1, 2)
    return player_num


def space_check(board, position):
    return board[position - 1] == ''


def full_board_check(board):
    for i in range(1,9):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = -1
    while position not in range(1,9) or not space_check(board, position):
        position = int(input("Please enter position in range 1 - 9 "))

    return position


def replay():
    play_again = input("Play again? Enter Yes or No")

    return play_again == 'Yes'


print('Welcome to Tic Tac Toe!')
while True:
    play_the_game = 'No'
    board = [''] * 10
    player1,player2 = player_input()

    first_play = choose_first()
    print('Player {} will go first.'.format(first_play))
    play_the_game = input('Are you ready to play? Enter Yes or No.')

    while play_the_game == 'Yes':
        if first_play == 1:
            display_board(board)
            first_play_position = player_choice(board)
            place_marker(board, player1, first_play_position)
            if win_check(board, player1):
                display_board(board)
                print('Congratulations player 1 !You won the game!')
                play_the_game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie Game!!')
                    play_the_game = False
                else:
                    first_play = 2
        else:
            display_board(board)
            second_play_position = player_choice(board)
            place_marker(board, player2, second_play_position)
            if win_check(board, player2):
                display_board(board)
                print('Congratulations player 2 !You won the game!')
                play_the_game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Tie Game!!')
                    play_the_game = False
                else:
                    first_play = 1

    if not replay():
        break

print('--- The End ---')


