from collections import deque
from heapq import heappop, heappush
from math import inf


class Graph:
    def __init__(self, size: int) -> None:
        self.size = size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        """
        Add an edge from `u` to `v` with the given `weight`, or `1` if no `weight` is provided.
        """
        self.adj[u].append((weight, v))

    def bfs(self, start: int) -> None:  # O(V + E):
        """
        Perform a breadth-first search starting from the `start` node.
        """
        visited = [False] * self.size
        visited[start] = True

        queue = deque([start])

        while queue:
            node = queue.popleft()

            for weight, neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dfs_recursive(self, start: int) -> None:  # O(V + E)
        """
        Perform a depth-first search recursively starting from the `start` node.
        """
        visited = [False] * self.size

        def helper(node: int) -> None:
            visited[node] = True

            for weight, neighbor in self.adj[node]:
                if not visited[neighbor]:
                    helper(neighbor)

        helper(start)

    def dfs_iterative(self, start: int) -> None:  # O(V + E)
        """
        Perform a depth-first search iteratively starting from the `start` node.
        """
        visited = [False] * self.size
        stack = [start]

        while stack:
            node = stack.pop()

            if not visited[node]:
                visited[node] = True

                for weight, neighbor in self.adj[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    def dijkstra(self, start: int) -> list[float]:  # O((V + E) log V)
        """
        Find the length of the shortest path from the `start` node to all other nodes.
        """
        distance = [inf] * self.size
        distance[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            d1, node = heappop(priority_queue)

            if d1 > distance[node]:
                continue

            for weight, neighbor in self.adj[node]:
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
                    heappush(priority_queue, (distance[neighbor], neighbor))

        return distance

    def bellman_ford(self, start: int) -> list[float] | None:  # O(V * E)
        """
        Find the length of the shortest path from the `start` node to all other nodes.

        Supports negative weights, but not negative cycles. Returns `None` if a negative cycle is detected.
        """
        distance = [inf] * self.size
        distance[start] = 0

        for i in range(self.size):
            for node in range(self.size):
                if distance[node] == inf:
                    continue

                for weight, neighbor in self.adj[node]:
                    if distance[node] + weight < distance[neighbor]:
                        if i == self.size - 1:
                            return None  # negative cycle

                        distance[neighbor] = distance[node] + weight

        return distance

    def floyd_warshall(self) -> list[list[float]] | None:  # O(V^3)
        """
        Find the length of the shortest path between all pairs of nodes.

        Supports negative weights, but not negative cycles. Returns `None` if a negative cycle is detected.
        """
        distances = [[inf] for _ in range(self.size)] * self.size

        for node in range(self.size):
            distances[node][node] = 0

            for weight, neighbor in self.adj[node]:
                distances[node][neighbor] = weight

        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    distances[i][j] = min(
                        distances[i][k] + distances[k][j], distances[i][j]
                    )

        if any(distances[i][i] < 0 for i in range(self.size)):
            return None  # negative cycle

        return distances
