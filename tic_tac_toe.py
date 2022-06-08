# This is an assignment for cse210, week 2.
# Tic-Tac-Toe
# Jennifer McNeil

"""Tic-Tac-Toe is played according to the following rules.
1. The game is played on a grid that is three squares by three squares.
2. Player one uses x's. Player two uses o's.
3. Players take turns putting their marks in empty squares.
4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
5. If all nine squares are full and neither player has three in a row, the game ends in a draw."""


def main():
    # Functions go here
    play = True
    player = current_player('')
    board = create_board()
    print(f'Welcome to Tic Tac Toe')
    while play:
        display_board(board)
        player_choice(player, board)
        if check_for_win(board):
            print(f'Congrats Player {player}! You won!')
            display_board(board)
            play = play_again()
            board = create_board()
        elif check_for_draw(board):
            print(f'No one wins! It\'s a draw')
            display_board(board)
            play = play_again()
            board = create_board()
        player = current_player(player)
    print(f'Thanks for playing.')


def current_player(current_player):
    # determine who is the current player
    if current_player == '' or current_player == 'O':
        return 'X'
    else:
        return 'O'


def create_board():
    # This is a list that will go into the game board
    # and hold the values on "x" or "o" from the player inputs
    board = []
    for box in range(9):
        board.append(box + 1)
    return board


def display_board(board):
    # This prints out the game board
    print()
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print()


def check_for_win(board):
    return (  # for horizontal wins
        board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        # for vertical wins
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        # for diangle wins
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6])


def player_choice(player, board):
    # Check to see is the box has been choosen already.
    box = int(input(f"Your turn Player {player}. Choose a box (1-9): "))
    while board[box - 1] == 'X' or board[box - 1] == 'O':
        print(f'That box has already been used.')
        box = int(input(f'Please choose another box: '))
    board[box - 1] = player


def play_again():
    # To see if the play is to be played again.
    play = input('Whould you like to play again: (Y or N): ')
    if play.capitalize() == 'Y':
        return True
    else:
        return False


def check_for_draw(board):
    for box in range(9):
        if board[box] != 'X' and board[box] != 'O':
            return False
    return True


if __name__ == "__main__":
    main()
