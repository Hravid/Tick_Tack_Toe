def print_board():
    print('---------'
          f'\n| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |'
          f'\n| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |'
          f'\n| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |'
          '\n---------')


def is_number(sds):
    try:
        global x, y
        x, y = list(map(int, sds))
        return True
    except ValueError:
        return False


def is_valid(list_map):
    r, t = list(map(int, list_map))
    if r <= 3 and t <= 3:
        return True
    else:
        return False


def is_occupied(list_map):
    r, t = list(map(int, list_map))
    if matrix[r - 1][y - 1] == 'O' or matrix[r - 1][t - 1] == 'X':
        return False
    else:
        return True


def is_won(board):
    list_x = ['X', 'X', 'X']
    list_o = ['O', 'O', 'O']
    for rows in range(3):
        if board[rows] == list_x:
            print('X wins')
            return True
        elif board[rows] == list_o:
            print('O wins')
            return True
    for columns in range(3):
        if board[0:][columns] == list_x:
            print('X wins')
            return True
        elif board[0:][columns] == list_o:
            print('O wins')
            return True
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('X wins')
        return True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print('O wins')
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('X wins')
        return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print('O wins')
        return True
    elif board[0].count(' ') == 0 and board[1].count(' ') == 0 and board[2].count(' ') == 0:
        print('Draw')
        return True


def check_input(dsd):
    while True:
        if not is_number(dsd):
            print("You should enter numbers!")
            break
        if not is_valid(user_input):
            print('Coordinates should be from 1 to 3!')
            break
        if not is_occupied(user_input):
            print('This cell is occupied! Choose another one!')
            break
        else:
            return True


i = 0
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print_board()


while True:
    user_input = input('Enter coordinates: ').split()
    if not check_input(user_input):
        continue
    else:
        matrix[x-1].pop(y-1)
        if i % 2 == 0:
            matrix[x-1].insert(y-1, 'X')
        if i % 2 == 1:
            matrix[x-1].insert(y-1, 'O')
        print_board()
        i += 1
        if is_won(matrix):
            break
