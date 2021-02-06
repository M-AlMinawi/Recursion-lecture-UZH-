# We only need numpy for this problem
import numpy as np
import sys

# Change maximum recursion limit from 1000 to 3000 as a precaution
sys.setrecursionlimit(3000)

# Initialize our representation of a chess board
matrix = np.zeros((8,8))

# Recursive function to keep adding kings to a chess board

# Three inputs, the board and the indices to determine which empty square we pick


def add_king(board,N=0,M=0):
    # Find open slots by finding the indices of all 0 entries in the matrix
    open_spot = np.where(board == 0)
    # Run recursively as long as there is one or more 0 entries in the matrix (Uses zero = False, non-zero = True)
    if not board.all():
        # Choose row and column by varying N and M respectively
        open_x = open_spot[0][N*8]
        open_y = open_spot[1][M]
        # Place a king at the chosen square
        board[open_x][open_y] = 1
        # Calculate all potentially attacked positions by the king
        attack_spots = [(open_x+1,open_y+1),(open_x-1,open_y+1),(open_x+1,open_y-1),(open_x-1,open_y-1),
                        (open_x-1,open_y),(open_x,open_y-1),(open_x+1,open_y),(open_x,open_y+1)]
        # If the squares are within the board, we set their matrix entry to -1
        for spot in attack_spots:
            if all(len(board)>i>=0 for i in spot):
                board[spot] = -1
        # Run the function again, this time we set N and M to 0, since varying them once is enough
        return add_king(board)
    else:
        # Once all the squares either house a king or are attacked by one, we return the board
        return board

# Recursive function to find all possible solutions to the problem


def solver(board,solutions=[],N=0,M=0):
    # Run recursive calls as long as we have not tried placing the first king at every square on the board
    if N != 7 or M != 7:
        # Calculate the solution using our previous recursive function
        pos_sol = add_king(board,N,M)
        # Check that it is a valid solution by noting that there are 16 kings and 48 attacked squares
        if sum(pos_sol.flatten())==-32:
            # Do not accept a solution if it has already been found earlier
            if any((i==pos_sol).all() for i in solutions):
                pass
            # If the solution is new, add it to the list of solutions
            else:
                solutions.append(pos_sol)
        # Reset the board for the next run
        board = np.zeros((8, 8))
        # Run the function again, moving first through each column, then each row
        return solver(board,solutions,N+M//7,(M+1)%8)
    else:
        # Once we have tried every square once, return the list of solutions
        return solutions
# Run the program


answers = solver(matrix)
