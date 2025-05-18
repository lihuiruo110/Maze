import curses
# ... 위에 기존 게임 로직 그대로 ...

def main(stdscr):
    curses.curs_set(0)
    # 나머지 내용 동일 ...

def start_game():
    curses.wrapper(main)
