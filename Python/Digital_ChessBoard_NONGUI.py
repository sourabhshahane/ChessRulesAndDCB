#               N
#               ^
#          W  -----  E
#               !
#               !
#               !
#               S


pgn_Event = "Casual Game"                  #Name of the event (descriptive and same for same events for easy scanning / '?' if unknown) e.g. 1. "FIDE World Championship" 2. "Casual Game"
pgn_Site = "Riga LAT"                      #Site of the event (should include region, city, and country in standerd 3 letter notation / '?' if unknown) e.g. 1. "New York City, NY USA" 2. "St. petersburg RUS" 3. "Riga LAT"
pgn_Date = "1999.05.27"                    #Date of the event in YYYY.MM.DD (if any unknown '?' is used at the place) e.g. 1. 1999.05.27 2. 1998.07.?? etc
pgn_Round = "1"                            #Round of the game ('?' if unknown, should be whole number, and incase of hierarchy, single '.' is used to seperate them) e.g. 1. 1 2. 3.1
pgn_White = "Shahane, Sourabh S."          #Player name playing as white(The name should appear as in telephone directory-> "Last_Name, First_Name" and they are seperated by ", " and wherever initial apears it must be followed by period "." if multiple players playing white, they should be written in alphabetical order & seperated by a colon and if a program is playing the game version number is required / "?" if unknown) e.g. 1. "Tal, Mikhail N." 2. "Alphazero v1.1"
pgn_Black = "Tal, Mikhail N."              #Player name playing as Black(The name should appear as in telephone directory-> "Last_Name, First_Name" and they are seperated by ", " and wherever initial apears it must be followed by period "." if multiple players playing black, they should be written in alphabetical order & seperated by a colon and if a program is playing the game version number is required / "?" if unknown)
pgn_Result = "1-0"                         #result of the game, should be exact same as the gametext termination marker. 4 possibilities "1-0" -> white won / "0-1" -> black won / "1/2-1/2" -> draw / "*" -> game in progress / abandoned / result unknown 
pgn_WhiteELO= "3215"                       #ELO of white at the start of the game
pgn_BlackELO= "3421"                       #ELO of Black at the start of the game

pgn_movetext = '''

'''

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True 
    else:
        return False


class pawns():
    def __init__(self, isWhite, positions, ids) -> None:
        self.name = 'P'
        self.ids = ids
        self.positions = positions
        self.isWhite = isWhite
        self.isKilled = 8*[False]
        self.isFirstMove = 8*[True]
        self.isUpgraded = 8*[False]
        self.isEnPassantVulnerable = 8*[False]

    def listOfAllPossibleSquares(self, id):
        List = list()
        index = self.ids.index(id)
        currentPosX = self.positions[index][0]
        currentPosY = self.positions[index][1]
        if(self.isWhite):
            if(self.isFirstMove[index] == True):
                List.append((currentPosX+2, currentPosY))
            for i in [-1, 0, 1]:
                if(currentPosY + i in range(1, 9)):
                    List.append((currentPosX + 1, currentPosY + i))
            return List
        else:
            if(self.isFirstMove[index] == True):
                List.append((currentPosX-2, currentPosY))
            for i in [-1, 0, 1]:
                if(currentPosY + i in range(1, 9)):
                    List.append((currentPosX - 1, currentPosY + i))
            return List
    
    def enPassantPawnPosition(self):
        if self.isEnPassantVulnerable != 8*[False]:
            return self.positions[self.isEnPassantVulnerable.index(True)]
        else:
            return None

class rooks():
    def __init__(self, isWhite, positions, ids) -> None:
        self.name = 'R'
        self.ids = ids
        self.positions = positions
        self.isWhite = isWhite
        self.isKilled = 2*[False]
        self.isFirstMove = 2*[True]

    def listOfAllPossibleSquares(self, id):
        List = list()
        index = self.ids.index(id)
        currentPosX = self.positions[index][0]
        currentPosY = self.positions[index][1]
        for i in range(1, 9):
            for j in range(1, 9):
                if(j != currentPosY and i == currentPosX):List.append((currentPosX, j))
                if(i != currentPosX and j == currentPosY):List.append((i, currentPosY))
        return List

class knights():
    def __init__(self, isWhite, positions, ids) -> None:
        self.name = 'N'
        self.ids = ids
        self.positions = positions
        self.isWhite = isWhite
        self.isKilled = 2*[False]

    def listOfAllPossibleSquares(self, id):
            List = list()
            index = self.ids.index(id)
            currentPosX = self.positions[index][0]
            currentPosY = self.positions[index][1]
            for i in [-2, 2]:
                for j in [1, -1]:
                    if(currentPosX + i in range(1, 9) and currentPosY + j in range(1, 9)):
                        List.append((currentPosX + i, currentPosY + j))
                    if(currentPosX + j in range(1, 9) and currentPosY + i in range(1, 9)):
                        List.append((currentPosX + j, currentPosY + i))
            return List

class bishops():
    def __init__(self, isWhite, positions, ids) -> None:
        self.name = 'B'
        self.ids = ids
        self.positions = positions
        self.isWhite = isWhite
        self.isKilled = 2*[False]
    
    def listOfAllPossibleSquares(self, id):
        List = list()
        index = self.ids.index(id)
        currentPosX = self.positions[index][0]
        currentPosY = self.positions[index][1]
        for i in range(-8, 9):
            for j in range(8, -9, -1):
                if i == 0 and j == 0:
                    pass
                elif(currentPosX + i in range(1, 9) and currentPosY + j in range(1, 9) and i == -j and i != 0 and j != 0):
                    List.append((currentPosX + i, currentPosY + j))
                elif(currentPosX + i in range(1, 9) and currentPosY + j in range(1, 9) and i == j and i != 0 and j != 0):
                    List.append((currentPosX + i, currentPosY + j))
        return List

class Queens():
    def __init__(self, isWhite, positions, ids) -> None:
        self.name = 'Q'
        self.ids = ids
        self.positions = positions
        self.white = isWhite
        self.iskilled = [False]

    def listOfAllPossibleSquares(self, id):
        List = list()
        index = self.ids.index(id)
        currentPosX = self.positions[index][0]
        currentPosY = self.positions[index][1]
        for i in range(-8, 9):
            for j in range(8, -9, -1):
                if(j != currentPosY and i == currentPosX and i > 0 and j > 0):List.append((currentPosX, j))
                if(i != currentPosX and j == currentPosY  and i > 0 and j > 0):List.append((i, currentPosY))
                if i == 0 and j == 0:
                    pass
                elif(currentPosX + i in range(1, 9) and currentPosY + j in range(1, 9) and i == -j and i != 0 and j != 0):
                    List.append((currentPosX + i, currentPosY + j))
                elif(currentPosX + i in range(1, 9) and currentPosY + j in range(1, 9) and i == j and i != 0 and j != 0):
                    List.append((currentPosX + i, currentPosY + j))
        return List

class King():
    def __init__(self, isWhite, position, id) -> None:
        self.name = 'K'
        self.id = id
        self.position = position
        self.isWhite = isWhite
        self.isCastled = False
        self.isFirstMove = True

    def listOfAllPossibleSquares(self):
        List = list()
        currentPosX = self.position[0][0]
        currentPosY = self.position[0][1]
        for i in [1, 0, -1]:
            for j in [-1, 0, 1]:
                if((currentPosX + i) in range(1, 9) and (currentPosY + j) in range(1, 9) ):
                    if(i == 0 and j == 0):
                        pass
                    else:
                        List.append((currentPosX + i, currentPosY + j))
        return List

class pieces():
    def __init__(self, pawns, rooks, bishops, Queens, King, knights) -> None:
        self.whiteRooks = rooks(True, [(1,1), (1,8)], ids = [1, 8])
        self.whiteKnights = knights(True, [(1,2), (1,7)], ids = [2, 7])
        self.whiteBishops = bishops(True, [(1,3), (1,6)], ids = [3, 6])
        self.whiteQueens = Queens(True, [(1,4)], ids = [4])
        self.whiteKing = King(True, [(1,5)], id = [5])
        self.whitePawns = pawns(True, [(2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8)], ids = [i+1 for i in range(8,16)])

        self.blackPawns = pawns(False, [(7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8)], ids = [i+1 for i in range(16,24)])
        self.blackRooks = rooks(False, [(8,1), (8,8)], ids = [25, 32])
        self.blackKnights = knights(False, [(8,2), (8,7)], ids = [26, 31])
        self.blackBishops = bishops(False, [(8,3), (8,6)], ids = [27, 30])
        self.blackQueens = Queens(False, [(8,4)], ids = [28])
        self.blackKing = King(False, [(8,5)], id = [29])


class chessboard():
    
    def __init__(self, pieces) -> None:
        self.turn = "W"
        self.ids = [i+1 for i in range(0,32)]
        self.whiteIDs = [i+1 for i in range(0, 16)]
        self.blackIDs = [i+1 for i in range(16, 32)]
        self.pieces = pieces(pawns, rooks, bishops, Queens, King, knights)
        self.ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.currentWhitePiecePositions = [
            (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8)
        ]

        self.currentBlackPiecePositions = [
            (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8)
        ]
        
        self.currentAllPiecePositions = [
            (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8)
          , (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8)
        ]                                   #give id-1 as index to currentPositions and it will give the piece's co-ordinates

        self.id2name = {
             '1': 'WR',  '2': 'WN',  '3': 'WB',  '4': 'WQ',  '5': 'WK',  '6': 'WB',  '7': 'WN',  '8': 'WR',
             '9': 'WP', '10': 'WP', '11': 'WP', '12': 'WP', '13': 'WP', '14': 'WP', '15': 'WP', '16': 'WP',
            '17': 'BP', '18': 'BP', '19': 'BP', '20': 'BP', '21': 'BP', '22': 'BP', '23': 'BP', '24': 'BP',
            '25': 'BR', '26': 'BN', '27': 'BB', '28': 'BQ', '29': 'BK', '30': 'BB', '31': 'BN', '32': 'BR',
        }

        self.allPositions = [
            (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8)
          , (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8)
          , (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8)
          , (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8)
          , (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8)
          , (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8)  
          , (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8)
          , (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8)
        ]

        self.coordinates = [
            ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
            ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
            ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
            ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
            ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
            ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
        ]

    def listOfAllPossibleMoves(self, id):

        squaresList = list()
        movesList = list()
        finalMovesList = list()

        piece = self.id2name[str(id)]

        if piece[1] == 'P':
            return self.possiblePawnMoves(id)

        elif piece[1] == 'R':

            if self.possibleMovesInDirection(id, 'N') != None:movesList+= self.possibleMovesInDirection(id, 'N')
            if self.possibleMovesInDirection(id, 'E')!= None:movesList+= self.possibleMovesInDirection(id, 'E')
            if self.possibleMovesInDirection(id, 'S') != None:movesList+= self.possibleMovesInDirection(id, 'S')
            if self.possibleMovesInDirection(id, 'W') != None:movesList+= self.possibleMovesInDirection(id, 'W')

            return movesList
        
        elif piece[1] == 'N':
            if piece[0] == 'W':
                squaresList = self.pieces.whiteKnights.listOfAllPossibleSquares(id)
                for square in squaresList:
                    if square not in self.currentWhitePiecePositions:
                        finalMovesList.append(square)
            else:
                squaresList = self.pieces.blackKnights.listOfAllPossibleSquares(id)
                for square in squaresList:
                    if square not in self.currentBlackPiecePositions:
                        finalMovesList.append(square)
            return finalMovesList

        elif piece[1] == 'B':
            if self.possibleMovesInDirection(id, 'NE') != None:movesList+= self.possibleMovesInDirection(id, 'NE')
            if self.possibleMovesInDirection(id, 'SE')!= None:movesList+= self.possibleMovesInDirection(id, 'SE')
            if self.possibleMovesInDirection(id, 'SW') != None:movesList+= self.possibleMovesInDirection(id, 'SW')
            if self.possibleMovesInDirection(id, 'NW') != None:movesList+= self.possibleMovesInDirection(id, 'NW')

            return movesList
        
        elif piece[1] == 'Q':
            
            if self.possibleMovesInDirection(id, 'N') != None:movesList+= self.possibleMovesInDirection(id, 'N')
            if self.possibleMovesInDirection(id, 'E')!= None:movesList+= self.possibleMovesInDirection(id, 'E')
            if self.possibleMovesInDirection(id, 'S') != None:movesList+= self.possibleMovesInDirection(id, 'S')
            if self.possibleMovesInDirection(id, 'W') != None:movesList+= self.possibleMovesInDirection(id, 'W')
            if self.possibleMovesInDirection(id, 'NE') != None:movesList+= self.possibleMovesInDirection(id, 'NE')
            if self.possibleMovesInDirection(id, 'SE')!= None:movesList+= self.possibleMovesInDirection(id, 'SE')
            if self.possibleMovesInDirection(id, 'SW') != None:movesList+= self.possibleMovesInDirection(id, 'SW')
            if self.possibleMovesInDirection(id, 'NW') != None:movesList+= self.possibleMovesInDirection(id, 'NW')
        
            return movesList

        elif piece[1] == 'K':
            if piece[0] == 'W':
                squaresList = self.pieces.whiteKing.listOfAllPossibleSquares()

                isKingsFirstMove = self.pieces.whiteKing.isFirstMove
                isRooksFirstMove = self.pieces.whiteRooks.isFirstMove

                if isKingsFirstMove:
                    if isRooksFirstMove[0] == True:
                        if len(self.possibleMovesInDirection(id, 'W')) == 3:
                            if self.isInCheck(id) == False:
                                if not common_member(self.possibleMovesInDirection(id, 'W')[:2], self.allPossibleOpponentsMoves(id)):
                                    finalMovesList.append((self.pieces.whiteKing.position[0][0], self.pieces.whiteKing.position[0][1] - 2))
                    
                    elif isRooksFirstMove[1] == True:
                        if len(self.possibleMovesInDirection(id, 'E')) == 2:
                            if self.isInCheck(id) == False:
                                if not common_member(self.possibleMovesInDirection(id, 'E'), self.allPossibleOpponentsMoves(id)):
                                    finalMovesList.append((self.pieces.whiteKing.position[0][0], self.pieces.whiteKing.position[0][1] + 2))
            
            else:
                squaresList = self.pieces.blackKing.listOfAllPossibleSquares()

                isKingsFirstMove = self.pieces.blackKing.isFirstMove
                isRooksFirstMove = self.pieces.blackRooks.isFirstMove
                
                if isKingsFirstMove:
                    if isRooksFirstMove[0] == True:
                        if len(self.possibleMovesInDirection(id, 'W')) == 3:
                            if self.isInCheck(id) == False:
                                if not common_member(self.possibleMovesInDirection(id, 'W')[:2], self.allPossibleOpponentsMoves(id)):
                                    finalMovesList.append((self.pieces.blackKing.position[0][0], self.pieces.blackKing.position[0][1] - 2))
                    
                    elif isRooksFirstMove[1] == True:
                        if len(self.possibleMovesInDirection(id, 'E')) == 2:
                            if self.isInCheck(id) == False:
                                if not common_member(self.possibleMovesInDirection(id, 'E'), self.allPossibleOpponentsMoves(id)):
                                    finalMovesList.append((self.pieces.blackKing.position[0][0], self.pieces.blackKing.position[0][1] + 2))

            if self.possibleMovesInDirection(id, 'N') != None:movesList+= self.possibleMovesInDirection(id, 'N')
            if self.possibleMovesInDirection(id, 'E')!= None:movesList+= self.possibleMovesInDirection(id, 'E')
            if self.possibleMovesInDirection(id, 'S') != None:movesList+= self.possibleMovesInDirection(id, 'S')
            if self.possibleMovesInDirection(id, 'W') != None:movesList+= self.possibleMovesInDirection(id, 'W')
            if self.possibleMovesInDirection(id, 'NE') != None:movesList+= self.possibleMovesInDirection(id, 'NE')
            if self.possibleMovesInDirection(id, 'SE')!= None:movesList+= self.possibleMovesInDirection(id, 'SE')
            if self.possibleMovesInDirection(id, 'SW') != None:movesList+= self.possibleMovesInDirection(id, 'SW')
            if self.possibleMovesInDirection(id, 'NW') != None:movesList+= self.possibleMovesInDirection(id, 'NW')

            for square in squaresList:
                if square in movesList and square not in self.allPossibleOpponentsMoves(id):
                    finalMovesList.append(square)

            return finalMovesList
    
    def possiblePawnMoves(self, id):
        currentPosition = self.currentAllPiecePositions[id - 1]
        currentPosX = currentPosition[0]
        currentPosY = currentPosition[1]

        color = self.id2name[str(id)][0]
        
        listOfPossibleMoves = list()

        if color == 'W':

            enPassantAvailableAt = self.pieces.blackPawns.enPassantPawnPosition()

            if((currentPosX + 1, currentPosY) not in self.currentAllPiecePositions):
                listOfPossibleMoves.append((currentPosX + 1, currentPosY))

                if self.pieces.whitePawns.isFirstMove[self.pieces.whitePawns.ids.index(id)]:
                    if((currentPosX+2, currentPosY) not in self.currentAllPiecePositions):
                        listOfPossibleMoves.append((currentPosX + 2, currentPosY))

            for i in [-1, 1]:
                if(currentPosY + i in range(1, 9)):
                    if (currentPosX + 1,currentPosY + i) in self.currentBlackPiecePositions:
                        listOfPossibleMoves.append((currentPosX + 1, currentPosY + i))
            
            if enPassantAvailableAt != None:
                if enPassantAvailableAt == (currentPosX, currentPosY - 1):
                    listOfPossibleMoves.append((currentPosX + 1, currentPosY - 1))
                elif enPassantAvailableAt == (currentPosX, currentPosY + 1):
                    listOfPossibleMoves.append((currentPosX + 1, currentPosY + 1))

            return listOfPossibleMoves

        else:
            
            enPassantAvailableAt = self.pieces.whitePawns.enPassantPawnPosition()

            if((currentPosX - 1, currentPosY) not in self.currentAllPiecePositions):
                listOfPossibleMoves.append((currentPosX - 1, currentPosY))

                if self.pieces.blackPawns.isFirstMove[self.pieces.blackPawns.ids.index(id)]:
                    if((currentPosX - 2, currentPosY) not in self.currentAllPiecePositions):
                        listOfPossibleMoves.append((currentPosX - 2, currentPosY))

            for i in [-1, 1]:
                if(currentPosY + i in range(1, 9)):
                    if (currentPosX - 1,currentPosY + i) in self.currentWhitePiecePositions:
                        listOfPossibleMoves.append((currentPosX - 1, currentPosY + i))
            
            if enPassantAvailableAt != None:
                if enPassantAvailableAt == (currentPosX, currentPosY - 1):
                    listOfPossibleMoves.append((currentPosX - 1, currentPosY - 1))
                elif enPassantAvailableAt == (currentPosX, currentPosY + 1):
                    listOfPossibleMoves.append((currentPosX - 1, currentPosY + 1))

            return listOfPossibleMoves
    
    def possibleMovesInDirection(self, id, dir):
        currentPosition = self.currentAllPiecePositions[id - 1]
        currentPosX = currentPosition[0]
        currentPosY = currentPosition[1]

        color = self.id2name[str(id)][0]

        listOfPossibleMoves = []

        if dir == 'N':
            if color == 'W':
                for x in range(currentPosX + 1, 9):
                    if (x, currentPosY) in self.currentBlackPiecePositions:
                        listOfPossibleMoves.append((x, currentPosY))
                        break

                    if (x, currentPosY) in self.currentWhitePiecePositions:
                            if (x-1, currentPosY) == currentPosition:
                                break
                            if((x - 1, currentPosY) not in listOfPossibleMoves):listOfPossibleMoves.append((x - 1, currentPosY))
                            break
                    
                    if (x == 8):
                        listOfPossibleMoves.append((x, currentPosY))
                        break
                    
                    listOfPossibleMoves.append((x, currentPosY))

            else:
                for x in range(currentPosX + 1, 9):
                    if (x, currentPosY) in self.currentWhitePiecePositions:
                        listOfPossibleMoves.append((x, currentPosY))
                        break

                    if (x, currentPosY) in self.currentBlackPiecePositions:
                            if (x - 1, currentPosY) == currentPosition:
                                break
                            if((x - 1, currentPosY) not in listOfPossibleMoves):listOfPossibleMoves.append((x, currentPosY))
                            break

                    if (x == 8):
                        listOfPossibleMoves.append((x, currentPosY))
                        break

                    listOfPossibleMoves.append((x, currentPosY))

        elif dir == 'S':
            if color == 'W':
                for x in range(currentPosX - 1, 0, -1):
                    if (x, currentPosY) in self.currentBlackPiecePositions:
                        listOfPossibleMoves.append((x, currentPosY))
                        break

                    if (x, currentPosY) in self.currentWhitePiecePositions:
                            if (x + 1, currentPosY) == currentPosition:
                                break
                            if((x + 1, currentPosY) not in listOfPossibleMoves):listOfPossibleMoves.append((x + 1, currentPosY))
                            break
                    
                    if (x == 1):
                        listOfPossibleMoves.append((x, currentPosY))
                        break

                    listOfPossibleMoves.append((x, currentPosY))

            else:
                for x in range(currentPosX - 1, 0, -1):
                    if (x, currentPosY) in self.currentWhitePiecePositions:
                        listOfPossibleMoves.append((x, currentPosY))
                        break

                    if (x, currentPosY) in self.currentBlackPiecePositions:
                            if (x + 1, currentPosY) == currentPosition:
                                break
                            if((x + 1, currentPosY) not in listOfPossibleMoves):listOfPossibleMoves.append((x + 1, currentPosY))
                            break

                    if (x == 1):
                        listOfPossibleMoves.append((x, currentPosY))
                        break
                    
                    listOfPossibleMoves.append((x, currentPosY))

        elif dir == 'E':
            if color == 'W':
                for y in range(currentPosY + 1, 9):
                    if (currentPosX, y) in self.currentBlackPiecePositions:
                        listOfPossibleMoves.append((currentPosX, y))
                        break

                    if (currentPosX, y) in self.currentWhitePiecePositions:
                            if (currentPosX, y - 1) == currentPosition:
                                break
                            if((currentPosX, y - 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX, y - 1))
                            break
                    
                    if (y == 8):
                        listOfPossibleMoves.append((currentPosX, y))
                        break
                    
                    listOfPossibleMoves.append((currentPosX, y))

            else:
                for y in range(currentPosX + 1, 9):
                    if (currentPosX, y) in self.currentWhitePiecePositions:
                        listOfPossibleMoves.append((currentPosX, y))
                        break

                    if (currentPosX, y) in self.currentBlackPiecePositions:
                            if (currentPosX, y - 1) == currentPosition:
                                break
                            if((currentPosX, y - 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX, y - 1))
                            break

                    if (y == 8):
                        listOfPossibleMoves.append((currentPosX, y))
                        break
                        
                    listOfPossibleMoves.append((currentPosX, y))

        elif dir == 'W':
            if color == 'W':
                for y in range(currentPosY - 1, 0, -1):
                    if (currentPosX, y) in self.currentBlackPiecePositions:
                        listOfPossibleMoves.append((currentPosX, y))
                        break

                    if (currentPosX, y) in self.currentWhitePiecePositions:
                            if (currentPosX, y + 1) == currentPosition:
                                break
                            if((currentPosX, y + 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX, y + 1))
                            break
                    
                    if (y == 1):
                        listOfPossibleMoves.append((currentPosX, y))
                        break

                    listOfPossibleMoves.append((currentPosX, y))

            else:
                for y in range(currentPosY - 1, 0, -1):
                    if (currentPosX, y) in self.currentWhitePiecePositions:
                        listOfPossibleMoves.append((currentPosX, y))
                        break

                    if (currentPosX, y) in self.currentBlackPiecePositions:
                            if (currentPosX, y + 1) == currentPosition:
                                break
                            if((currentPosX, y + 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX, y + 1))
                            break

                    if (y == 1):
                        listOfPossibleMoves.append((currentPosX, y))
                        break

                    listOfPossibleMoves.append((currentPosX, y))

        elif dir == 'NE':
            if color == 'W':
                for i in range(1, 9 - max(currentPosX, currentPosY)):
                    if (currentPosX + i, currentPosY + i) in self.currentBlackPiecePositions and currentPosX + i in range(1, 9) and currentPosY + i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY + i))
                        break

                    if (currentPosX + i, currentPosY + i) in self.currentWhitePiecePositions  and currentPosX + i in range(1, 9) and currentPosY + i in range(1, 9):
                            if (currentPosX + i - 1, currentPosY + i - 1) == currentPosition:
                                break
                            if((currentPosX + i - 1, currentPosY + i - 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX + i - 1, currentPosY + i - 1))
                            break
                    
                    if (currentPosX + i, currentPosY + i) == (currentPosX + (8 - max(currentPosX, currentPosY) ), currentPosY + (8 - max(currentPosX, currentPosY)) ):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY + i))
                        break

                    listOfPossibleMoves.append((currentPosX + i, currentPosY + i))

            else:
                for i in range(1, 9 - max(currentPosX, currentPosY)):
                    if (currentPosX + i, currentPosY + i) in self.currentWhitePiecePositions and currentPosX + i in range(1, 9) and currentPosY + i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY + i))
                        break

                    if (currentPosX + i, currentPosY + i) in self.currentBlackPiecePositions  and currentPosX + i in range(1, 9) and currentPosY + i in range(1, 9):
                            if (currentPosX + i - 1, currentPosY + i - 1) == currentPosition:
                                break
                            if((currentPosX + i - 1, currentPosY + i - 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX + i - 1, currentPosY + i - 1))
                            break
                    
                    if (currentPosX + i, currentPosY + i) == (currentPosX + (8 - max(currentPosX, currentPosY) ), currentPosY + (8 - max(currentPosX, currentPosY)) ):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY + i))
                        break
                    
                    listOfPossibleMoves.append((currentPosX + i, currentPosY + i))
                    
        elif dir == 'SW':
            if color == 'W':
                for i in range(1, 1 + min(currentPosX - 1, currentPosY - 1)):
                    if (currentPosX - i, currentPosY - i) in self.currentBlackPiecePositions and currentPosX - i in range(1, 9) and currentPosY - i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY - i))
                        break

                    if (currentPosX - i, currentPosY - i) in self.currentWhitePiecePositions  and currentPosX - i in range(1, 9) and currentPosY - i in range(1, 9):
                            if (currentPosX - i + 1, currentPosY - i + 1) == currentPosition:
                                break
                            if((currentPosX - i + 1, currentPosY - i + 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX - i + 1, currentPosY - i + 1))
                            break
                    
                    if (currentPosX - i, currentPosY - i) == (currentPosX - (min(currentPosX - 1, currentPosY - 1) ), currentPosY - (min(currentPosX - 1, currentPosY - 1)) ):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY - i))
                        break

                    listOfPossibleMoves.append((currentPosX - i, currentPosY - i))

            else:
                for i in range(1, 1 + min(currentPosX - 1, currentPosY - 1)):
                    if (currentPosX - i, currentPosY - i) in self.currentWhitePiecePositions and currentPosX - i in range(1, 9) and currentPosY - i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY - i))
                        break

                    if (currentPosX - i, currentPosY - i) in self.currentBlackPiecePositions  and currentPosX - i in range(1, 9) and currentPosY - i in range(1, 9):
                            if (currentPosX - i + 1, currentPosY - i + 1) == currentPosition:
                                break
                            if((currentPosX - i + 1, currentPosY - i + 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX - i + 1, currentPosY - i + 1))
                            break
                    
                    if (currentPosX - i, currentPosY - i) == (currentPosX - (min(currentPosX - 1, currentPosY - 1) ), currentPosY - (min(currentPosX - 1, currentPosY - 1)) ):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY - i))
                        break
                    
                    listOfPossibleMoves.append((currentPosX - i, currentPosY - i))

        elif dir == 'NW':
            if color == 'W':
                for i in range(1, 1 + min(8 - currentPosX, currentPosY - 1)):
                    if (currentPosX + i, currentPosY - i) in self.currentBlackPiecePositions and currentPosX + i in range(1, 9) and currentPosY - i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY - i))
                        break

                    if (currentPosX + i, currentPosY - i) in self.currentWhitePiecePositions  and currentPosX + i in range(1, 9) and currentPosY - i in range(1, 9):
                            if (currentPosX + i - 1, currentPosY - i + 1) == currentPosition:
                                break
                            if((currentPosX + i - 1, currentPosY - i + 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX + i - 1, currentPosY - i + 1))
                            break
                    
                    if (currentPosX + i, currentPosY - i) == (currentPosX + min(8 - currentPosX, currentPosY - 1) , currentPosY - min(8 - currentPosX, currentPosY - 1)):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY - i))
                        break

                    listOfPossibleMoves.append((currentPosX + i, currentPosY - i))

            else:
                for i in range(1, 1 + min(8 - currentPosX, currentPosY - 1)):
                    if (currentPosX + i, currentPosY - i) in self.currentWhitePiecePositions and currentPosX + i in range(1, 9) and currentPosY - i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY - i))
                        break

                    if (currentPosX + i, currentPosY - i) in self.currentBlackPiecePositions  and currentPosX + i in range(1, 9) and currentPosY - i in range(1, 9):
                            if (currentPosX + i - 1, currentPosY - i + 1) == currentPosition:
                                break
                            if((currentPosX + i - 1, currentPosY - i + 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX + i - 1, currentPosY - i + 1))
                            break
                    
                    if (currentPosX + i, currentPosY - i) == (currentPosX + min(8 - currentPosX, currentPosY - 1), currentPosY - min(8 - currentPosX, currentPosY - 1)):
                        listOfPossibleMoves.append((currentPosX + i, currentPosY - i))
                        break
                        
                    listOfPossibleMoves.append((currentPosX + i, currentPosY - i))

        elif dir == 'SE':
            if color == 'W':
                for i in range(1, 1 + min(currentPosX - 1, 8 - currentPosY)):
                    if (currentPosX - i, currentPosY + i) in self.currentBlackPiecePositions and currentPosX - i in range(1, 9) and currentPosY + i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY + i))
                        break

                    if (currentPosX - i, currentPosY + i) in self.currentWhitePiecePositions  and currentPosX - i in range(1, 9) and currentPosY + i in range(1, 9):
                            if (currentPosX - i + 1, currentPosY + i - 1) == currentPosition:
                                break
                            if((currentPosX - i + 1, currentPosY + i - 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX - i + 1, currentPosY + i - 1))
                            break
                    
                    if (currentPosX - i, currentPosY + i) == (currentPosX - (min(currentPosX - 1, 8 - currentPosY) ), currentPosY + (min(currentPosX - 1, 8 - currentPosY)) ):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY + i))
                        break

                    listOfPossibleMoves.append((currentPosX - i, currentPosY + i))

            else:
                for i in range(1, 1 + min(currentPosX - 1, 8 - currentPosY)):
                    if (currentPosX - i, currentPosY + i) in self.currentWhitePiecePositions and currentPosX - i in range(1, 9) and currentPosY + i in range(1, 9):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY + i))
                        break

                    if (currentPosX - i, currentPosY + i) in self.currentBlackPiecePositions  and currentPosX - i in range(1, 9) and currentPosY + i in range(1, 9):
                            if (currentPosX - i + 1, currentPosY + i - 1) == currentPosition:
                                break
                            if((currentPosX - i + 1, currentPosY + i - 1) not in listOfPossibleMoves):listOfPossibleMoves.append((currentPosX - i + 1, currentPosY + i - 1))
                            break
                    
                    if (currentPosX - i, currentPosY + i) == (currentPosX - (min(currentPosX - 1, 8 - currentPosY) ), currentPosY + (min(currentPosX - 1, 8 - currentPosY)) ):
                        listOfPossibleMoves.append((currentPosX - i, currentPosY + i))
                        break                    
                        
                    listOfPossibleMoves.append((currentPosX - i, currentPosY + i))
                    
        
        return listOfPossibleMoves

    def changeTurn(self):
        if self.turn == "W":
            self.turn = "B"
        else:
            self.turn = "W"
        return 0

    def showTurn(self):
        print(self.turn)
        return 0

    def nextID(self):
        ID = self.ids[-1] + 1
        return ID

    def allPossibleOpponentsMoves(self, id):
        piece = self.id2name[str(id)]
        movesList = list()

        if piece[0] == 'W':
            for ID in self.blackIDs:
                movesList += self.listOfAllPossibleMoves(ID)
            return movesList

        else:
            for ID in self.whiteIDs:
                movesList += self.listOfAllPossibleMoves(ID)
            return movesList
    
    def allPossibleSelfMoves(self, id):
        piece = self.id2name[str(id)]
        movesList = list()

        if piece[0] == 'W':
            for ID in self.whiteIDs:
                movesList += self.listOfAllPossibleMoves(ID)
            return movesList

        else:
            for ID in self.blackIDs:
                movesList += self.listOfAllPossibleMoves(ID)
            return movesList

    def isInCheck(self, id):
        currentKingPos = self.currentAllPiecePositions[id - 1]
        oppMovesList = self.allPossibleOpponentsMoves(id)
        if currentKingPos in oppMovesList:
            return True
        else:
            return False

    def isPinnedToKing(self, id):
        pass

    def isCheckMated(self, id):
        if self.isInCheck(id) and self.turn == self.id2name[str(id)][0] and self.listOfAllPossibleMoves(id) == []:
            return True
        else:
            return False

    def isStaleMated(self, id):
        if self.isInCheck(id) == False and self.turn == self.id2name[str(id)][0] and self.listOfAllPossibleMoves(id) == [] and self.allPossibleSelfMoves(id) == []:
            return True
        else:
            return False

digitalChessBoard = chessboard(pieces)
v = digitalChessBoard.allPossibleSelfMoves(5)
print(v)
print(len(v))
# digitalChessBoard.showTurn()
# digitalChessBoard.changeTurn()
# digitalChessBoard.showTurn()
