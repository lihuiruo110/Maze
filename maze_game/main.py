import curses
from maze_game.game import main  # ← game.py의 main 함수 가져오기

def start_game():
    curses.wrapper(main)
