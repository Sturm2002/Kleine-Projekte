from copy import deepcopy
import operator

pawn_field = [
    [1,1,1,1,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [2,2,2,2,2,2]
]

checkers_field = [
    [0,1,0,1,0,1],
    [0,0,1,0,1,0],
    [0,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,2,0,2,0,2],
    [0,0,0,0,0,0]
]

ttt_field = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

BLACK = 1
WHITE = 2

def runAlgorithm(name, field, depth):
    if name == 1:
        return minimax(field, depth, True, pawnEvaluation, name)[1]
    elif name == 2:
        return minimax(field, depth, True, pawnEvaluation, name)[1]
    elif name == 3:
        pass # hier deinen code
        return field

def minimax(field, depth, isMax, evalFunction, gameName):
    if depth == 0:
        return evalFunction(field), field
    if isMax:
        maxEval = float('-inf')
        bestMove = None
        for move in getAllMoves(field, BLACK, gameName):
            evaluation =  minimax(move[0], depth-1, False, evalFunction, gameName)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move
            #Check if piece got captured
            if move[1] != None:
                return maxEval, bestMove
                break
        return maxEval, bestMove
    else:
        minEval = float('inf')
        bestMove = None
        for move in getAllMoves(field, WHITE, gameName):
            evaluation =  minimax(move[0], depth-1, True, evalFunction, gameName)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move
                        #Check if piece got captured
            if move[1] != None:
                return minEval, bestMove
                break
        return minEval, bestMove

def pawnEvaluation(field):
    whitePieces = len(getAllPieces(field, WHITE))
    blackPieces = len(getAllPieces(field, BLACK))
    if whitePieces == 0:
        return 10
    elif blackPieces == 0:
        return -10
    return blackPieces - whitePieces  + (checkWin(field, BLACK) - checkWin(field, WHITE))
    
def checkWin(field, color):
    if color == BLACK:
        for column in field[0]:
            if column == WHITE:
                return 10
    elif color == WHITE:
        for column in field[len(field)-1]:
            if column == BLACK:
                return -10
    return 0

def getAllMoves(field, pieceValue, gameName):
    moves = []
    pieces = getAllPieces(field, pieceValue)
    for piece in pieces:
        for move in getPieceMoves(piece, pieceValue, field, gameName):
            simulatedMove = simulateMove(field, piece, move[0], pieceValue,gameName, move[1])
            moves.append([simulatedMove[0],simulatedMove[1]])
    return moves

def getAllPieces(field, pieceValue):
    positions = []
    for row in range(len(field)):
        for column in range(len(field)):
            if field[row][column] == pieceValue:
                positions.append([row,column])
    return positions

def getPieceMoves(piece, pieceValue, field, gameName):
    if pieceValue == BLACK:
        return getDownwardMoves(piece, field, gameName)
    return getUpwardMoves(piece, field, gameName)

def getDownwardMoves(piece, field, gameName):
    if gameName == 1: 
       return getPawnMoves(piece, field, operator.add, WHITE)
    elif gameName == 2:
        return getCheckersMoves(piece, field, operator.add, WHITE)

def getUpwardMoves(piece, field, gameName):
    if gameName == 1:
        return getPawnMoves(piece, field, operator.sub, BLACK)
    elif gameName == 2:
        return getCheckersMoves(piece, field, operator.sub, BLACK)


def getPawnMoves(piece, field, operatorFunction, oponentColor):
    pieceMoves = []
    #Check direction of movement. If moving downwards -> check if piece would move out of range
    if operatorFunction == operator.add and piece[0] < len(field) -1 or operatorFunction == operator.sub and piece[0] > 0:
        #Move forward
        if field[operatorFunction(piece[0],1)][piece[1]] == 0:
            pieceCopy = deepcopy(piece)
            pieceCopy[0] = operatorFunction(pieceCopy[0],1)
            pieceMoves.append([pieceCopy, False])
        #Capture left
        if piece[1] > 0 and field[operatorFunction(piece[0],1)][piece[1]-1] == oponentColor:
            pieceCopy = deepcopy(piece)
            pieceCopy[0] = operatorFunction(piece[0],1)
            pieceCopy[1] -= 1
            pieceMoves.append([pieceCopy, True])
        #Move right
        if piece[1] < len(field) -2 and field[operatorFunction(piece[0],1)][piece[1]+1] == oponentColor:
            pieceCopy = deepcopy(piece)
            pieceCopy[0] = operatorFunction(piece[0],1)
            pieceCopy[1] += 1
            pieceMoves.append([pieceCopy, True])
    return pieceMoves 

def getCheckersMoves(piece, field, operatorFunction, oponentColor):
    moves = []
    capture = False 
    #Check if piece is able to move 2 upward/downward
    if piece[0] >= 2 and operatorFunction == operator.sub or piece[0] <= len(field) - 3 and operatorFunction == operator.add:
        #Check capture right
        #Check if piece is able to move right
        if piece[1] <= len(field) - 3:
            #Check if oponent is adjecent
            if (field[operatorFunction(piece[0],1)][piece[1]+1] == oponentColor): 
                #Check if field behind oponent is available
                if field[operatorFunction(piece[0],2)][piece[1] + 2] == 0:
                    pieceCopy = deepcopy(piece)
                    pieceCopy[0] = operatorFunction(piece[0],2)
                    pieceCopy[1] += 2
                    moves.append([pieceCopy, True])
        #Check capture left
        #Check if piece is able to move left
        if piece[1] >= 2:
            #Check if oponent is adjecent left
            if (field[operatorFunction(piece[0],1)][piece[1]-1] == oponentColor):
                #Check if field behind oponent is available
                if field[operatorFunction(piece[0],2)][piece[1] - 2] == 0:
                    pieceCopy = deepcopy(piece)
                    pieceCopy[0] = operatorFunction(piece[0],2)
                    pieceCopy[1] -= 2
                    moves.append([pieceCopy, True])

        if len(moves) >= 1:
            capture = True
            return moves
    #check move without capture 
    if capture == False: 
        if operatorFunction == operator.sub and piece[0] >=1 or operatorFunction == operator.add and piece[0] <= len(field) -2:
            #check left move
            if piece[1] > 1 and field[operatorFunction(piece[0],1)][piece[1] - 1] == 0:
                pieceCopy = deepcopy(piece)
                pieceCopy[0] = operatorFunction(piece[0],1)
                pieceCopy[1] -= 1
                moves.append([pieceCopy, False])
            #check right move
            if piece[1] < len(field) -1 and field[operatorFunction(piece[0],1)][piece[1] + 1] == 0:
                pieceCopy = deepcopy(piece)
                pieceCopy[0] = operatorFunction(piece[0],1)
                pieceCopy[1] += 1
                moves.append([pieceCopy, False])
    return moves

def simulateMove(field, fromPosition, toPosition, pieceValue, gameName, hasCaptured):
    fieldCopy = deepcopy(field)
    capturedPiece = None
    if gameName == 1:
        fieldCopy[fromPosition[0]][fromPosition[1]] = 0
        fieldCopy[toPosition[0]][toPosition[1]] = pieceValue
    elif gameName == 2:
        fieldCopy[fromPosition[0]][fromPosition[1]] = 0
        if hasCaptured:
            capturedPiece = [int((fromPosition[0] + toPosition[0]) /2),int((fromPosition[1] + toPosition[1]) /2)]
            fieldCopy[capturedPiece[0]][capturedPiece[1]] = 0
            fieldCopy[toPosition[0]][toPosition[1]] = pieceValue
        elif not hasCaptured:
            fieldCopy[toPosition[0]][toPosition[1]] = pieceValue
    return fieldCopy, capturedPiece

print(runAlgorithm(2,checkers_field,5))