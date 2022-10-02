def create_field():
    n = 0
    player_mark = ''
    comp_mark = ''
    while n < 3:
        print('Enter field size(number from 3 to +inf):', end=" ")
        n = int(input())
    field = [['.'] * n for i in range(n)]
    draw_field(field)
    while player_mark != "X" and player_mark != "O":
        print('Do you want to be X or O?', end=" ")
        player_mark = input()
    if player_mark == "X":
        comp_mark = "O"
    else:
        comp_mark = "X"
    print('X will go first\n')
    return field, player_mark, comp_mark


def draw_field(field):
    for i in range(0, len(field)):
        if i == 0:
            print(' ', end=' ')
            for k in range(len(field)):
                print(k + 1, end=' ')
            print()
        for i2 in range(0, len(field[i])):
            if i2 == 0:
                print(i + 1, end=' ')
            print(field[i][i2], end=' ')
        print()
    # print('\n')


def player_turn(field, player_mark):
    a = 0
    b = 0
    while a == 0 and b == 0:
        while a < 1 or a > len(field):
            print('Enter the cell number horizontally as a number from 1 to ', len(field), ':', sep='',
                  end=" ")
            a = int(input())
            if a < 1 or a > len(field):
                print("Try again")
        while b < 1 or b > len(field):
            print('Enter the cell number vertically as a number from 1 to ', len(field), ':', sep='',
                  end=" ")
            b = int(input())
            if b < 1 or b > len(field):
                print("Try again")
        if field[a - 1][b - 1] == '.':
            field[a - 1][b - 1] = player_mark
            draw_field(field)
        else:
            print("This cell is not empty. Try again")
            a = 0
            b = 0


choice = []


def win_check(field, a, b, moves_left):
    n = len(field)
    if n > 5:
        n = 5
    a -= 1
    b -= 1
    to_check = [[], [], [], []]
    c = max(0, b - (n - 1))
    d = min(len(field) - 1, b + (n - 1))
    for i in range(c, d + 1):
        to_check[0].append(field[a][i])
    c = max(0, a - (n - 1))
    d = min(len(field) - 1, a + (n - 1))
    for i in range(c, d + 1):
        to_check[1].append(field[i][b])
    c = min(a, b, n - 1)
    i = a - c
    j = b - c
    k = 0
    while i + k < len(field) and j + k < len(field) and k <= (n - 1) * 2:
        to_check[2].append(field[i + k][j + k])
        k += 1
    c = min(a, len(field) - 1 - b, n - 1)
    i = a - c
    j = b + c
    k = 0
    while i + k < len(field) and j - k >= 0 and k <= (n - 1) * 2:
        to_check[3].append(field[i + k][j - k])
        k += 1
    for raw in to_check:
        cnt = 1
        for j in range(1, len(raw)):
            if raw[j] == raw[j - 1] and raw[j] != '.':
                cnt += 1
            else:
                cnt = 1
            if cnt == n:
                return 10
    if moves_left == 0:
        return 0
    return None


def minimax(field, player_mark, curr_mark, moves_left, x, y, depth):
    # if depth > 5:
    #   return 0
    global choice
    if x != -1 and y != -1:
        wc = win_check(field, x + 1, y + 1, moves_left)
        if wc == 10 and curr_mark != player_mark:
            return 10
        if wc == 10 and curr_mark == player_mark:
            return -10
        if wc == 0:
            return 0

    available_moves = []
    scores = []
    moves = []

    if x != -1 and y != -1:
        if curr_mark == 'X':
            curr_mark = 'O'
        else:
            curr_mark = 'X'

    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == '.':
                available_moves.append([i, j])
    for move in available_moves:
        field[move[0]][move[1]] = curr_mark
        scores.append(minimax(field, player_mark, curr_mark, moves_left - 1, move[0], move[1], depth + 1))
        moves.append(move)
        field[move[0]][move[1]] = '.'

    if curr_mark != player_mark:
        ind_of_max = -1
        max_score = -20
        for i in range(len(scores)):
            if scores[i] > max_score:
                ind_of_max = i
                max_score = scores[i]
        choice = [moves[ind_of_max][0], moves[ind_of_max][1]]
        return scores[ind_of_max]

    else:
        ind_of_min = -1
        min_score = 20
        for i in range(len(scores)):
            if scores[i] < min_score:
                ind_of_min = i
                min_score = scores[i]
        choice = [moves[ind_of_min][0], moves[ind_of_min][1]]
        return scores[ind_of_min]


def game(field, player_mark, comp_mark):
    moves_left = len(field) * len(field)
    if player_mark == 'X':
        player_turn(field, player_mark)
        moves_left -= 1
    while True:
        minimax(field, player_mark, comp_mark, moves_left, -1, -1, 0)
        moves_left -= 1
        global choice
        field[choice[0]][choice[1]] = comp_mark
        draw_field(field)
        if win_check(field, choice[0] + 1, choice[1] + 1, moves_left) == 10:
            print('You lose!')
            break
        if moves_left == 0:
            print('It\'s a  draw!')
            break

        player_turn(field, player_mark)
        moves_left -= 1
        if moves_left == 0:
            print('It\'s a  draw!')
            break


def start():
    field, player_mark, comp_mark = create_field()
    game(field, player_mark, comp_mark)


start()
