import time

def visualize_algorithm(maze, canvas, generator, speed):
    for node in maze.graph.nodes():
        for neighbor in maze.neighbors(node):
            maze.draw_line_between(canvas, node, neighbor, color=(0, 0, 0))

    for c1, c2 in generator(maze):
        maze.connect(c1, c2)
        maze.draw_line_between(canvas, c1, c2)
        time.sleep(speed)             
