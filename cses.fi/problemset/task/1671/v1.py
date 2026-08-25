import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline
print = sys.stdout.write


class Graph:
    def __init__(self, size: int) -> None:
        self.size = size
        self.adj = [[] for _ in range(size)]

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        self.adj[u].append((weight, v))

    def dijkstra(self, start: int) -> list[float]:
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


def main() -> None:
    cities, connections = map(int, input().split())
    g = Graph(cities)

    for _ in range(connections):
        u, v, w = map(int, input().split())

        g.add_edge(u - 1, v - 1, w)

    distances = g.dijkstra(0)

    print(" ".join(str(d) for d in distances) + "\n")


if __name__ == "__main__":
    main()
