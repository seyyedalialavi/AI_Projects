board = []
for i in range(3):
    board.append([' ', ' ', ' '])


def draw_board():
    for i in range(0, 3):
        for j in range(0, 3):
            print('| ' + board[i][j], end=" ")
        print('|')
    print()

def check_win():
    if board[0][0] == board[1][1] == board[2][2] != ' ': return board[1][1]
    if board[2][0] == board[1][1] == board[0][2] != ' ': return board[1][1]
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ': return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ': return board[0][i]
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ': return "Not_End"
    return 'Draw'


def alphabeta(alpha, beta, maximizingPlayer):
    px, py, qx, qy = None, None, None, None
    result = check_win()

    p = 0
    if result == 'X': p = -1
    if result == 'O': p = 1
    if result != 'Not_End': return p, 0, 0

    if maximizingPlayer:
        firstmax = -2
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    (newvalue, min_i, min_j) = alphabeta(alpha, beta, False)
                    if newvalue > firstmax:
                        firstmax = newvalue
                        px = i
                        py = j
                    alpha = max(alpha, newvalue)
                    board[i][j] = ' '
                    if beta <= alpha:
                        break

        return firstmax, px, py
    else:
        firstmin = 2
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    (newvalue, max_i, max_j) = alphabeta(alpha, beta, True)
                    if newvalue < firstmin:
                        firstmin = newvalue
                        qx = i
                        qy = j
                    beta = min(beta, newvalue)
                    board[i][j] = ' '
                    if beta <= alpha:
                        break

        return firstmin, qx, qy


def check_end(winner):
    if winner == 'X':
        print('Player won')
    if winner == 'O':
        print('Computer won')
    if winner == 'Draw':
        print("Draw")
    if winner != 'Not_End':
        input()
        exit(0)


computer = 1
player = 2
choose = 0

while choose != 2 and choose != 1:
    print("Who plays first?\n1- Computer\n2- Player")
    choose = int(input())

turn = choose





while True:
    draw_board()
    winner = check_win()
    check_end(winner)
    if turn == computer:
        m, x, y = alphabeta(-2, 2, True)
        board[x][y] = 'O'
        turn = player
    else:
        y,x = -1,-1
        while x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != ' ':
            print("Enter x and y:")
            y,x = map(int,input().split(" "))
        board[x][y] = 'X'
        turn = computer

