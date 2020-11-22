# 第三章
# 第5题
def SumNum():
    result = 0
    for num in range(2, 101):

        if num % 2 == 0:
            result += num
    print(result)


# 第6题
def CalYear():
    flag = 0
    for year in range(2000, 3001):
        if year % 4 == 0 and year % 100 != 0:
            flag += 1
            print(year, end=' ')
            if flag % 18 == 0:
                print('')
        if year % 400 == 0:
            flag += 1
            print(year, end=' ')
            if flag % 18 == 0:
                print('')


# 第7题
def SumOdd(n=100):
    ls = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            ls.append(i)
    print(ls)
    result = 0
    j = 0
    for i in ls:
        result += pow(-1, j) * i
        j += 1
    print(f'Sn={result}')


# 第8题
def Sum(n=100):
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    print(f'Sn= {result}')


# 第9题 上三角
def UpperMultiTable():
    for row in range(1, 10):
        # print(f'{row}---',end='')
        for col in range(1, row + 1):
            print(f'{col}*{row}={row * col}', end='\t')
        print('')


# 第9题 矩形
def RectMultiTable():
    for row in range(1, 10):
        # print(f'{row}---',end='')
        for col in range(1, 10):
            print(f'{row}*{col}={row * col}', end='\t')
        print('')


# 第9题 下三角
def LowerMultiTable():
    for row in range(1, 10):
        print('\t\t' * (row - 1), end='')
        for col in range(row, 10):
            print(f'{row}*{col}={row * col}', end='\t')
        print('')


# 第10题
def CalTriangle():
    a = int(input("请输入三角形的边A:"))
    b = int(input("请输入三角形的边B:"))
    c = int(input("请输入三角形的边C:"))
    if False in (a, b, c) or (a + b <= c or a + c <= b or c + b <= a):
        print("无法构成三角形")
    else:
        sum1 = a + b + c
        h = sum1 / 2
        sum2 = pow(h * (h - a) * (h - b) * (h - c), 0.5)
        print(f'三角形的三边分别为: a={a}, b={b}, c={c}')
        print(f'三角形的周长= {sum1} ,面积={sum2}')


# 第12题
def FunctionA():
    a = float(input("请输入系数a:"))
    b = float(input("请输入系数b:"))
    c = float(input("请输入系数c:"))
    if a == 0 and b == 0:
        print("此方程无解！")
    elif a == 0 and b != 0:
        print(f"此方程的解为：{-c / b}")
    elif b ** 2 - 4 * a * c == 0:
        print(f"此方程有两个相等实根：{-b / (2 * a)}")
    elif b ** 2 - 4 * a * c > 0:
        print(
            f"此方程有两个不等实根：{-b / (2 * a) + ((b ** 2 - 4 * a * c) ** 0.5) / (2 * a)} "
            f"和{-b / (2 * a) - ((b ** 2 - 4 * a * c) ** 0.5) / (2 * a)}")
    elif b ** 2 - 4 * a * c < 0:
        print(
            f"此方程有两个共轭复根：{-b / (2 * a)}+{((4 * a * c - b ** 2) ** 0.5) / (2 * a)}i "
            f"和{-b / (2 * a)}-{((4 * a * c - b ** 2) ** 0.5) / (2 * a)}i")


if __name__ == '__main__':
    # SumNum()  # 第5题
    # CalYear()# 第6题
    # SumOdd()  # 第7题
    # Sum()  # 第8题
    # UpperMultiTable()  # 第9题
    # RectMultiTable()
    # LowerMultiTable()
    # CalTriangle()  # 第10题
    FunctionA()  # 第12题
    pass
