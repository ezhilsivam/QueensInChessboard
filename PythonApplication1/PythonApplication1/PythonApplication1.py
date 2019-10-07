# 8 Queens problem solved using Back tracking
#
#
# Solving for possible column position for each row such that
# there is no 'Queen' conflict for each chosen column position
# If there is a 'Queen' conflict, using backTracking algorithm 
# to rework on the previous col postion found. 

def PrintBoard2(ColPos):
    for row in range(8):
        for col in range(8):
            if ColPos[row]== col:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

def diagonallyClashing(ColPos, row, col):
    indecesAlreadyTaken = []
    conflict = False
    for ro in range(8):
        if ColPos[ro] != -1:
            indecesAlreadyTaken += [ro *8 + ColPos[ro]]
    conflitingPos = []
    conflitingPos += list(range(row*8 + col, -1, -9))[1:][0:col]  # trailingLeftDiag 
    conflitingPos += list(range(row*8+col,0, -7))[1:][:7-col] # trailingRightDiag 
    conflitingPos += list(range((row*8 + col), 64, 7))[1:col+1] # leadingLeftDiag 
    conflitingPos += list(range((row*8 + col),64,9))[1:8-col] # leadingRightDiag 

    #print(row, col, indecesAlreadyTaken, end='  ')
    for pos in conflitingPos:
        if any(x == pos for x in indecesAlreadyTaken):
            conflict = True
            break
    #print(conflitingPos, conflict)
    return conflict

def isValidColPos(ColPos, row, col):
    if any(x == col for x in ColPos):
        return False
    elif diagonallyClashing(ColPos, row, col):
        return False
    else:
        return True

def SolveColPositions(ColPos):
    for row in range(8):
        if ColPos[row] == -1:
            for col in range(8):
                if isValidColPos(ColPos, row, col):
                    ColPos[row] = col
                    if (SolveColPositions(ColPos)):
                        return True
                    else:
                        ColPos[row] = -1
            return False
    return True


ColPositions = [-1]*8
solved = SolveColPositions(ColPositions)
print()
print(solved, ColPositions)
print()
PrintBoard2(ColPositions)
