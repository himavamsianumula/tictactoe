from tictactoe import actions,result,winner,terminal,utility,minimax

X = "X"
O = "O"
EMPTY = None

board= [[EMPTY, EMPTY,EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

board= [[X, X,O],
        [O, X, O],
        [X, EMPTY,EMPTY ]]
print(winner(board))
print(terminal(board))
print(utility(board))
print(minimax(board))
