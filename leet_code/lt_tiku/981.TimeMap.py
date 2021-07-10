"""
981. 基于时间的键值存储
创建一个基于时间的键值存储类 TimeMap，它支持下面两个操作：

1. set(string key, string value, int timestamp)

存储键 key、值 value，以及给定的时间戳 timestamp。
2. get(string key, int timestamp)

返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp。
如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
如果没有值，则返回空字符串（""）。
"""
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def set(self, key, value, timestamp):
        self_dict = self.dict[key]
        self_dict.append([timestamp, value])

    def get(self, key, timestamp):
        mapList = self.dict[key]
        if not len(mapList):
            return ""
        left, right = 0, len(mapList) - 1
        while left < right:
            mid = (left + right + 1) >> 1  # mid 进一位 要不然left和right差1会是死循环
            if mapList[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        leftT = mapList[left][0]
        leftValue = mapList[left][1]
        return leftValue if leftT <= timestamp else ""


if __name__ == '__main__':
    solution = TimeMap()
    solution.set("1", "zs", 1)
    solution.set("1", "lisi", 2)
    fun = solution.get("1", 2)
    print(fun)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
