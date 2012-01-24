import argparse
import time
from inspect import isfunction

from maze import Maze
from io import Canvas, user_pressed_escape
import generators

def _build_parser():
    parser = argparse.ArgumentParser(
        description='visualize maze generation algorithms'
    )
    parser.add_argument('--algorithm', 
        required=True,
        choices=[f for f in dir(generators) 
                         if isfunction(getattr(generators, f))],
        help='algorithm to use'
    )
    parser.add_argument('--speed',
        type=int,
        default=100,
        metavar='ms',
        help='visualization speed (milliseconds per edge)'
    )
    parser.add_argument('--width', 
        type=int, 
        default=10, 
        metavar='columns',
        help='maze width'
    )
    parser.add_argument('--height',
        type=int,
        default=10,
        metavar='rows',
        help='maze height'
    )
    parser.add_argument('--cellsize', 
        type=int, 
        default=50, 
        metavar='pixels',
        help='cell size'
    )
    return parser

if __name__ == '__main__':
    args = _build_parser().parse_args()
    maze = Maze(args.width, args.height)
    canvas = Canvas(args.width, args.height, args.cellsize)
    generator = getattr(generators, args.algorithm)

    for node in maze.graph.nodes():
        for neighbor in maze.neighbors(node):
            maze.draw_line_between(canvas, node, neighbor, color=(0, 0, 0))

    for c1, c2 in generator(maze):
        maze.connect(c1, c2)
        maze.draw_line_between(canvas, c1, c2)
        if user_pressed_escape():
            break
        time.sleep(args.speed / 1000.0)
