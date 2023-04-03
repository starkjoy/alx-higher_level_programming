#!/usr/bin/python3
""" N-queen problem possible solution """



import sys

def  print_board(board):
    """ print the board """
    for row in board:
        print(row)

def is_safe(board, row, col, n):
    """ check if its safe to place queen at board """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve(board, col, n):
    """ use backtracking to find all solutions """
    if col == n:
        print_board(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
