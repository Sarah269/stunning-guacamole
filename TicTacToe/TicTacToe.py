############################################################
# Python Game:  Tic Tac Toe                                #
# Reference: 12 Beginner Python Projects. freeCodeCamp.org #
# Date: August 2024                                        #
# Files: TicTacToe.py, player.py                           #
############################################################

import math
import time
from player import * 


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @ staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #    # ['x', 'x', 'o'] --> [(0,'x'), (1,'x'), (2,'o')]
        #    if spot == ' ':
        #        moves.append(i)
        #  return moves

    def empty_squares(self):
        return ' ' in self.board #empty squares will return a boolean
    
    def num_empty_squares(self):
        return self.board.count(' ') # count number of spaces in the board

    def make_moves(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, then return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
         
    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3) # divide by 3 round down
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([spot == letter for spot in row]):
            # all values in row have the same value 
            return True
           
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([spot == letter for spot in column]):
            # all values in column have the same value 
            return True

        # check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        # there are the only moves possible to win a diagonal
     
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
         
            # print('diag1', diagonal1)
            if all([spot == letter for spot in diagonal1]):
                # all values in diagonal have the same value 
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            # print('diag2', diagonal2)
            if all([spot == letter for spot in diagonal2]):
                # all values in diagonal have the same value 
                return True
         # if all checks fail, no winner  
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    #  (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
     
        #let's define a function to make a move!
        if game.make_moves(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square} ')
                game.print_board()
                print(' ') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game

            
            # after we made out move, we need to alternate players  
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game:
        print('It ''s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True) 
                