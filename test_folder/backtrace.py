def Backtrack(t, s):
    if t == n:
        if s == c:
            print("子集为：")
            for i in range(0, n):
                if x[i] != 0:
                    print(a[i], end=' ')
            print()
            return
    else:
        s = s+a[t]
        x[t] = a[t]
        Backtrack(t+1, s)
        s = s-a[t]  # 回溯之前还原
        x[t] = 0
        Backtrack(t+1, s)


if __name__ == '__main__':
    # 全局变量
    t = 0  # 递归深度
    s = 0  # 子集和
    x = {}  # 判断列表，状态为1或0

    print('请输入集合个数以及求和目标值：')
    n, c = map(int, input().split())
    str = input('请输入集合（以空格为间隔连续输入）:')
    a = list(map(int, str.strip().split()))
    # if Backtrack(t, s) is None:
    #     print("No Solutions!")
    # assert Backtrack(t, s) is not None, print("No Solutions!")
    k = Backtrack(t, s)
    print(k)
