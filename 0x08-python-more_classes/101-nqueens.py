#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys
""" Define a function to check if it's
    safe to place a queen at a specific position """

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

    """Define a function to print the board"""
    def print_board(board):
        for row in board:
            print(" ".join(map(str, row)))
        print()

    """Define a function to solve the N-queens problem"""
    def solve_nqueens(N):
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    
    """Initialize a 2D board with zeros"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    """Define a recursive utility function to find all solutions"""
    def solve_util(col):
        if col >= N:
            solutions.append([row[:] for row in board])
            return
        
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve_util(col + 1)
                board[i][col] = 0
    
    """Start the recursive process"""
    solve_util(0)

    """Print all solutions"""
    for solution in solutions:
        print_board(solution)

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Call the solve_nqueens function with the provided N"""
    solve_nqueens(N)

