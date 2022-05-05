import numpy as np


class Node():
    # 节点类
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    # 树类
    def __init__(self):
        self.root = Node()

    def add(self, data):
        # 为树加入节点
        node = Node(data)
        if self.root.data == None:  # 如果树为空，就对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:  # 对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if treeNode.left == None:
                    treeNode.left = np.append(treeNode, node)
                    return
                elif treeNode.right == None:
                    treeNode.right = treeNode
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    def BFS(self, root):  # 层次遍历核心代码
        if root == None:
            return
        queue = []
        queue.append(root)

        while queue:
            now_node = queue.pop(0)
            print(now_node.data)
            if now_node.left != None:
                queue.append(now_node.left)
            if now_node.right != None:
                queue.append(now_node.right)


if __name__ == '__main__':
    # 主函数
    datas = [[1], [2], [3]]
    tree = Tree()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个加入树的节点

    print('递归实现前序遍历：')
    tree.BFS(tree.root)

    print(np.sum(datas))
