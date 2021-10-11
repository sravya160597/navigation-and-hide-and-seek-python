#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : SRAVYA GARAGA sgaraga@iu.edu
#
# Based on skeleton code in CSCI B551, Spring 2021

import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Count total # of pichus on board
def count_pichus(board):
    return sum([row.count('p') for row in board])


# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col):
    return board[0:row] + [board[row][0:col] + ['p', ] + board[row][col + 1:]] + board[row + 1:]


# Get list of successors of given board state
def successors(board):
    return [add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0, len(board[0])) if board[r][c] == '.']


def check_valid_successors(board, row, col):  #check valid successors for rows and columns
    for l in range(row + 1, len(board)):
        if board[l][col] == 'X' or board[l][col] == '@':
            break
        elif board[l][col] == 'p':
            return False
    for l in range(row - 1, -1, -1):
        if board[l][col] == 'X' or board[l][col] == '@':
            break
        elif board[l][col] == 'p':
            return False
    for l in range(col + 1, len(board[0])):
        if board[row][l] == 'X' or board[row][l] == '@':
            break
        elif board[row][l] == 'p':
            return False
    for l in range(col - 1, -1, -1):
        if board[row][l] == 'X' or board[row][l] == '@':
            break
        elif board[row][l] == 'p':
            return False
    return True


def is_goal(board, k):
    if count_pichus(board) == k:
        # print(k)
        row = 0;
        col = 0;
        while row < len(board):
            while col < len(board[0]):
                if (board[row][col] == 'p'):
                    if check_valid_successors(board, row, col) == False:
                        return False
                col += 1
            row += 1
            return True
    else:
        return False


def check_goal_extra(board):
    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            if (board[r][c] == 'p'):
                if check_valid_successors(board, r, c) == False:
                    return False
    return True


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):
    fringe = [initial_board]
    while len(fringe) > 0:
        for b in successors(fringe.pop()):
            if count_pichus(b) > k:
                break
            if is_goal(b, k):
                return (b, True)
            if check_goal_extra(b):
                fringe.append(b)
            # print(is_goal(s,k))
    return ([], False)


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print("Here's what we found:")
    print(printable_board(newboard) if success else "None")




