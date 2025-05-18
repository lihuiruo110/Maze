from setuptools import setup, find_packages

setup(
    name="random_maze_game",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "maze-game = maze_game.main:start_game"
        ]
    },
    author="lihuiruo110",
    description="터미널 기반 랜덤 미로 게임 (curses)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
)
