import numpy as np
import sys

import matplotlib.pyplot as plt

sys.setrecursionlimit(3000)

# Creates the list of arrays

def create_arrays(N):  # Creates a list of arrays corresponding to layers of spiral
    arrays = []  # Empty list to store arrays
    for i in range(1, 2 * N + 1, 2):
        if i > 1:
            # Creates the subsequent arrays with (2N + 1)^2 - (2N-1)^2 elements, i.e 8,16,24, etc..
            array_start = (i - 2) ** 2 + 1
            array_end = i ** 2 + 1
        else:
            # Creates the first array with 1 element
            array_start = 1
            array_end = 2
        array = np.arange(array_start, array_end)
        arrays.append(array)  # Adds array to list
    return arrays

# Layers the arrays around each other to form the spiral


def create_spiral(array_list):
    last_entry = array_list[-1][-1] # Identify the largest number in the spiral
    grid_size = int(np.sqrt(last_entry)) # Determine grid size
    grid = np.zeros(shape=(grid_size, grid_size)) # Initialize grid
    for j in range(len(array_list)):
        if j > 0:
            # Sets bottom-right diagonal elements
            grid[grid_size // 2 + j][grid_size // 2 + j] = array_list[j - 1][-1] + np.sqrt(array_list[j][-1]) - 1
            for i in range(1, int(np.sqrt(array_list[j][-1]))):
                # Sets upper triangle of elements including top-left diagonal
                grid[grid_size // 2 - j][grid_size // 2 + j - i] = array_list[j][-1] - i
                # Sets lower triangle of elements excluding the diagonals
                grid[grid_size // 2 + j][grid_size // 2 + j - i] = array_list[j - 1][-1] + np.sqrt(
                    array_list[j][-1]) - 1 + i
                # Sets right triangle of elements excluding the diagonals
                grid[grid_size // 2 + j - i][grid_size // 2 + j] = array_list[j - 1][-1] + np.sqrt(
                    array_list[j][-1]) - 1 - i
                # Sets left triangle of elements excluding the diagonals
                grid[grid_size // 2 - j + i][grid_size // 2 - j] = array_list[j][-1] - int(
                    np.sqrt(array_list[j][-1])) - i + 1
        # Sets diagonal entries from bottom-left to top-right
        grid[grid_size // 2 - j][grid_size // 2 + j] = array_list[j][-1]
    return grid

# Initialize the arrays and the spiral, 81 x 81 is a sufficient size, but we can use a larger grid if we want to


arrays = create_arrays(40)
spiral = create_spiral(arrays)

# Solve the problem


def knight_walk(path, visited_vals=[], visited_positions=[]):
    # Places knight at one if it is the first run of the function
    if not visited_vals:
        position = (len(path) // 2, len(path) // 2)
        visited_positions.append(position)
        visited_vals.append(path[position])
    # Places knight at the last position it visited if it is not the first run of the function
    else:
        position = visited_positions[-1]
    # Calculates the eight possible moves for the knight
    possible_moves = [(position[0] + 2, position[1] + 1), (position[0] + 2, position[1] - 1),
                      (position[0] - 2, position[1] + 1), (position[0] - 2, position[1] - 1),
                      (position[0] + 1, position[1] + 2), (position[0] + 1, position[1] - 2),
                      (position[0] - 1, position[1] + 2), (position[0] - 1, position[1] - 2)]
    # Calculates the number associated with each of the moves
    move_values = [path[i] for i in possible_moves]
    # Removes any previously visited positions from the set of allowed moves
    allowed_moves = list(set(move_values) - set(visited_vals))
    # If there are allowed moves, choose the one associated with the smallest number
    if len(allowed_moves) != 0:
        new_val = np.amin(allowed_moves) # Determine smallest number
        position = (np.where(path == new_val)[0][0], np.where(path == new_val)[1][0]) # Find indices associated with lowest number
        visited_positions.append(position) # Add position to list of visited positions
        visited_vals.append(new_val)
        knight_walk(path, visited_vals, visited_positions) # Repeat the process
    return visited_vals, visited_positions


# Plotting the solution

visited, pos = knight_walk(spiral)
x_pos = [item[0] for item in pos] # List of x values of positions
y_pos = [item[1] for item in pos] # List of y values of positions
# 5 Plots to add some color and obtain a nicer graph
plt.plot(x_pos[:300],y_pos[:300])
plt.plot(x_pos[300:700],y_pos[300:700],color='green')
plt.plot(x_pos[700:1200],y_pos[700:1200],color='yellow')
plt.plot(x_pos[1200:1800],y_pos[1200:1800],color='orange')
plt.plot(x_pos[1800:],y_pos[1800:],color='crimson')
# Save and show figure
plt.savefig('Knight walk.png',dpi=500)
plt.show()