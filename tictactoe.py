"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np

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
    """
    Returns player who has the next turn on a board.
    """
    x=0
    o=0
    for i in board:
        for j in i:
            if j=="X":
                x+=1
            if j=="O":
                o+=1
    if x==o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos_act=set()
    for row,i in enumerate(board):
        for col,j in enumerate(i):
            if j==EMPTY:
                pos_act.add((row,col))
    return pos_act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i,j)=action

    if i>2 or j>2 or i<0 or j<0:
        raise NotImplementedError
    else:
        brd=copy.deepcopy(board)
        plyr=player(brd)
        brd[i][j]=plyr
    return brd

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking rows
    for r,i in enumerate(board):
        a=board[r][0]
        f=0
        for c, j in enumerate(i):
            if a!=board[r][c] or a==None:
                f=1
                break
        if f==0:
            return a

    #checking columns
    for r,i in enumerate(board):
        a=board[0][r]
        f=0
        for c, j in enumerate(i):
            if a!=board[c][r] or a==None:
                f=1
                break
        if f==0:
            return a

    #checking diagnols
    if board[0][0]==board[1][1] and board[2][2]==board[1][1] and board[1][1]!=None:
        return board[0][0]

    if board[2][0]==board[1][1] and board[0][2]==board[1][1] and board[1][1]!=None:
        return board[1][1]

    return None

def isfilled(board):
    count=0
    for r,i in enumerate(board):
        for c,j in enumerate(i):
            if j==EMPTY:
                count+=1

    if count==0:
        return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None or isfilled(board):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w=winner(board)
    if w==X:
        return 1
    elif w==O:
        return -1
    elif isfilled(board):
        return 0

def max_val(board):
    if terminal(board):
        return (utility(board),(None,None))
    v=[]
    a=list(actions(board))
    for action in a:
        temp=min_val(result(board,action))
        v.append(temp[0])
    ind=np.argmax(v)
    return (v[ind],a[ind])

def min_val(board):
    if terminal(board):
        return (utility(board),(None,None))
    v=[]
    a=list(actions(board))
    for action in a:
        temp=max_val(result(board,action))
        v.append(temp[0])
    ind=np.argmin(v)
    return (v[ind],a[ind])

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p=player(board)
    if p==X:
        return (max_val(board))[1]
    else:
        return (min_val(board))[1]
