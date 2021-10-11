#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : SRAVYA GARAGA sgaraga@iu.edu
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys
import json

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        #print (0 <= pos[0] < n  and 0 <= pos[1] < m)
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col,direction):
        moves=((row+1,col,direction+'D'), (row-1,col,direction+'U'), (row,col-1,direction+'l'), (row,col+1,direction+'R'))
        #print(moves)

	# Return only moves that are within the board and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]


# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        #print(pichu_loc)
        fringe = [(pichu_loc,0,'')] # adding '' to store the path
        vis_path = [] #to store all the visited successors.
        while fringe:
                (curr_move, curr_dist,curr_path) = fringe.pop(0)
                vis_path.append(curr_move)
                #print(curr_move, curr_dist)
                for move in moves(house_map, *curr_move,curr_path):
                        if house_map[move[0]][move[1]]=="@":
                                return (curr_dist+1,move[2])  # return the number of moves and path
                        else:
                                if (move[0],move[1]) not in vis_path:
                                        fringe.append(((move[0],move[1]),curr_dist + 1,move[2]))
        return (-1,'')

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Routing in this board:\n" + printable_board(house_map) + "\n")
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + str(solution[1]))

