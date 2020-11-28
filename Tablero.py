# import pygame
import sys


class Game:

    # Inicia el juego

    def __init__(self, player1=0, player2=0):
        if player1 == 0:
            player_name1: str = input("Nombre jugador 1: ")
            self.player1 = Jugador(player_name1)
        else:
            self.player1 = player1

        if player2 == 0:
            player_name2 = input("Nombre jugador 2: ")
            self.player2 = Jugador(player_name2)
        else:
            self.player2 = player2

        self.board = Board()

    def play(self):
        self.board.display()
        gameOver = False
        winner = -1

        while not gameOver:  # Bucle
            # Turno jugador 1
            move = self.player1.getMove(self.board)
            (isValid, error) = self.board.validMove(move, 1)
            while not isValid:
                self.board.display()
                print(error)
                move = self.player1.getMove(self.board)
                (isValid, error) = self.board.validMove(move, 1)
            self.board.update(move, 1)
            self.board.display()

            # Turno jugador 2
            move = self.player2.getMove(self.board)
            (isValid, error) = self.board.validMove(move, 2)
            while not isValid:
                self.board.display()
                print(error)
                move = self.player2.getMove(self.board)
                (isValid, error) = self.board.validMove(move, 2)
            self.board.update(move, 2)
            self.board.display()

            gameOver, winner = self.board.isGameOver()

        # Ganador

        print("GAME OVER")
        if winner == 1:
            print(self.player1.name + " ganó")
        else:
            print(self.player2.name + " ganó")


class Jugador:
    def __init__(self, name):
        self.name = name

    def getMove(self, board):
        return input("Turno de " + self.name + ", ingresa movimiento: ")

class Enemigo:
    def __init__(self, name):
        self.name = "Bot"





class Board:

    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0]
        ]

        self.wallsVertical = [
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 1
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 2
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 3
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 4
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 5
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 6
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 7
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 8
            [0, 0, 0, 0, 0, 0, 0, 0], # columna 9
        ]

        self.wallsHorizontal = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.moveDictionary = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
            "W": 10,
        }

    # Coordenadas del jugador
    def getPlayerPosition(self, player):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == player:
                    return i, j
        return -1, -1

    # numero de murallas no jugadas
    def wallsRemaining(self, player):
        count = 0
        for row in self.wallsVertical:
            for cell in row:
                if cell == player:
                    count += 1
        for row in self.wallsHorizontal:
            for cell in row:
                if cell == player:
                    count += 1
        return 8 - count

    # Validar movimiento
    def validMove(self, move, player):
        move = move.upper()
        if not self.validFormat(move):
            return False, "formato inválido"
        else:
            return self.legalMove(move, player)

    # Movimientos legales o válidos
    def validFormat(self, move):
        rows = "123456789"  # Mediante el teclado se hace posible el movimiento
        columns = "ABCDEFGHI"
        if len(move) == 4:
            # WALL
            if move[0] in rows and move[1] in rows and move[2] in columns and move[3] in columns:
                if int(move[0]) + 1 == int(move[1]) and int(self.moveDictionary.get(move[2])) + 1 == int(
                        self.moveDictionary.get(move[3])):
                    return True
                else:
                    return False
            if move[0] in columns and move[1] in columns and move[2] in rows and move[3] in rows:
                if int(move[2]) + 1 == int(move[3]) and int(self.moveDictionary.get(move[0])) + 1 == int(
                        self.moveDictionary.get(move[1])):
                    return True
                else:
                    return False

            #if move[9] in columns:
                #input("Ingresa el lugar de las murallas: ")

        elif len(move) == 2:
            # MOVEMENT
            if move[0] in columns and move[1] in rows:
                return True
            else:
                return False
        else:
            return False

    # Validar movimientos
    def legalMove(self, move, player):
        (isLegal, error) = True, ""
        if len(move) == 4:
            # Muralla
            if move[0] in self.moveDictionary.keys():
                # VERTICAL
                i = self.moveDictionary.get(move[0])
                j = int(move[2]) - 1
                # Valida si existen murallas
                if self.wallsVertical[i][j] > 0:
                    return False, ""
                # valida si cruza muralla
                if self.wallsHorizontal[j][i] > 0:
                    return False, ""
                else:
                    # Validar superposicion
                    if j == 0:
                        if self.wallsVertical[i][j + 1] > 0:
                            return False, ""
                    elif j == 7:
                        if self.wallsVertical[i][j - 1] > 0:
                            return False, ""
                    else:
                        if self.wallsVertical[i][j - 1] > 0 or self.wallsVertical[i][j + 1] > 0:
                            return False, ""

            else:
                # Horizontal
                i = int(move[0]) - 1
                j = self.moveDictionary.get(move[2])

                # Pared
                if self.wallsHorizontal[i][j] > 0:
                    return False, ""
                # check if crossing
                elif self.wallsVertical[j][i] > 0:
                    return False, ""
                else:
                    # Comprobar que no haya superposición
                    if j == 0:
                        if self.wallsHorizontal[i][j + 1] > 0:
                            return False, ""
                    elif j == 7:
                        if self.wallsHorizontal[i][j - 1] > 0:
                            return False, ""
                    else:
                        if self.wallsHorizontal[i][j - 1] > 0 or self.wallsHorizontal[i][j + 1] > 0:
                            return False, ""

            # Valida muralla
            if self.wallBlocksPlayerIn(move, 1):
                return False, ""
            if self.wallBlocksPlayerIn(move, 2):
                return False, ""

        if len(move) == 2:

            # Adyacencia
            (x, y) = self.getPlayerPosition(player)
            i = int(move[1]) - 1
            j = self.moveDictionary.get(move[0])
            if not (i, j) in self.getAdjacentSquares(x, y):
                if self.legalJump(i, j, player):
                    return True, ""
                else:
                    return False, ""
            else:
                # check walls
                (isLegal, error) = self.isntBlocked(i, j, x, y)
        return isLegal, error

    # Valida si no hay enemigos cerca para salto
    def legalJump(self, i, j, player):
        (x, y) = self.getPlayerPosition(player)
        opponent = 1
        if player == 1:
            opponent = 2
        (opX, opY) = self.getPlayerPosition(opponent)
        if (opX, opY) in self.getAdjacentSquares(x, y):
            if self.isntBlocked(opX, opY, x, y)[0]:
                if (i, j) in self.getAdjacentSquares(opX, opY):
                    if self.isntBlocked(i, j, opX, opY)[0]:
                        return True
        return False

    # Comprueba si un muro dado bloqueará al jugador
    def wallBlocksPlayerIn(self, wall, player):
        self.update(wall, player)
        (x, y) = self.getPlayerPosition(player)
        reachableSquares = self.getReachableSquares(x, y, [(x, y)])
        if player == 1:
            for (i, j) in reachableSquares:
                if i == 8:
                    self.removeWall(wall)
                    return False
        if player == 2:
            for (i, j) in reachableSquares:
                if i == 0:
                    self.removeWall(wall)
                    return False
        self.removeWall(wall)
        return True

    # Cuadrados a los que el jugador puede moverse
    def getReachableSquares(self, x, y, visited):
        adjacents = self.getAdjacentSquares(x, y)
        reachableAdjacents = []
        for (i, j) in adjacents:
            (isntBlocked, error) = self.isntBlocked(i, j, x, y)
            if isntBlocked and not (i, j) in visited:
                reachableAdjacents.append((i, j))
        visited = visited + reachableAdjacents
        for (i, j) in reachableAdjacents:
            visited = self.getReachableSquares(i, j, visited)
        return visited

    # Cuadrados adyacentes como coordenadas xy
    def getAdjacentSquares(self, x, y):
        allPossible = \
            [
                (x + 1, y),  # Arriba
                (x - 1, y),  # Abajo
                (x, y + 1),  # Derecha
                (x, y - 1)  # Izquierda
            ]
        adjacentSquares = []
        for (i, j) in allPossible:
            if not (i < 0 or i > 8 or j < 0 or j > 8):
                adjacentSquares.append((i, j))
        return adjacentSquares

    # Validaciones de saltos y movimiento
    def isntBlocked(self, i, j, x, y):
        if j == y:
            if i == x + 1:
                # arriba
                if y == 0:
                    if self.wallsHorizontal[x][y] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                elif y == 8:
                    if (self.wallsHorizontal[x][y - 1] > 0):
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                else:
                    if self.wallsHorizontal[x][y] > 0 or self.wallsHorizontal[x][y - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
            elif i == x - 1:
                # abajooo
                if y == 0:
                    if self.wallsHorizontal[x - 1][y] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                elif (y == 8):
                    if self.wallsHorizontal[x - 1][y - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                else:
                    if self.wallsHorizontal[x - 1][y] > 0 or self.wallsHorizontal[x - 1][y - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
            else:
                return False, ""
        elif i == x:
            if j == y + 1:
                # derecha
                if x == 0:
                    if self.wallsVertical[y][x] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                elif x == 8:
                    if self.wallsVertical[y][x - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                else:
                    if self.wallsVertical[y][x] > 0 or self.wallsVertical[y][x - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
            elif j == y - 1:
                # izquierda
                if x == 0:
                    if (self.wallsVertical[y - 1][x] > 0):
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                elif x == 8:
                    if self.wallsVertical[y - 1][x - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
                else:
                    if self.wallsVertical[y - 1][x] > 0 or self.wallsVertical[y - 1][x - 1] > 0:
                        return False, "no puede ir a través de la pared"
                    else:
                        return True, ""
            else:
                return False, ""
        else:
            return False, ""

    # Actualiza tablero si el movimiento es legal
    def update(self, move, player):
        move = move.upper()
        if len(move) > 2:

            if move[0] in self.moveDictionary.keys():
                # vertical
                i = self.moveDictionary.get(move[0])
                j = int(move[2]) - 1
                self.wallsVertical[i][j] = player

            else:
                # horizontal
                i = int(move[0]) - 1
                j = self.moveDictionary.get(move[2])
                self.wallsHorizontal[i][j] = player

        else:
            # Movimiento
            (x, y) = self.getPlayerPosition(player)
            self.board[x][y] = 0
            i = int(move[1]) - 1
            j = self.moveDictionary.get(move[0])
            self.board[i][j] = player

    # Remover barrera
    def removeWall(self, wall):
        wall = wall.upper()
        if wall[0] in self.moveDictionary.keys():
            # vertical
            i = self.moveDictionary.get(wall[0])
            j = int(wall[2]) - 1
            self.wallsVertical[i][j] = 0

        else:
            # horizontal
            i = int(wall[0]) - 1
            j = self.moveDictionary.get(wall[2])
            self.wallsHorizontal[i][j] = 0

    # Verificar si alguien ha ganado
    def isGameOver(self):
        (x1, y1) = self.getPlayerPosition(1)
        if x1 == 8:
            return True, 1
        (x2, y2) = self.getPlayerPosition(2)
        if x2 == 0:
            return True, 2
        return False, -1

    # Dibujo del tablero
    def display(self):

        sys.stdout.write("               _____   _____   _____   _____   _____   _____   _____   _____   _____\n")
        for i in range(8):
            self.displayRow(9 - i)
            self.displayGap(8 - i)
        self.displayRow(1)
        sys.stdout.write("                 A       B       C       D       E       F       G       H       I\n")

    # Tablero
    def displayRow(self, rowNumber):
        self.displayRowHelper(rowNumber, False, "|     |")
        self.displayRowHelper(rowNumber, True, "|     |")
        self.displayRowHelper(rowNumber, False, "|_____|")

    # Tablero
    def displayRowHelper(self, rowNumber, center, cellString):
        if center:
            sys.stdout.write("            " + str(rowNumber) + " ")
        else:
            sys.stdout.write("              ")

        for i in range(9):
            if rowNumber == 9:
                if self.wallsVertical[i][rowNumber - 2] > 0:
                    if center and self.board[rowNumber - 1][i] == 1:
                        sys.stdout.write("|  1  |W")
                    elif center and self.board[rowNumber - 1][i] == 2:
                        sys.stdout.write("|  2  |W")
                    else:
                        sys.stdout.write(cellString + "W")
                else:
                    if center and self.board[rowNumber - 1][i] == 1:
                        sys.stdout.write("|  1  | ")
                    elif center and self.board[rowNumber - 1][i] == 2:
                        sys.stdout.write("|  2  | ")
                    else:
                        sys.stdout.write(cellString + " ")
            elif rowNumber == 1:
                if self.wallsVertical[i][rowNumber - 1] > 0:
                    if center and self.board[rowNumber - 1][i] == 1:
                        sys.stdout.write("|  1  |W")
                    elif center and self.board[rowNumber - 1][i] == 2:
                        sys.stdout.write("|  2  |W")
                    else:
                        sys.stdout.write(cellString + "W")
                else:
                    if center and self.board[rowNumber - 1][i] == 1:
                        sys.stdout.write("|  1  | ")
                    elif center and self.board[rowNumber - 1][i] == 2:
                        sys.stdout.write("|  2  | ")
                    else:
                        sys.stdout.write(cellString + " ")
            else:
                if self.wallsVertical[i][rowNumber - 1] > 0 or self.wallsVertical[i][rowNumber - 2] > 0:
                    if center and self.board[rowNumber - 1][i] == 1:
                        sys.stdout.write("|  1  |W")
                    elif center and self.board[rowNumber - 1][i] == 2:
                        sys.stdout.write("|  2  |W")
                    else:
                        sys.stdout.write(cellString + "W")
                else:
                    if center and self.board[rowNumber - 1][i] == 1:
                        sys.stdout.write("|  1  | ")
                    elif center and self.board[rowNumber - 1][i] == 2:
                        sys.stdout.write("|  2  | ")
                    else:
                        sys.stdout.write(cellString + " ")
        sys.stdout.write("\n")

    # Tablero
    def displayGap(self, gapNumber):
        if (self.wallsRemaining(1) > 8 - gapNumber):
            sys.stdout.write(" WWWWWWWWWWWWW")
        else:
            sys.stdout.write("              ")

        i = 0
        while i < 8:
            if self.wallsHorizontal[gapNumber - 1][i] == 1 or self.wallsHorizontal[gapNumber - 1][i] == 2:
                sys.stdout.write(" WWWWWWWWWWWWW ")
                i += 2
            else:
                sys.stdout.write(" _____ ")
                i += 1
            if self.wallsVertical[i - 1][gapNumber - 1] > 0:
                sys.stdout.write("W")
            else:
                sys.stdout.write(" ")
        if i == 8:
            sys.stdout.write(" _____ ")

        if (self.wallsRemaining(2) > 8 - gapNumber):
            sys.stdout.write("WWWWWWWWWWWWW\n")
        else:
            sys.stdout.write("\n")


g = Game()
g.play()
