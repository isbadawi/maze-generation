import random

def aldous_broder(maze):
    def _connected(maze, cell):
        return any(maze.connected(cell, n) for n in maze.neighbors(cell))
    start = random.choice(maze.graph.nodes())
    current = start
    while not all(_connected(maze, cell) for cell in maze.graph.nodes()):
        dest = random.choice(maze.neighbors(current))
        if not _connected(maze, dest):
            yield (current, dest)
        current = dest
