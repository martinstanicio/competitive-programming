import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write


class Graph:
    def bfs(self, start: int, end: int) -> int:
        visited = set()
        queue = deque([(start, 0)])

        while queue:
            node, level = queue.popleft()

            if node == end:
                return level

            if node in visited:
                continue
            visited.add(node)

            if node < end:
                queue.append((node * 2, level + 1))

            if node >= 1:
                queue.append((node - 1, level + 1))

        return -1


def main() -> None:
    start, end = map(int, input().split())
    g = Graph()

    answer = 0

    tmp = max(start - end, 0)
    answer += tmp
    start -= tmp

    answer += g.bfs(start, end)

    print(str(answer) + "\n")


if __name__ == "__main__":
    main()
