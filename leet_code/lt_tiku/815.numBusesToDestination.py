"""
815. 公交路线
给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
"""
from collections import defaultdict, deque


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        # 每个车站可以乘坐的公交车
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        # 每个公交车线路可以到达的车站
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])
        # 已经乘坐了的公交车
        buses = set()
        # 已经到达了的车站
        stops = {source}
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            # 当前车站中尚未乘坐的公交车
            for bus in stations[pos] - buses:
                # 该公交车尚未到达过的车站
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1


if __name__ == '__main__':
    solution = Solution()
    fun = solution.numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15, target=12)
    print(fun)
