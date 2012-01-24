import networkx

class InvalidEdge(Exception):
    pass

class Maze(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.graph = networkx.Graph()
        for i in range(self.w):
            for j in range(self.h):
                self.graph.add_node((i, j))

    def _in_bounds(self, *args):
        return all(0 <= x < self.w and 0 <= y < self.h for x, y in args)

    def adjacent(self, (x1, y1), (x2, y2)):
        return abs(x1 - x2) + abs(y1 - y2) == 1

    def neighbors(self, (x, y)):
        result = []
        if x != 0:
            result.append((x - 1, y))
        if x != self.w - 1:
            result.append((x + 1, y))
        if y != 0:
            result.append((x, y - 1))
        if y != self.h - 1:
            result.append((x, y + 1))
        return result

    def walls(self, c):
        return [(c,n) for n in self.neighbors(c) if not self.connected(c,n)]

    def connected(self, c1, c2):
        return c2 in self.graph.neighbors(c1)

    def reachable(self, c):
        return any(self.connected(c, n) for n in self.neighbors(c))

    def connect(self, c1, c2):
        if not self._in_bounds(c1, c2) or not self.adjacent(c1, c2):
            raise InvalidEdge
        self.graph.add_edge(c1, c2)

    def draw_line_between(self, canvas, (x1, y1), (x2, y2), 
                                color=(255, 255, 255)):
        if x1 == x2:
            y = max(y1, y2)
            from_ = (x1, y)
            to = (x1 + 1, y)
        else:
            x = max(x1, x2)
            from_ = (x, y1)
            to = (x, y1 + 1)
        canvas.line(from_, to, color=color)
