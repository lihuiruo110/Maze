from setuptools import setup

setup(
    name='random_maze_game',
    version='0.1',
    description='Terminal-based infinite random maze game with traps and scoring',
    author='lihuiruo110',
    py_modules=['maze_game'],
    entry_points={
        'console_scripts': [
            'maze-game = maze_game:main',
        ],
    },
)
