# 数组
> python的所有遍历操作都是左开右闭
## 数组访问
数组访问可以正向或逆向

arr[2] == arr[-1]
```
arr = ["a","b","c"]
        0   1   2
       -3  -2  -1
```
1. 正向索引下标是从零开始，不是1
2. 反向索引是到-1结束，不是0

## 数组赋值
A是一个数组
1. arr = A 让nums变量指向A的地址值
2. arr[:] = A 是A对arr逐一覆盖赋值，不改变nums值



## 数组截取
数组是从左到右取值，起始位置不能越过结束位置
    arr[2,1]==[],arr[-1,-3]==[]
### 两个参数
arr[i,e]
1. i:起始位置 默认0
2. e:结束位置 len(a)
3. arr[:]等于arr的视图，可以修改值但是不用改变数组的地址值
### 三个参数
arr[i,e,s]

1. i:起始位置 默认-1
2. e:结束位置 默认-len(a)-1 （逆向索引比正向索引大1位）
3. s:步长 默认为1

arr[::-1] 倒叙遍历数组



# Bool
## 多个判断
1 and 0 or 1 and 0
运算顺序：
1. 先运算所有的and运算，and运算部分先后，存在一个假即为假
2. 再运算所有的or，运算不分顺序，存在一个真即为真。
上述运算结果为：
0 or 0 结果为假


# 二进制
## 常见数字
0xFF=255



# 常见API
## collections模块
### Counter
用于用于追踪值的出现次数 ，继承了dict
```python
from collections import Counter
s="aaceeee"
counter = Counter(s)
# dict(counter) = {'a': 2, 'c': 1, 'e': 4}
```
部分API
1. most_common(n) 获取词频最高的k元素(指定一个参数n，列出前n个元素，不指定参数，则列出所有)
2. items 遍历集合 (从dict类中继承的方法) keys() 获取key数组 values() 获取value数组
3. update(ele...) 新增字符词频，可传入多个元素
4. subtract(ele...) 降低字符词频,可传入多个元素,词频可为负数
5. elements() 获取所有元素的迭代器

##sorted & sort
1. sort 将list自身进行排序,不返回新的list对象 速度比sorted更快
2. sorted可以排序任何元素,sort只能排序数字、数组、元组

### sort
> list.sort(key=None, reverse=False)
1. key=None 值为一个函数，此函数只有一个参数且返回一个值用来进行比较
2. reverse=False 默认升序 小->大 True 降序排序
```python
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
def takeSecond(node):
    return node[1]
random.sort(key=takeSecond)
print(random)
```

### sorted
sorted 可以对所有可迭代的对象进行排序操作
>sorted(iterable, key=None, reverse=False)  
```python

```

