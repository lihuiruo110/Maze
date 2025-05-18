from setuptools import setup

setup(
    name='random_maze_game',
    version='0.1',
    description='Terminal-based infinite random maze game with traps and scoring',
    author='lihuiruo110',
    py_modules=['maze'],
    entry_points={
        'console_scripts': [
            'maze-game = maze:main',
        ],
    },
    install_requires=[
        # curses는 표준 라이브러리라 별도 설치 불필요
        # 윈도우는 windows-curses 설치 필요
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
