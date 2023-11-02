#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys
import time
import statistics

ROW = "ABCDEFGHI"
COL = "123456789"

domain = {}


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

#helper function to see if new assignment of cell=value is consistent
def consistency_test(board, cell):
    #this will give us the letter of the row. But we want an integer
    cell_row=cell[0]
    #this will convert row letter to a row number starting at 0
    cell_row=ROW.index(cell_row)
    #need to convert to string and -1 to get the col index
    cell_column=int(cell[1])-1
    #convert board values to a list
    board_values = list(board.values())

    #verify columns are consistent
    column = board_values[cell_column::9]

    #remove 0's from column
    while 0 in column:
        column.remove(0)
    #if duplicates-->violates constraints, not consistent
    if len(column) != len(set(column)):
        return False
        
    #verify rows are consistent
    row = board_values[9*cell_row:9*(cell_row+1)]
    #remove 0's from row
    while 0 in row:
        row.remove(0)
        #if duplicates-->violates constraints, not consistent
    if len(row) != len(set(row)):
        return False
        
    #verify 3x3 box is consistent
    box1= ['A1', 'A2', 'A3', 
           'B1', 'B2', 'B3', 
           'C1', 'C2', 'C3']
    box2= ['A4', 'A5', 'A6', 
           'B4', 'B5', 'B6', 
           'C4', 'C5', 'C6']
    box3= ['A7', 'A8', 'A9', 
           'B7', 'B8', 'B9', 
           'C7', 'C8', 'C9']

    box4= ['D1', 'D2', 'D3', 
           'E1', 'E2', 'E3', 
           'F1', 'F2', 'F3']
    box5= ['D4', 'D5', 'D6', 
           'E4', 'E5', 'E6', 
           'F4', 'F5', 'F6']
    box6= ['D7', 'D8', 'D9', 
           'E7', 'E8', 'E9', 
           'F7', 'F8', 'F9']

    box7= ['G1', 'G2', 'G3', 
           'H1', 'H2', 'H3', 
           'I1', 'I2', 'I3']
    box8= ['G4', 'G5', 'G6', 
           'H4', 'H5', 'H6', 
           'I4', 'I5', 'I6']
    box9= ['G7', 'G8', 'G9', 
           'H7', 'H8', 'H9', 
           'I7', 'I8', 'I9']

    box_values = []
    if cell in box1:
        for index in box1:
            box_values.append(board[index])
    elif cell in box2:
        for index in box2:
            box_values.append(board[index])
    elif cell in box3:
        for index in box3:
            box_values.append(board[index])
    elif cell in box4:
        for index in box4:
            box_values.append(board[index])
    elif cell in box5:
        for index in box5:
            box_values.append(board[index])
    elif cell in box6:
        for index in box6:
            box_values.append(board[index])
    elif cell in box7:
        for index in box7:
            box_values.append(board[index])
    elif cell in box8:
        for index in box8:
            box_values.append(board[index])
    elif cell in box9:
        for index in box9:
            box_values.append(board[index])
    # print(box_values)
    
    #remove 0's from box_values
    while 0 in box_values:
        box_values.remove(0)
    #duplicates-->violates constraints
    if len(box_values) != len(set(box_values)):
        return False
    
    return True   
    

#initialize domain dictionary for sudoku board
def domains(board):
    global domain
         
    for key in board.keys():
        #if cell already is filled, its domain is that value
        if board[key] != 0:
            domain[key] = {board[key]}
        #if cell is not filled, then domain is list from 1-9
        #use sets for faster lookup
        else:
            domain[key] = set(range(1,10))
            for row in ROW:
                if board[row + key[1]] != 0:
                    domain[key].discard(board[row + key[1]])
            for column in COL:
                if board[key[0]+column] !=0:
                    domain[key].discard(board[key[0]+column])


#forward checking to remove num from domains of cells in same row, column, and same 3x3box 
def forward_checking(board, cell, num):
    global domain
#set domain of current cell=num
    domain[cell] = {num}
#remove value from the domains of all cells in the row
    for column in COL:
        key = cell[0] + column
        #don't need to check current cell
        if key!=cell:
            if num in domain[key]:
                domain[key].remove(num)
                if len(domain[key])==0:
                    return False
#remove value from the domains of all cells in the column
    for row in ROW:
        key = row + cell[1]
        #don't need to check current cell
        if key!=cell:
            if num in domain[key]:
                domain[key].remove(num)
                if len(domain[key])==0:
                    return False
#remove this value from the domains of all cells in the 3x3box
    box1= ['A1', 'A2', 'A3', 
           'B1', 'B2', 'B3', 
           'C1', 'C2', 'C3']
    box2= ['A4', 'A5', 'A6', 
           'B4', 'B5', 'B6',
           'C4', 'C5', 'C6']
    box3= ['A7', 'A8', 'A9', 
           'B7', 'B8', 'B9', 
           'C7', 'C8', 'C9']
    box4= ['D1', 'D2', 'D3', 
           'E1', 'E2', 'E3', 
           'F1', 'F2', 'F3']
    box5= ['D4', 'D5', 'D6', 
           'E4', 'E5', 'E6', 
           'F4', 'F5', 'F6']
    box6= ['D7', 'D8', 'D9', 
           'E7', 'E8', 'E9', 
           'F7', 'F8', 'F9']
    box7= ['G1', 'G2', 'G3', 
           'H1', 'H2', 'H3', 
           'I1', 'I2', 'I3']
    box8= ['G4', 'G5', 'G6', 
           'H4', 'H5', 'H6', 
           'I4', 'I5', 'I6']
    box9= ['G7', 'G8', 'G9', 
           'H7', 'H8', 'H9',
           'I7', 'I8', 'I9']
    if cell in box1:
        box = box1 
    elif cell in box2:
        box= box2
    elif cell in box3:
        box = box3
    elif cell in box4:
        box= box4
    elif cell in box5:
        box= box5
    elif cell in box6:
        box=box6
    elif cell in box7:
        box=box7
    elif cell in box8:
        box=box8
    elif cell in box9:
        box=box9

    for key in box:
        if key!=cell:
            if num in domain[key]:
                domain[key].remove(num)
                if len(domain[key])==0:
                    return False
    return True

#checks to see if board is complete (all keys have values that are not 0)
def is_complete(board):
    for key in board.keys():
        if board[key] == 0:
            return False
    return True

def backtracking(board):
    """Takes a board and returns solved board."""
    global domain
    #base case:
    if is_complete(board):
        solved_board = board
        return solved_board
    #use MRV heurisitc to select a cell
    minimum_domain_size = 10
    for key in board.keys():
        if board[key] == 0 and len(domain[key]) < minimum_domain_size:
                selected_cell = key
                minimum_domain_size = len(domain[key])
    #for each value in selected_cell's domain
    for num in domain[selected_cell]:
        board[selected_cell] = num
        # print(selected_cell, num)
        if consistency_test(board, selected_cell):
            #save current domain
            current_domain = {k: list(v) for k, v in domain.items()}
            #Forward check
            if (forward_checking(board, selected_cell, num)):
                # print(board)
                result = backtracking(board)
                if result:
                    return result
                # solved_board = board
                # return solved_board
            #remove {var=value} and inferences from assignment
            board[selected_cell] = 0
            domain = current_domain
        board[selected_cell] = 0
    return None
# solved_board = board
# return solved_board 
                
    # TODO: implement this



if __name__ == '__main__':

    
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}  

        domains(board)     
        
        start_time  = time.time()
        
        solved_board = backtracking(board)
        end_time = time.time()
        running_time = end_time-start_time
        print(board_to_string(solved_board))
        print(f"{running_time} seconds")