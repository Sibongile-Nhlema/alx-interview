#!/usr/bin/python3
'''
Module that handles the implementation of the N queens project

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
'''
import sys
from typing import List, Tuple


def nqueens(N: int) -> None:
    '''
    Function to solve the N Queens puzzle
    '''
    if N < 4:
        '''
        N must be an integer greater or equal to 4
        '''
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0] * N for _ in range(N)]
    solutions: List[List[List[int, int]]] = []
    solve_n_queens(board, 0, N, solutions)
    
    for solution in solutions:
        print(solution)


def solve_n_queens(board: List[List[int]], col: int, N: int, solutions: List[List[Tuple[int, int]]]) -> bool:
    '''
    Recursive function to solve N Queens problem
    '''
    if col >= N:
        # if all queens are placed then add the solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append((i, j))
        solutions.append(solution)
        return True
    
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            
            # Recur to place rest of the queens
            solve_n_queens(board, col + 1, N, solutions)
            
            # placing queen at board[i][col] doesn't lead to a solution
            board[i][col] = 0
    
    return False


def is_safe(board: List[List[int]], row: int, col: int) -> bool:
    '''
    Check whether it's safe to place a queen at board[row][col]
    '''
    # 1. Check this row on left hand side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # 2. Check upper diagonal on left hand side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # 3. Check lower diagonal on left hand side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        '''
         Wrong number of arguments called
        '''
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        '''
        If N is not an integer
        '''
        print("N must be a number")
        sys.exit(1)