# 第八章
# 第2题
def factV1(n):
    # 递归程序
    if n == 1:
        return 1
    else:
        return n * factV1(n - 1)


def fact():
    n = int(input("请输入整数n(n>=0) : "))
    # 递归
    print(f" 递归: {n} !={factV1(n)}")

    # 非递归
    result = 1
    num = n
    while True:
        if num == 0:
            break
        else:
            result = result * num
            num -= 1

    print(f"非递归: {n} !={result}")


# 第3题
def fibV1(n):
    # 递归程序
    if n == 1 or n == 2:
        return 1
    else:
        return fibV1(n - 1) + fibV1(n - 2)


def fib(n=20):
    # 递归
    print("递归:")
    for i in range(1, n + 1):
        print(f"{fibV1(i)}".rjust(5), end='')
        if i == 10:
            print()
    print()
    # 非递归
    print("非递归:")
    listA = [1, 1]
    for i in range(2, n):
        listA.append(listA[i - 1] + listA[i - 2])
    for i in range(n):
        print(f"{listA[i]}".rjust(5), end='')
        if i == 9:
            print()


# 第4题
def min_n(a, b, *args):
    listA = [a, b]
    for i in args:
        listA.append(i)
    print(f"最小值为:{min(listA)}")


# 第5题
def Abc():
    s1 = [9, 7, 8, 3, 2, 1, 55, 6]
    print(f"list= {s1}")
    print(f"最大值= {max(s1)} ,最小值= {min(s1)} ,元素个数= {len(s1)}")
    s2 = ["apple", "pear", "melon", "kiwi"]
    print(f"list= {s2}")
    print(f"最大值= {max(s2)} ,最小值= {min(s2)} ,元素个数= {len(s2)}")
    s3 = "TheQuickBrownFox"
    print(f"list= {s3}")
    print(f"最大值= {max(s3)} ,最小值= {min(s3)} ,元素个数= {len(s3)}")


if __name__ == '__main__':
    # fact()  # 第二题
    # fib()  # 第三题
    # min_n(8,2)  # 第四题
    # min_n(16, 1, 7, 4, 15)  # 第四题
    Abc()  # 第五题
    pass
