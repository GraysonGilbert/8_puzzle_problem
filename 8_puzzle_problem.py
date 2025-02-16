"""Solving the 8 Puzzle Problem using the Breadth First Search (BFS) algorithm"""

import numpy as np
from collections import deque

"""This class handles all the actions related to determining and modifying the board (node) state for the puzzle."""
class PuzzleState:
    def __init__(self, node_state_i, node_index_i, parent_node_index_i = None):
        self.node_state_i = np.array(node_state_i)
        self.node_index_i = node_index_i
        self.parent_node_index_i = parent_node_index_i

        self.board = self.arrange_board()   # Arrange board at initialization
        self.possible_moves = self.get_possible_moves() # Calculate possible moves at initialization
        self.zero_location = self.find_zero()   # Find zero location at initialization
    
    """Allows for comparing puzzle states to determine if they are equal to one another"""
    def __eq__(self, other): 
        return np.array_equal(self.node_state_i, other.node_state_i)

    """Creates a hash value of the puzzle state based on its node index. Required to efficiently track visited states.""" 
    def __hash__(self): 
        return hash(tuple(self.node_state_i.flatten()))

    """Rearranges board state into 3x3 column-based grid."""
    def arrange_board(self): 
        return self.node_state_i.reshape((3,3), order="F")
    
    """Find and return 0 location of the current board (node) state."""
    def find_zero(self):
        row, col = np.where(self.board == 0)
        return row[0], col[0]
    
    """Find all valild moves given the current board (node) state."""
    def get_possible_moves(self):

        row, col = self.find_zero()
        moves = {}

        move_options = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        
        for move, (row_move, col_move) in move_options.items(): # Checks that a move is valid, meaning it stays within the bounds of the 3x3 puzzle
            new_row, new_col = row + row_move, col + col_move

            if 0 <= new_row < 3 and  0 <= new_col < 3:
                moves[move] = (row_move, col_move)

        return moves

    """Swap the tiles for two specified indexes"""
    def swap_tiles(self, current_row, current_col, new_row, new_col):
        new_state = self.node_state_i.copy()
        
        index_1 = current_col * 3 + current_row
        index_2 = new_col * 3 + new_row

        new_state[index_1], new_state[index_2] = new_state[index_2], new_state[index_1]

        return new_state
    
    """Moves the 0 tile up 1 row."""
    def action_move_up(self): 
        if "up" in self.possible_moves:
            row_change, col_change = self.possible_moves["up"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            return self.swap_tiles(current_row, current_col, new_row, new_col) 
        
        return None

    """Moves the 0 tile down 1 row."""
    def action_move_down(self):
        if "down" in self.possible_moves:
            row_change, col_change = self.possible_moves["down"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            return self.swap_tiles(current_row, current_col, new_row, new_col) 

        return None
    
    """Moves the 0 tile left 1 column."""
    def action_move_left(self):
        if "left" in self.possible_moves:
            row_change, col_change = self.possible_moves["left"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            return self.swap_tiles(current_row, current_col, new_row, new_col) 

        return None
    
    """Moves the 0 tile right 1 column"""
    def action_move_right(self):
        if "right" in self.possible_moves:
            row_change, col_change = self.possible_moves["right"]
            current_row, current_col = self.zero_location
            new_row, new_col = current_row + row_change, current_col + col_change

            return self.swap_tiles(current_row, current_col, new_row, new_col) 

        return None
    
"""This class handles all the actions related to solving the puzzle. Including the BFS search algorithm."""
class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

        self.visited_states = {}
        self.queue = deque([self.initial_state])

        self.node_counter = 1

        self.node_path = []
        self.node_info = []
        self.nodes_explored = []
    
    """Performs a Breadth First Search (BFS) algorithm with backtracking to find the optimal path from inital puzzle state to goal state."""
    def solve_puzzle_bfs(self):
        while self.queue:
            current_state = self.queue.popleft()

            self.nodes_explored.append(current_state.node_state_i.flatten())
            self.node_info.append([current_state.node_index_i, current_state.parent_node_index_i, current_state.node_state_i.flatten()])

            if np.array_equal(current_state.node_state_i, self.goal_state):
                
                print("Found goal state!")
                self.generate_path(current_state)
                self.write_files()

                return self.node_path
            
            self.visited_states[tuple(current_state.node_state_i.flatten())] = current_state

            for move in current_state.possible_moves.keys():
                
                new_board_state = None

                if move == "up":
                    new_board_state = current_state.action_move_up()
                elif move == "down":
                    new_board_state = current_state.action_move_down()
                elif move == "left":
                    new_board_state = current_state.action_move_left()
                elif move == "right":
                    new_board_state = current_state.action_move_right()
                
                if new_board_state is not None:
                    new_state = PuzzleState(new_board_state, self.node_counter, current_state.node_index_i)

                    if tuple(new_state.node_state_i.flatten()) not in self.visited_states:
                        new_state = PuzzleState(new_board_state, self.node_counter, current_state.node_index_i)
                        self.node_counter += 1
                        self.queue.append(new_state) 
                        self.visited_states[tuple(new_state.node_state_i.flatten())] = new_state
            
        print('Exited loop, this configuration is not solvable!')

    """Generates a path using backtracking from the goal state back to the initial puzzle state."""
    def generate_path(self, goal_state):
        current_state = goal_state
        path = []

        while current_state is not None:

            print(f"Current State ID: {id(current_state)}, Node Index: {current_state.node_index_i}")  # Debug print
            path.append(current_state)

            if current_state.node_index_i == 0:
                break

            current_state = self.get_parent_state(current_state)


            
        self.node_path = path[::-1] # Sets the node path equal to the reverse of path

    """Determines the parent node state to move through graph."""
    def get_parent_state(self, state):

        if state.parent_node_index_i is None:
            return None
        
        for s in self.visited_states.values():
            if s.node_index_i == state.parent_node_index_i:
                return s
        
        return None
 
    
    """Writes the 3 output files from the generated lists."""
    def write_files(self):
        with open("Nodes.txt", "w") as nodes_file:
            for state in self.nodes_explored:
                nodes_file.write(" ".join(map(str, state)) + "\n")
        
        with open("NodesInfo.txt", "w") as nodes_info_file:
            for node_info in self.node_info:
                node_state = " ".join(map(str, node_info[2]))
                nodes_info_file.write(f"{node_info[0]}\t{node_info[1]}\t{node_state}\n")

        with open("nodePath.txt", "w") as node_path_file:
            for state in self.node_path:
                node_path_file.write(" ".join(map(str, state.node_state_i.flatten())) + "\n")
        


"""Test Cases:"""

#node_state = [1, 4, 7, 2, 5, 8, 3, 6, 0] # Solvable, initial state = goal state
#node_state = [2, 8, 3, 1, 6, 4, 7, 0, 5] # Solvable
#node_state = [8, 2, 3, 1, 6, 4, 7, 0, 5] # Not Solvable
node_state = [1, 4, 7, 0, 2, 8, 3, 5, 6] # Solvable


goal_state = [1, 4, 7, 2, 5, 8, 3, 6, 0]

"""Creating instances of the PuzzleState and PuzzleSolver classes"""
test = PuzzleState(node_state_i=node_state, node_index_i=0, parent_node_index_i=0)
path_test = PuzzleSolver(test, goal_state)


"""Solving the 8-Puzzle Problem"""
path_test.solve_puzzle_bfs()