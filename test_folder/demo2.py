import numpy as np


class Node():
    def __init__(self, data=None):
        self._data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        # 如果data存储#字符，那么节点虽然存在，但存储数据是空；否则，data存储输入的数据
        if self.data == '#':
            return None
        return self._data


class BTree():
    def __init__(self, root=None):
        self.root = root

    def add(self, datas):
        for data in datas:
            node = Node(data)
            if self.root is None:
                self.root = node
            else:
                queue = [self.root]
                while queue:
                    cur_node = queue.pop(0)
                    if cur_node.left is None:
                        cur_node.left = node
                        return
                    elif cur_node.right is None:
                        cur_node.right = node
                        return
                    else:
                        queue.append(cur_node.left)
                        queue.append(cur_node.right)

    def breadth_traversal(self, root):
        if root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data, end=' ')
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def leaves(self):
        return


if __name__ == '__main__':
    global C
    C = 10
    s = [2, 2, 6, 5, 4]

    tree = BTree()
    # c = input()
    # s = list(input().split())
    # for i in range(len(s)):
    tree.add(s)

print(tree.root)
#    tree.leaves()
