# [第一题](./cloud/duringbug/one.py)：
- 1. 我首先想的是递归加规划(将已经算出来的结果储存在store字典里)
```python
class MaxFinder:
    def __init__(self):
        self.store = {}
        self.son = {}

    def find_max(self, num):
        if num in self.store:
            return self.store[num]
        else:
            max_value = num
            num_1 = 0
            num_2 = num
            for i in range(1, math.floor(num/2)+1):
                r = self.find_max(i) * self.find_max(num-i)
                if r > max_value:
                    max_value = r
                    num_1 = i
                    num_2 = num-i
            self.store[num] = max_value
            self.son[num] = [num_1, num_2]
            return max_value

    def print_result(self, num):
        if num <= 3:
            print(num, end=" ")
        else:
            self.print_result(self.son[num][0])
            self.print_result(self.son[num][1])
```
但发现打印的结果全是3，说明分解的时候，尽量向2，3分解会是相乘更大

# [第二题](./cloud/duringbug/two.py)
确实快

# [第三题](./cloud/duringbug/three.py)

# [第四题](./cloud/duringbug/four.py)

# [第五题](./cloud/duringbug/five.py)

# [第六题](./cloud/duringbug/six.py)

**发现在跳出循环的阀值相同时,c越靠近$ \sqrt{2} 结果更精确$**

# [第七题](./cloud/duringbug/seven.py)

# [第八题](./cloud//duringbug/eight.py)

# [第九题](./cloud/duringbug/nine.py)

运行结果
```bash
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 

2**10=1024
2**20=1048576
2**30=1073741824
2**40=1099511627776
2**50=1125899906842624

原岸状态:: ['man', 'sheep', 'wolf', 'greens'] ['wolf', 'greens'] ['man', 'wolf', 'greens'] ['wolf'] ['man', 'sheep', 'wolf'] ['greens'] ['man', 'sheep', 'greens'] ['sheep'] ['man', 'sheep'] 
原岸状态:: ['man', 'sheep', 'wolf', 'greens'] ['wolf', 'greens'] ['man', 'wolf', 'greens'] ['wolf'] ['man', 'sheep', 'wolf'] ['sheep'] ['man', 'sheep'] 
原岸状态:: ['man', 'sheep', 'wolf', 'greens'] ['wolf', 'greens'] ['man', 'wolf', 'greens'] ['greens'] ['man', 'sheep', 'wolf'] ['sheep'] ['man', 'sheep'] 
原岸状态:: ['man', 'sheep', 'wolf', 'greens'] ['wolf', 'greens'] ['man', 'wolf', 'greens'] ['greens'] ['man', 'sheep', 'greens'] ['sheep'] ['man', 'sheep'] 

1.4142135381698608

1.4142135623746899
1.4142135626178514

1.41421356237384
1.4142135623738359
1.4142135623738188

-1.6506291914393951

蒙特卡洛方法:3.1400480000
无限级数:3.1415916536
投针法3.1419720000

11.8033230000
```