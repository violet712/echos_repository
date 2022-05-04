import numpy as np


class Node():
    def __init__(self, data=None):
        self._data = data
        self.lchild = None
        self.rchild = None

    @property
    def data(self):
        # 如果data存储#字符，那么节点虽然存在，但存储数据是空；否则，data存储输入的数据
        if self.data == '#':
            return None
        return self._data


class BTree():
    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur_node = queue.pop(0)
                if cur_node.lchild == None:
                    cur_node.lchild = node
                    return
                elif cur_node.rchild == None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                    queue.append(cur_node.rchild)

    def breadth_traversal(self, root):
        if root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def leaves(self):
        return

        # class BTree:
        #     # 初始化
        #     def __init__(self, data=[], lchild=None, rchild=None):
        #         self.data = data
        #         self.lchild = lchild
        #         self.rchild = rchild

        #     # 前序构建二叉树
        #     def pre_order(self, data):

        # 构建二叉树
        # def add(self, data):
        #     node = Node(data)
        #     if self.root is None:
        #         self.root = node
        # else:
        #     self.root.add(node)

        # 输出叶子节点
        # def leaves(self):
        #     if self.data is None:
        #         return None
        #     elif self.left is None and self.right is None:
        #         print(self.data, end='\n')
        #     elif self.left is None and self.right is not None:
        #         self.right.leaves()
        #     elif self.right is None and self.left is not None:
        #         self.left.leaves()
        #     else:
        #         self.left.leaves()
        #         self.right.leaves()


if __name__ == '__main__':
    c = 10
    s = [2, 2, 6, 5, 4]

    tree = BTree([])
    # c = input()
    # s = list(input().split())
    for i in range(len(s)):
        tree.add(data=s[i])

print(tree)
#    tree.leaves()
