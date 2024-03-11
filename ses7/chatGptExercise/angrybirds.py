import random
import os

class Pig:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Bird:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Workspace:
    
    @staticmethod
    def make_move(board, direction):
        if direction == 'U':
            if board.bird.row > 0:
                board.bird.row -1
        elif direction == 'D':
            if board.bird.row < board.rows:
                board.bird.row += 1
        elif direction == 'L':
            if board.bird.column > 0:
                board.bird.column -= 1
        elif direction == 'R':
            if board.bird.column < board.columns - 1:
                board.bird.column += 1
        else:
            print("Invalid direction")




class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.pig = None
        self.bird = None 

    def print_board(self):
        print("============= ANGRY BIRDS ==============")
        for row in range(self.rows):
            for col in range(self.columns):
                if self.pig and self.pig.row == row and self.pig.column == col:
                    print("P", end=" ")  # Print P for pig
                elif self.bird and self.bird.row == row and self.bird.column == col:
                    print("B", end=" ")  # Print B for bird
                else:
                    print("*", end=" ")  # Print * for empty space
            print()

    def place_pig(self):
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        self.pig = Pig(row, column)

    def place_bird(self):
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        self.bird = Bird(row, column)

class Game:

    def run(self):
        self.board = Board(10, 10)
        self.board.place_pig()
        self.board.place_bird()
        self.board.print_board()

        while True:
            direction = input("Move (U/D/L/R): ").strip().upper()
            if direction in ["U", "D", "L", "R"]:
                Workspace.make_move(self.board, direction)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.board.print_board()
            else:
                print("GAME OVER")
                break
        
            if self.board.bird.row == self.board.pig.row and self.board.bird.column == self.board.pig.column:
                print("YOU'VE CAUGHT THE PIG")
                break


game = Game()
game.run()
