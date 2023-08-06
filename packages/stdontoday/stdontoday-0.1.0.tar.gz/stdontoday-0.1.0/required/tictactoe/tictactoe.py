"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count, o_count = 0, 0
    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            elif j == O:
                o_count += 1
    if x_count == o_count:
        return X
    else:
        return O
    # """
    # Returns player who has the next turn on a board.
    # """


def actions(board):
    all_pos = list()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                all_pos.append((i, j))
    return all_pos
    # """
    # Returns set of all possible actions (i, j) available on the board.
    # """


def result(board, action):
    pos_x, pos_y = action
    new_board = copy.deepcopy(board)
    if pos_x < 0 or pos_x > 2 or pos_y > 2 or pos_y < 0:
        raise ValueError
    if player(board) == X:
        new_board[pos_x][pos_y] = X
    else:
        new_board[pos_x][pos_y] = O
    return new_board
    # """
    # Returns the board that results from making move (i, j) on the board.
    # """


def winner(board):
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    return None
    # """
    # Returns the winner of the game, if there is one.
    # """


def terminal(board):
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return True
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return True
    emp_count = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                emp_count += 1
    if emp_count == 0:
        return True
    return False
    # """
    # Returns True if game is over, False otherwise.
    # """
    # raise NotImplementedError


def utility(board):
    if winner(board) == O:
        return -1
    elif winner(board) == X:
        return 1
    else:
        return 0
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move


