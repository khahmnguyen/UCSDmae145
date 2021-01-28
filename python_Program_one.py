
"""
The template starts from here
"""

# A15708577 


# from IPython import get_ipython
# # get_ipython().magic('clear')
# get_ipython().magic('reset -sf')

# import all modules here if you need any
import numpy as np
import random
# your file should always start from definition of functions 

def create_board():
    """ Add illustrations here, if needed """
    
    # define variables you need
    
    board = np.array([ [0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])#numpy array to represente a 3 x 3 table, each element should be set as an integer equal to zero
    
    return board


def place(board , player, position):
    """ Add illustrations here, if needed """
    if board[(position)] == 0:
        board[(position)] = player
    else: 
        print('Error: position is not empty')
    return board #(same data type as input board)

def possibilities(board):
    ind = []
    [x,y] = np.where(board==0)
    for i in range(len(x)):
        my_tuple = (x[i], y[i])
        ind.append(my_tuple)
    #operations
    
    return ind #each element in this list should be tuple or it is empty (return [])   

def random_place(board, player):  # Important: you need to use a random seed of 1
    random.seed(1)                # Or you will fail the autograder test; for truly random results comment this line out
    empty_positions = possibilities(board)
    # operations
    board[random.choice(empty_positions)]=player
    return board

def repeat(n):                     # Important: you should enter 1 to initialize the random seed
                                  # # Or you will fail the autograder test, for truly random results comment this line out     
    board = create_board()
    random.seed(1)
    
    if n> 4 or n<1:
        print('Input must be 1<= int <=4')
    else: 
        for i in range(n):
           board = random_place (board, 1)
           board = random_place(board, 2)
    return board
    
# if __name__ == '__main__':
#     """ 
#     This is the place where you can test your function. 
#     You can define variables, feed them into your function and check the output   
#     """
    
#     board = create_board()
#     # board[(1,2)] =3
#     # print(board)
#     board = place(board, 1, (2,2)) 
#     board = place(board, 2, (2,2)) 
#     # for i in range(3):
#     #     board = place(board, 2, (1,i))
    
#     empty_positions = possibilities(board)
#     print(board)
#     print(empty_positions)
#     # board = random_place(board, 1)
 
#     # n =  3# an integer n < 5 since there are only 9 cells in the board and two players in turn place the mark
#     #               # repeat n times
#     # board = repeat(n)
#     print(board)