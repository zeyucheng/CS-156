# -----------------------------------------------------------------------------
# Name:     adversarial_search
# Purpose:  Homework 5 - Implement adversarial search algorithms
#
# Author:
#
# -----------------------------------------------------------------------------
"""
Adversarial search algorithms implementation

Your task for homework 5 is to implement:
1.  minimax
2.  alphabeta
3.  abdl (alpha beta depth limited)
"""
import random
import sys


def rand(game_state):
    """
    Generate a random move.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the random move
    """
    done = False
    while not done:
        row = random.randint(0, game_state.size - 1)
        col = random.randint(0, game_state.size - 1)
        if game_state.available(row,col):
            done = True
    return row, col


def minimax(game_state):
    """
    Find the best move for our AI agent by applying the minimax algorithm
    (searching the entire tree from the current game state)
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    return max(game_state.possible_moves(), key=lambda node: value(game_state.successor(node, 'AI'), 'user'))

def value(game_state, player):
    """
    Calculate the minimax value for any state under the given agent's control
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    if game_state.is_win('AI'):
        return 1
    if game_state.is_win('user'):
        return -1
    if game_state.is_tie():
        return 0
    # If the agent is MAX return max-value
    if player is 'AI':
        return max_value(game_state)
    # If the agent is MIN return min-value
    return min_value(game_state)


def max_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    v = -sys.maxsize
    for move in game_state.possible_moves():
        v1 = value(game_state.successor(move, 'AI'), 'user') # not good
        tup = [v, v1]
        # print("TUP", tup)
        v = max(tup)
        # print('MAX: ', v)
    return v

def min_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    v = sys.maxsize
    for move in game_state.possible_moves():
        v1 = value(game_state.successor(move, 'user'), 'AI') # little gud
        tup = [v, v1]
        # print("TUP", tup)
        v = min(tup)
        # print('MIN: ', v)
    return v


def alphabeta(game_state):
    """
    Find the best move for our AI agent by applying the minimax algorithm
    with alpha beta pruning.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below\
    a = -sys.maxsize
    b = sys.maxsize
    return max(game_state.possible_moves(), key=lambda node: ab_value(game_state.successor(node, 'AI'), 'user', a, b))


def ab_value(game_state, player, alpha, beta):
    """
    Calculate the minimax value for any state under the given agent's control
    using alpha beta pruning
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    if game_state.is_win('AI'):
        return 1
    if game_state.is_win('user'):
        return -1
    if game_state.is_tie():
        return 0
    # If the agent is MAX return max-value
    if player is 'AI':
        return abmax_value(game_state, alpha, beta)
    # If the agent is MIN return min-value
    return abmin_value(game_state, alpha, beta)


def abmax_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    a = alpha
    v = -sys.maxsize
    for move in game_state.possible_moves():
        v = max([v, ab_value(game_state.successor(move, 'AI'), 'user', a, beta)])
        if v >= beta:
            return v
        a = max(a, v)
    return v


def abmin_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    b = beta
    v = sys.maxsize
    for move in game_state.possible_moves():
        v = min([v, ab_value(game_state.successor(move, 'user'), 'AI', alpha, b)])
        if v <= alpha:
            return v
        b = min([b, v])
    return v


def abdl(game_state, depth):
    """
    Find the best move for our AI agent by limiting the alpha beta search to
    the given depth and using the evaluation function game_state.eval()
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    a = -sys.maxsize
    b = sys.maxsize
    return max(game_state.possible_moves(), key=lambda node: abdl_value(game_state.successor(node, 'AI'), 'user', a, b, depth))



def abdl_value(game_state, player, alpha, beta, depth):
    """
    Calculate the utility for any state under the given agent's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) utility of that state
    """
    # Enter your code here and remove the pass statement below
    if player == 'AI' and game_state.is_win('AI'):
        return 1
    if player == 'user' and game_state.is_win('user'):
        return -1
    if game_state.is_tie():
        return 0
    if depth == 0:
        return game_state.eval()
    # If the agent is MAX return max-value
    if player is 'AI':
        return abdlmax_value(game_state, alpha, beta, depth)
    # If the agent is MIN return min-value
    return abdlmin_value(game_state, alpha, beta, depth)


def abdlmax_value(game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Max's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    a = alpha
    v = -sys.maxsize
    for move in game_state.possible_moves():
        v = max([v, abdl_value(game_state.successor(move, 'AI'), 'user', a, beta, depth -1)])
        if v >= beta:
            return v
        a = max(a, v)
    return v


def abdlmin_value( game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Min's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    b = beta
    v = sys.maxsize
    for move in game_state.possible_moves():
        v = min([v, abdl_value(game_state.successor(move, 'user'), 'AI', alpha, b, depth -1 )])
        if v <= alpha:
            return v
        b = min([b, v])
    return v

