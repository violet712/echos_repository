import numpy as np


def fifo(s, C):
    tw = 0  # 已选整数之和
    rw = 0  # 剩下整数之和
    rw = sum(s)
    s1 = []  # 当前子集
    queue = [-1]  # 初始化队列 活结点为-1

    for i in s:
        queue.push(sum + i)  # 加上活结点的值并加入队列
        queue.push(sum)
        if tw + rw > C:  # 如果已选整数之和+剩下整数之和大于C，则结束
            pass
        if tw + i == C:
            s1 = s1.append(i)
            print(s1)
        else:
            return
    dot = queue.pop(0)  # 取出队列第一个值
    if dot == -1:
        if queue.empty():
            return
        queue.push(-1)
    return


if __name__ == '__main__':
    C = 10
    s = [2, 2, 5, 6, 4]
    fifo(s, C)
