import numpy as np
from main import *

main = Main()

def Minimax (board ,depth ,is_maximizing) :
    if main.check_winner(board , main.player):
        return 100
    if main.check_winner(board , main.player) :
        return -100

        
