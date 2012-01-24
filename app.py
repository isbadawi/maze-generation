import argparse

from maze import Maze
from drawing.canvas import Canvas

def _build_parser():
    parser = argparse.ArgumentParser(
        description='visualize maze generation algorithms'
    )
    parser.add_argument('--width', 
        type=int, 
        default=10, 
        help='maze width'
    )
    parser.add_argument('--height',
        type=int,
        default=10,
        help='maze height'
    )
    parser.add_argument('--cellsize', 
        type=int, 
        default=50, 
        help='cell size'
    )
    return parser

if __name__ == '__main__':
    args = _build_parser().parse_args()
    maze = Maze(args.width, args.height)
    canvas = Canvas(args.width, args.height, args.cellsize)
    for cell in maze.neighbors((0, 0)):
        maze.connect(cell, (0, 0))
    maze.connect((0, 1), (1, 1))
    maze.draw(canvas)
