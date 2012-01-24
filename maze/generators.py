import random

def aldous_broder(maze):
    start = random.choice(maze.graph.nodes())
    current = start
    while not all(maze.reachable(cell) for cell in maze.graph.nodes()):
        dest = random.choice(maze.neighbors(current))
        if not maze.reachable(dest):
            yield (current, dest)
        current = dest

def kruskal(maze):
    start = random.choice(maze.graph.nodes())
    walls = maze.walls(start)
    while walls:
        wall = random.choice(walls)
        if not maze.reachable(wall[1]):
            yield wall
            walls.extend(maze.walls(wall[1]))
        walls.remove(wall)

