import curses
import random
import time
from collections import deque

WIDTH, HEIGHT = 15, 15

# ... generate_maze, has_path, generate_valid_maze, place_traps, draw_maze, star_rating 함수들 그대로 ...

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stage = 1
    # ... 나머지 게임 루프 그대로 ...

def start_game():
    curses.wrapper(main)
