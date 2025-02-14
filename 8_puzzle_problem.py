# Solving the 8 Puzzle Problem using Breadth First Search (BFS)

import numpy as np



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

