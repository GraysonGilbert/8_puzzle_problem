# Solving the 8 Puzzle Problem using Breadth First Search (BFS)

import numpy as np
from collections import deque


"""Step 2: Given the state of the current node, calculate the location of the blank tile [0] in
the 3x3 matrix and returns the output as a pair (i,j), where 0 <= i <= 2 and 0 <= j <= 2"""




"""Step 3: write 4 subfunctions to move the blank tile in 4 different directions."""

# Move Left

# Move right

# Move Up

# Move Down

"""Step 4: Append all the possible new nodes in a list. Check to see if the new node you explored
has been visited already and do not repeat that action for that node."""



"""Step 5: Write a subfunction (generate_path) that uses backtracking to find the path between the inital and final node"""


""" Code Outputs:
    -   Nodes.txt - All the explored states should be present as a list.
    NodesInfo.txt - Information about all the nodes explored (1st col. Node Index, 2nd col. Parent Node Index, 3rd col. Node)
    nodePath.txt - the solution to the puzzle as solved by your code. the elements are being stored column-wise i.e. for this
                    state 1, 4, 7, 2, 5, 8, 3, 6, 0 the eight puzzle state is
                    
                    1 2 3
                    4 5 6
                    7 8 0   

                    The order of states should be from start node to goal node"""

class PuzzleState:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i = None):
        self.node_state_i = np.array(node_state_i)
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i

        self.board = self.arrange_board()
        self.possible_moves = self.get_possible_moves()
        self.zero_location = self.find_zero()

        print(self.board)
    
    def __eq__(self, other):
        return np.array_equal(self.node_state_i, other.node_state_i)
        
    def __hash__(self):
        return hash(tuple(self.node_state_i.flatten()))

    def arrange_board(self): # Rearranges board state into 3x3 column-based grid
        return self.node_state_i.reshape((3,3), order="F")
    

    def find_zero(self): # Find and return 0 location in the current node state
        row, col = np.where(self.board == 0)

        return row[0], col[0]
    
    def get_possible_moves(self): # Find all valild moves given the current node state

        row, col = self.find_zero()
        moves = {}

        move_options = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        
        for move, (row_move, col_move) in move_options.items():
            new_row, new_col = row + row_move, col + col_move

            if 0 <= new_row < 3 and  0 <= new_col < 3:
                moves[move] = (row_move, col_move)

        return moves

    def swap_tiles(self, current_row, current_col, new_row, new_col):
        new_state = self.node_state_i.copy()
        
        index_1 = current_col * 3 + current_row
        index_2 = new_col * 3 + new_row

        new_state[index_1], new_state[index_2] = new_state[index_2], new_state[index_1]
        #print(new_state)
        return new_state

    def action_move_up(self): # Moves 0 tile up if possible
        if "up" in self.possible_moves:
            row_change, col_change = self.possible_moves["up"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            new_puzzle_state = self.swap_tiles(current_row, current_col, new_row, new_col) 
        #print(new_puzzle_state)
        
        return PuzzleState(new_puzzle_state, self.node_index_i + 1, self.node_index_i)

    def action_move_down(self): # Moves 0 tile down if possible
        if "down" in self.possible_moves:
            row_change, col_change = self.possible_moves["down"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            new_puzzle_state = self.swap_tiles(current_row, current_col, new_row, new_col) 

        return PuzzleState(new_puzzle_state, self.node_index_i + 1, self.node_index_i)
    
    def action_move_left(self): # Moves 0 tile left if possible
        if "left" in self.possible_moves:
            row_change, col_change = self.possible_moves["left"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            new_puzzle_state = self.swap_tiles(current_row, current_col, new_row, new_col) 

        return PuzzleState(new_puzzle_state, self.node_index_i + 1, self.node_index_i)
    

    def action_move_right(self): # Moves 0 tile right if possible
        if "right" in self.possible_moves:
            row_change, col_change = self.possible_moves["right"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            new_puzzle_state = self.swap_tiles(current_row, current_col, new_row, new_col) 

        return PuzzleState(new_puzzle_state, self.node_index_i + 1, self.node_index_i)
    

"""
class PuzzleSolver:
    def __init__():
        pass
    def action_move_up(self):
        pass

class PuzzleUtils:
    def __init__(self):
        pass

"""

#node_state = [1, 4, 7, 2, 5, 8, 3, 6, 0]
node_state = [7, 6, 1, 5, 0, 4, 8, 3, 2]
index = 0

test = PuzzleState(node_state_i=node_state, node_index_i= index, parent_node_index_i=0)

#print(node_state)
#test.arrange_board()
#test.find_zero()
#test.get_possible_moves()
#test.swap_tiles(1,1,0,1)
test.action_move_right()