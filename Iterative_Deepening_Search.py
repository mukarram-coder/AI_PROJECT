class Graph_iterative:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def depth_limited_search(self, start, goal, depth_limit):
        result = self.dls(start, goal, depth_limit)
        if result is None:
            print(f"No path found within depth limit {depth_limit}")
        else:
            print("Path found:", result)

    def dls(self, current, goal, depth_limit):
        if current == goal:
            return [current]
        elif depth_limit == 0:
            return None
        else:
            for neighbor in self.neighbors(current):
                result = self.dls(neighbor, goal, depth_limit - 1)
                if result is not None:
                    return [current] + result
        return None

    def __str__(self):
        return str(self.edges)
