class Sudoku:
    def __init__(self, array):
        self.array = array
    
    def __str__(self):
        game = ""
        for i in range(len(self.array)):
            if i%3 == 0:
                game +="-------------------------" + '\n'
            for j in range(len(self.array)):
                if j%3 == 0:
                    game += "| "
                game += str(self.array[i][j]) + " "
            game +="| " + '\n'
        game += "-------------------------" 
        return game

    def getPosition(self,row,column):
        return self.array[row][column]
    
     #Method that given a row a column and a value returns True if all the comprovations are True and change the selected value
    def changeValue(self,row,column,value):
        if self.comZero(row,column)==True:
            if self.comRow(row,value):
                if self.comColumn(column,value):
                    if self.comSquare(row,column,value):
                        self.array[row][column] = value
                        return True
        return False
        
    #Method that given a column and a column returns True if there isn't a zero in the selected position
    def comZero(self,row,column):
        if self.array[row][column]==0:return True
        return False
        
    #Method that given a row and a value returns True if there aren't any repeated value in the row     
    def comRow(self,row,value):
        for x in range(len(self.array)):
            if self.array[row][x] == value: return False      
        return True
    
    #Method that given a column and a value returns True if there aren't any repeated value in the column 
    def comColumn(self,column,value):
        for x in range(len(self.array)):
            if self.array[x][column] == value: return False 
        return True
    
    #Method that given a row a column and a value returns True if there aren't any repeated value in the square
    def comSquare(self,row,column,value):
        row //= 3
        row *= 3
        column //= 3
        column *= 3
        square =[]

        for w in range(row,row+3):
            for h in range(column,column+3):
                square.extend(str(self.array[w][h]))
        
        if str(value) in str(square):
            return False
        else:
            return True      
    
    #Method that checks if theres in any 0, if there isn't any returns True which means that there is a winner 
    def gameFinished(self):
        for x in range(len(self.array)):
            for y in range(len(self.array[0])):
                if 0 in self.array:
                    return False
        return True
