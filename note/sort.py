"""
list的排序方法，只适用元素是数字、数组、元组
"""


class Solution(object):

    def takeSecond(self, node):
        return node[1]

    def sort(self):
        def takeSecond(node):
            return node[1]

        data = [[1, 2], [3, 0]]
        data.sort(key=takeSecond)
        print(data)

    def sorted(self):
        # 元组排序
        tuple_data = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
        # 利用参数key来规定排序的规则
        tuple_result = sorted(tuple_data, key=lambda x: x[0])
        print(tuple_result)

        dict_data = [{'name': '张三', 'height': 175}, {'name': '李四', 'height': 165}, {'name': '王五', 'height': 185}]
        dict_result = sorted(dict_data, key=lambda x: (x['height']))
        print(dict_result)


if __name__ == '__main__':
    solution = Solution()
    solution.sorted()
