from Sudoku import Sudoku
import sys, traceback

# Solved sudoku for testing
# sudokuArray = [[8,3,5,4,1,6,9,2,7],
# [2,9,6,8,5,7,4,3,1],
# [4,1,7,2,9,3,6,5,8],
# [5,6,9,1,3,4,7,8,2],
# [1,2,3,6,7,8,5,4,9],
# [7,4,8,5,2,9,1,6,3],
# [6,5,2,7,8,1,3,9,4],
# [9,8,1,3,4,5,2,7,6],
# [3,7,4,9,6,2,8,1,5]]

sudokuArray = [[3, 0, 5, 6, 2, 9, 0, 0, 7],
[7, 0, 6, 1, 0, 8, 0, 0, 0],
[8, 0, 1, 0, 0, 0, 2, 6, 5],
[0, 0, 3, 0, 0, 5, 0, 7, 0],
[6, 8, 7, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 7, 0, 0, 6, 0, 0],
[4, 7, 9, 5, 8, 0, 0, 2, 0],
[1, 0, 0, 4, 3, 0, 5, 0, 9],
[0, 0, 8, 9, 0, 0, 0, 0, 6]]


sudoku = Sudoku(sudokuArray)

print(sudoku)
print("--- To exit insert 10 in all the fields ---")
row = int(input("Insert row [1-9]: "))
col = int(input("Insert column [1-9]: "))
value = int(input("Insert value [1-9]: "))

while row!=10 or col!=10 or value!=10: 
    if (row>0 and row<10) and (col>0 and col<10) and (col>0 and col<10)  and sudoku.changeValue(row-1,col-1,value) :
        print("--- Value changed ---")
        print(sudoku)
        if sudoku.gameFinished():
               print("WE HAVE A WINNER!!")
               sys.exit(0)
        
    else:
        print("!!!!!!!!!! Incorrect position or value. Try it again. !!!!!!!!!! ")
        print(sudoku)
        
    print("--- To exit insert 10 in all the fields ---")   
    row = int(input("Insert row [1-9]: "))
    col = int(input("Insert column [1-9]: "))
    value = int(input("Insert value [1-9]: "))
