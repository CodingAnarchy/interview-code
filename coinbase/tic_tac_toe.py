from random import randint

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def render_board(board):
    print '|'.join(board[0])
    print '-----'
    print '|'.join(board[1])
    print '-----'
    print '|'.join(board[2])


def check_win(board):
    # Horizontal check
    if len(set(board[0])) == 1 and ' ' not in board[0]:
        return board[0][0], True
    elif len(set(board[1])) == 1 and ' ' not in board[1]:
        return board[1][0], True
    elif len(set(board[2])) == 1 and ' ' not in board[2]:
        return board[2][0], True

    columns = zip(board[0], board[1], board[2])
    if len(set(columns[0])) == 1 and ' ' not in columns[0]:
        return columns[0][0], True
    elif len(set(columns[1])) == 1 and ' ' not in columns[1]:
        return columns[1][0], True
    elif len(set(columns[2])) == 1 and ' ' not in columns[2]:
        return columns[2][0], True

    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
       (board[0][2] == board[1][1] and board[1][1] == board[2][0])) and board[1][1] != ' ':
        return board[1][1], True

    return None, False


render_board(board)

win = draw = False
player = 'X'

while not (win or draw):
    move_made = False

    while not move_made:
        row = randint(0, 2)
        col = randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = player
            player = 'O' if player == 'X' else 'X'
            move_made = True

    winner, win = check_win(board)

    if not (' ' in board[0] or ' ' in board[1] or ' ' in board[2]) and not win:
        draw = True

    render_board(board)
    print '\n\n'

if win:
    print "Congrats %s!" % winner
elif draw:
    print "Draw!"
