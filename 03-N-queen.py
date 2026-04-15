
#solving N-queen

#we need 2 function isSafe(mat,row,col) and solveNQueen(mat,row)
#approach is place to place the queen row wise and if we are not able to place the in row then we back trcak that means we go back to previos row and change is placement
# when placing a quen we check upper columm , left daignol and right daignnol is we don't encounter any queen then that position is safe and we can place the queen and move to next row


def isSafe(mat,row,col):
    n  = len(mat) #size of board in n queen row and col are eqaul
    
    for i in range(row): # ye upper ke colum ko chek krne ke liye i - 0,1,..row-1
        if mat[i][col] == 'Q': return False
        
    i,j = row-1 , col -1 # to check for upper left daignol
    
    while i>=0 and j>= 0:
        if mat[i][j] == 'Q': return False
        i-=1 ; j-=1
    
    i,j = row-1,col+1
    
    while i>=0 and j<n :
        if mat[i][j] == 'Q': return False
        i-=1; j+=1
    
    return True # agr koi conflict nhi mile then return True

def solveNQueens(mat,row): 
    n = len(mat)
    
    if row == n : # saare queen placed ho chuke hai considering we follow 0 - n-1 row number conventino
        for r in mat: print(r)
        return   #  matrix print kara ke void return krdo so that function stack khtmk ho
    
    # if row != n to hum current row mein each colum mein check karenge ifsafe to place krke move to next row recusilvely to support backtracking
    
    for col in range(n):
        if isSafe(mat,row,col):
            mat[row][col] = 'Q'
            #------ most important lines
            solveNQueens(mat,row+1) # recursive to suport 
            
            mat[row][col] = "." # here comes the back track


    