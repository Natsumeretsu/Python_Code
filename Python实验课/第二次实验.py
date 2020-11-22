# 第四章
import math


# 第2题 杨辉三角
def YangTri(n=5):
    ls0 = [1]
    ls1 = [1]
    for i in range(1, n + 1):
        for j in range(1, i - 1):
            ls1.insert(j, ls0[j - 1] + ls0[j])
        print(ls1)
        ls0 = ls1
        ls1 = [1, 1]


# 第2题 杨辉三角
def YangTriV2(n=5):
    ls0 = ['1']
    ls1 = ['1']
    for i in range(1, n + 1):
        for j in range(1, i - 1):
            ls1.insert(j, str(int(ls0[j - 1]) + int(ls0[j])))
        print("    ".join(ls1).center(n ** 2))
        ls0 = ls1
        ls1 = ['1', '1']


# 第3题
def CalTriangel():
    pi = 3.14

    a = int(input("请输入直角三角形的直角边A(>0): "))
    b = int(input("请输入直角三角形的直角边B(>0): "))
    c = (a ** 2 + b ** 2) ** 0.5
    a1 = math.asin(a / c) * 180 / pi
    b1 = math.asin(b / c) * 180 / pi
    print("执教三角形的三边分别为: a={:.1f},b={:.1f},c={:.1f}".format(a, b, c))
    print("三角形的周长 = {:.1f}, 面积 = {:.1f}".format(a + b + c, a * b * 0.5))
    print("三角形两个锐角的度数分别为:{:.1f} 和{:.1f}".format(a1, b1))


# 第5题
def CalSalary():
    salary = int(input("请输入有固定工资收入的党员的月工资: "))
    if salary <= 3000:
        DeOther = 0.5 * 0.01 * salary
    elif salary <= 5000:
        DeOther = 1 * 0.01 * salary
    elif salary <= 10000:
        DeOther = 1.5 * 0.01 * salary
    else:
        DeOther = 2 * 0.01 * salary
    print(f"月工资 = {salary},缴纳的党费 = {DeOther}")


# 第6题
def MiniCalculate():
    x = input("前输入操作数x:")
    y = input("前输入操作数y:")
    ch = input("请输入操作符:")
    if (ch == '/' or ch == '%') and y == '0':
        print("分母=0,零除异常!")
        return 0
    else:
        print(f"{x}{ch}{y}={eval(x + ch + y)}")


# 第8题 解方程
def Cal_CandR1():
    h = int(input("请输入总头数: "))
    while True:
        f = int(input("请输入总脚数(必须是偶数):"))
        if f % 2 == 0:
            break

    # 法一 解方程
    r1 = f / 2 - h
    c1 = h - r1
    if 0 <= c1 <= h and 0 <= r1 <= h and r1 + c1 == h:
        print("方法一:鸡:{:.0f} 只, 兔:{:.0f} 只".format(c1, r1))
    else:
        print("方法一:无解,请重新运行测试!")

    # 法二 枚举
    for c2 in range(h + 1):
        r2 = h - c2
        if 2 * c2 + 4 * r2 == f:
            print("方法二:鸡:{:.0f} 只, 兔:{:.0f} 只".format(c2, r2))
            break
        if c2 == h:
            print("方法二:无解,请重新运行测试!")


if __name__ == '__main__':
    # YangTri(15)
    # YangTriV2()  # 第二题
    # CalTriangel()  # 第三题
    # CalSalary()  # 第五题
    MiniCalculate()  # 第六题
    # Cal_CandR1()  # 第八题
    pass
