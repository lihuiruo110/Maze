import curses
import random
import time
from collections import deque

WIDTH, HEIGHT = 15, 15

def generate_maze(w, h):
    maze = [[1]*w for _ in range(h)]

    def carve(x, y):
        maze[y][x] = 0
        directions = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 < nx < w-1 and 0 < ny < h-1 and maze[ny][nx] == 1:
                maze[ny - dy//2][nx - dx//2] = 0
                carve(nx, ny)

    carve(1,1)
    maze[0][1] = 0      # 입구
    maze[h-1][w-2] = 0  # 출구
    return maze

def has_path(maze, start, end):
    w, h = len(maze[0]), len(maze)
    visited = [[False]*w for _ in range(h)]
    queue = deque([start])
    visited[start[1]][start[0]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and maze[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
    return False

def generate_valid_maze(w, h):
    while True:
        maze = generate_maze(w, h)
        if has_path(maze, (1,0), (w-2, h-1)):
            return maze

def place_traps(maze, trap_count):
    traps = set()
    empty_cells = [(x,y) for y,row in enumerate(maze) for x,cell in enumerate(row) if cell == 0]
    # 입구, 출구 제외
    empty_cells = [(x,y) for (x,y) in empty_cells if not ((x==1 and y==0) or (x==WIDTH-2 and y==HEIGHT-1))]
    traps = set(random.sample(empty_cells, min(trap_count, len(empty_cells))))
    return traps

def draw_maze(stdscr, maze, px, py, traps, stage, elapsed, stars):
    stdscr.clear()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            ch = "  "
            if (x, y) == (px, py):
                ch = "😃"
            elif (x, y) in traps:
                ch = "☠️"
            elif cell == 1:
                ch = "🧱"
            stdscr.addstr(y, x*2, ch)
    stdscr.addstr(HEIGHT, 0, f"Stage: {stage}  Time: {elapsed:.1f}s  Stars: {'★'*stars}{'☆'*(3-stars)}")
    stdscr.addstr(HEIGHT+1, 0, "Move with arrow keys. Press 'q' to quit.")
    stdscr.refresh()

def star_rating(time_taken):
    if time_taken < 30:
        return 3
    elif time_taken < 60:
        return 2
    else:
        return 1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stage = 1

    while True:
        maze = generate_valid_maze(WIDTH, HEIGHT)
        traps = place_traps(maze, trap_count=10)
        px, py = 1, 0  # 입구 위치
        start_time = time.time()
        stars = 0

        while True:
            elapsed = time.time() - start_time
            stars = star_rating(elapsed)
            draw_maze(stdscr, maze, px, py, traps, stage, elapsed, stars)

            try:
                key = stdscr.getch()
            except:
                key = -1

            if key == -1:
                time.sleep(0.05)
                continue

            if key == ord('q'):
                stdscr.nodelay(False)
                stdscr.clear()
                stdscr.addstr(0,0,f"Quit! You reached stage {stage}. Thanks for playing.")
                stdscr.refresh()
                time.sleep(2)
                return

            nx, ny = px, py
            if key == curses.KEY_UP:
                ny -= 1
            elif key == curses.KEY_DOWN:
                ny += 1
            elif key == curses.KEY_LEFT:
                nx -= 1
            elif key == curses.KEY_RIGHT:
                nx += 1

            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny][nx] == 0:
                px, py = nx, ny

            # 함정 밟으면 죽음
            if (px, py) in traps:
                stdscr.nodelay(False)
                stdscr.clear()
                stdscr.addstr(0, 0, f"You stepped on a trap! Game Over at stage {stage}.")
                stdscr.addstr(2, 0, "Press any key to exit.")
                stdscr.refresh()
                stdscr.getch()
                return

            # 출구 도착 시 다음 스테이지
            if (px, py) == (WIDTH-2, HEIGHT-1):
                stage += 1
                break

if __name__ == "__main__":
    curses.wrapper(main)
