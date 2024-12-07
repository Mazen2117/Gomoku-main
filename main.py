import pygame
import sys
import numpy as np

class Main:
    def __init__(self ,board_size):
        self.board_size = board_size
        self.board=np.zeros((board_size,board_size), dtype=int)
        self.player=1 #1 plays first(Black for GUI)


    def place_stone(board, row, col, player):
        """Place a stone at the clicked position."""
        if row < 0 or row >= len(board) or col < 0 or col >= len(board):
            return False
        
        if board[row][col] != 0:
            return False

        if board[row][col] == 0:  # 0 means empty
            board[row][col] = player
            return True

    def make_move(self, row, col):
        self.board[row][col]=self.player 

    def check_winner(self, player):
        """Check if the given player has won."""
        """The Following For Checking direct Horizontally and Vertically"""
        for x in range(self.board_size):
            for y in range (self.board_size-4) :
                if all(self.board[x][y+z] == player for z in range(5)):
                    return True

                if all(self.board[y+z][x] == player for z in range(5)):
                    return True
        
        """The Following For Checking Diagonally"""
        for x in range(self.board_size - 4):
                for y in range(self.board_size - 4):
                    if all(self.board[x+z][y+z] == player for z in range(5)):
                        return True
                    if all(self.board[x+z][y+4-z] == player for z in range(5)):
                        return True