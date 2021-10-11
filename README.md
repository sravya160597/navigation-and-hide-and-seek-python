# Assignment 0
## Part 1 Navigation:
* Code Overview:
In the first part route.pichu.py the following map is given and the initial position of the P is given at (5,1):
```
....XXX
.XXX...
....X..
.X.X.X.
pX....@
```
This map is read as the filename and the board is stored as the house map. To find the solution of the problem the board is passed to the search function.
First, we find the initial pichu location to start the route from there and end up at @. We store the initial pichu location along with the empty character to store the path in the fringe.
The vis_path array stores all the visited states. When the fringe is not empty it iterates in the while loop to find the path. The fringe.pop(0) always pops out the first element in the fringe and is stored in the curr_move . All the moves are stored in the vis_path. 
For every move it checks if that particular state is @ (goal state), if it is the goal state then we return the current distance and the path. If that is not the goal state then we check if that particular state is present in the vis_path array. If it is not present then we append it to the fringe at the end. All the states appended into the fringe are checked and then pop the first element till the fringe becomes empty.
We use BFS (breadth first search) algorithm. The first in first out approach is used where the fringe.pop(0) is used to take each state and search for the successor states.

The code I changed is in the search function :
```
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
                                return (curr_dist+1,move[2]
                        else:
                                if (move[0],move[1]) not in vis_path:
                                        fringe.append(((move[0],move[1]),curr_dist + 1,move[2]))
```
In the above function :
In the fringe tuple I have added the ‘’ to store the directions. I have added the curr_path variable to store the directions of the path.

* Problems Faced:
When I started analysing the code, it took me a while to understand what was happening and what all states are being considered to find the path and ultimately reach the goal state. The first time I made small changes in return function as curr_dist. I was not getting the right answer. Then again I used the BFS approach to pop the elements and then got the right answer. For the path traversed at the start the states which have been traversed previously were also getting added to the path. So after brainstorming I have added an array vis_path and checking if the present state is not present in that particular vis_path then only the state is getting appended to fringe. After doing that I was able to get the correct path.

* Initial State:
The initial statement would be the map given to start the navigation. That is 1 P at the end of the board.

* Goal State:
The goal state is @ where the P reaches the @ by traversing through the .’s and X’s.

* Set of valid states:
For the P to move till @ the P can move through the dots. Therefore the . is the valid state and the X is the invalid state.

* Cost function: 
Cost function is irrelevant here there are no costs given and we need to find the optimal solution to reach the goal state.

## Part 2 Hide and Seek :
* Code Overview:
In this part of the assignment, K is the number of P’s that should be placed.I started by analysing the solve function. The initial board is stored in the fringe and each state is poped out of the fringe. Then the successors function is called by passing each state in the fringe to that function. The add_pichu function is called for every successor state. The add_pichu adds a P at every possible state where there is a . in the board but we need to check if the location of the P is valid or not. So we check the goal function by passing the board and the k value.
```
if (board[row][col] == 'p'):
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
```

If the count of the pichus = k then the successor functions are checked where each successor of the P is checked in the row up, row down, column left, column right. When in the row and column there occurs X or @ the loop breaks that means that is a valid successor. If there occurs a P then there is no scope for including one more p so returns a false

The board and k is passed to is_goal where the count of pichus is checked and then it is checked for valid successors. After that one more goal function is written because an additional check is done for the P such that the successor state doesnot contain a P because after the is_goal in some cases adjacent P’s are being added.

* Problems faced:
While analysing the code, it was difficult in the first place to add the extra p’s and even after writing the function to check the successors in some cases the P’s are getting added side by side therefore I had to use an extra goal check function to avoid that case.

* Initial State:
The initial statement would be the map given to start the navigation. That is 1 P present at on the board

* Goal State:
The goal state is being able to place K p’s on the board.

* Set of valid states:
In this problem the set of valid states would be adding k number of p’s such there is X or @ in between two p’s.

* Cost function: 
Cost function is irrelevant here there are no costs given and we need to find the optimal solution to reach the goal state where we are able to place k p’s satisfying the condition





