import argparse
import threading
from inspect import isfunction

from maze import Maze, generators
from maze.visualizers import visualize_algorithm
from io.canvas import Canvas
from io.input import user_wants_to_stop

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
    thread = threading.Thread(
        target=visualize_algorithm, 
        args=(maze, canvas, generator, args.speed / 1000.0)
    )
    thread.daemon = True
    thread.start()
    while not user_wants_to_stop():
        pass
