# N Queens problem solved using Back tracking
#
#
# Solving for possible column position for each row such that
# there is no 'Queen' conflict for each chosen column position
# If there is a 'Queen' conflict, using backTracking algorithm 
# to rework on the previous col postion found. 

import time

def PrintBoard2(ColPos, size):
    for row in range(size):
        for col in range(size):
            if ColPos[row]== col:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

def diagonallyClashing(ColPos, row, col, size):
    indecesAlreadyTaken = []
    conflict = False
    for ro in range(size):
        if ColPos[ro] != -1:
            indecesAlreadyTaken += [ro *size + ColPos[ro]]
    conflitingPos = []
    conflitingPos += list(range(row*size + col, -1, -size-1))[1:][0:col]  # trailingLeftDiag 
    conflitingPos += list(range(row*size+col, 0, 1-size))[1:][:(size-1)-col] # trailingRightDiag 
    conflitingPos += list(range(row*size + col, size*size, size-1))[1:col+1] # leadingLeftDiag 
    conflitingPos += list(range(row*size + col, size*size, size+1))[1:size-col] # leadingRightDiag 

    #print(row, col, indecesAlreadyTaken, end='  ')
    for pos in conflitingPos:
        if any(x == pos for x in indecesAlreadyTaken):
            conflict = True
            break
    #print(conflitingPos, conflict)
    return conflict

def isValidColPos(ColPos, row, col, size):
    if any(x == col for x in ColPos):
        return False
    elif diagonallyClashing(ColPos, row, col, size):
        return False
    else:
        return True

def SolveColPositions(ColPos, size):
    for row in range(size):
        if ColPos[row] == -1:
            for col in range(size):
                if isValidColPos(ColPos, row, col, size):
                    ColPos[row] = col
                    if (SolveColPositions(ColPos, size)):
                        return True
                    else:
                        ColPos[row] = -1
            return False
    return True


size = 12
#for size in range(4, 30):
start = time.time()
ColPositions = [-1]*size
solved = SolveColPositions(ColPositions, size)
print(size, time.time() - start)

print()
print(solved, ColPositions)
print()
PrintBoard2(ColPositions, size)
