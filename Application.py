from Sudoku import Sudoku


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
row = int(input("Insert row [0-9]: "))
col = int(input("Insert column [0-9]: "))
value = int(input("Insert value [0-9]: "))

while row!=10 and col!=10 and value!=10: 
    if sudoku.changeValue(row,col,value):
        print("--- Value changed ---")
        print(sudoku)   
    else:
        print("!!!!!!!!!! Incorrect position or value. Try it again. !!!!!!!!!! ")
        print(sudoku)
        
    print("--- To exit insert 10 in all the fields ---")   
    row = int(input("Insert row [0-9]: "))
    col = int(input("Insert column [0-9]: "))
    value = int(input("Insert value [0-9]: "))
