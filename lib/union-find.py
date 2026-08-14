class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u: int) -> int:
        """
        Find the representative of the set that contains `u`.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        """
        Merge the sets that contain `u` and `v`.
        """
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] < self.rank[v]:
            u, v = v, u

        self.rank[u] += self.rank[v]
        self.parent[v] = u
