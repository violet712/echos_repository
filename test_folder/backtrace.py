def Backtrack(t, s):
    if t == n:
        if s == c:
            global has_solution
            has_solution = True
            print("子集为：")
            for i in range(0, n):
                if x[i] != 0:
                    print(a[i], end=' ')
            print()
            return
    else:
        s = s+a[t]
        x[t] = a[t]  # 选择第t个元素
        if s > c:  # 剪枝 子集和大于c则不再向下搜索
            pass
        else:
            Backtrack(t+1, s)
        s = s-a[t]  # 回溯之前还原
        x[t] = 0
        Backtrack(t+1, s)


if __name__ == '__main__':
    # 全局变量
    t = 0  # 递归深度
    s = 0  # 子集和
    x = {}  # 判断列表，状态为1或0
    has_solution = False  # 是否有解

    print('请输入集合个数以及求和目标值：')
    n, c = map(int, input().split())
    str = input('请输入集合（以空格为间隔连续输入）:')
    a = list(map(int, str.strip().split()))  # S
    Backtrack(t, s)
    if has_solution == False:
        print("No Solutions!")
