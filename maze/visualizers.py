import time

def visualize_algorithm(maze, canvas, generator, speed):
    def inner():
        for node in maze.graph.nodes():
            for neighbor in maze.neighbors(node):
                maze.draw_line_between(canvas, node, neighbor, color='black')
        for c1, c2 in generator(maze):
            maze.connect(c1, c2)
            maze.draw_line_between(canvas, c1, c2)
            time.sleep(speed)             
    canvas.do(inner)
