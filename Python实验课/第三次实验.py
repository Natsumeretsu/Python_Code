# 第五章

# 第2题
def CountStr():
    count = 0
    Ustr = input("请输入字符串并以空格分隔:").split(' ')
    for i in Ustr:
        count += 1
    print(f"其中的单词总数有: {count}")


# 第3题
def ListUniq(Alist):
    Ulist = list(set(Alist))
    print(Ulist)
    return Ulist


# 第4题
def MinMax():
    s = [9, 7, 8, 3, 2, 1, 55, 6]

    # for循环 & 直接访问元素列表(for i in s...)
    For_count = 0
    For_Max, For_Min = s[0], s[0]
    For_sum = 0
    for i in s:
        For_count += 1
        if i > For_Max:
            For_Max = i
        if i < For_Min:
            For_Min = i
        For_sum += i
    print(f"For循环 & 直接访问元素列表(for i in s...):\n\t元素的个数: {For_count}\t  元素的最大值: {For_Max}\t"
          f"元素的最小值: {For_Min}\t 元素的和: {For_sum}\t  元素的平均值: {For_sum / For_count}")

    # for循环 & 间接访问元素列表(for i in range(0,len(s)))
    For2_count = 0
    For2_Max, For2_Min = s[0], s[0]
    For2_sum = 0
    for For_i in range(0, len(s)):
        For2_count += 1
        if s[For_i] > For2_Max:
            For2_Max = s[For_i]
        if s[For_i] < For2_Min:
            For2_Min = s[For_i]
        For2_sum += s[For_i]
    print(f"For循环 & 间接访问元素列表(for i in range(0,len(s)):\n\t元素的个数: {For2_count}\t  元素的最大值: {For2_Max}\t"
          f"元素的最小值: {For2_Min}\t 元素的和: {For2_sum}\t  元素的平均值: {For2_sum / For2_count}")

    # while循环 & 正序访问 (i = 0 ; while i < len(s)...)
    while1_i = 0
    while1_Max, while1_Min = s[0], s[0]
    while1_sum = 0
    while while1_i < len(s):
        if s[while1_i] > while1_Max:
            while1_Max = s[while1_i]
        if s[while1_i] < while1_Min:
            while1_Min = s[while1_i]
        while1_sum += s[while1_i]
        while1_i += 1
    print(f"while循环 & 正序访问 (i = 0 ; while i < len(s)...):\n\t元素的个数: {len(s)}\t  元素的最大值: {while1_Max}\t"
          f"元素的最小值: {while1_Min}\t 元素的和: {while1_sum}\t  元素的平均值: {while1_sum / len(s)}")

    # while循环 & 反序访问 (i = len(s)-1 ; while i >= 0...)
    while2_i = len(s) - 1
    while2_Max, while2_Min = s[0], s[0]
    while2_sum = 0
    while while2_i >= 0:
        if s[while2_i] > while2_Max:
            while2_Max = s[while2_i]
        if s[while2_i] < while2_Min:
            while2_Min = s[while2_i]
        while2_sum += s[while2_i]
        while2_i -= 1
    print(f"while循环 & 反序访问 (i = len(s)-1 ; while i >= 0...):\n\t元素的个数: {len(s)}\t  元素的最大值: {while2_Max}\t"
          f"元素的最小值: {while2_Min}\t 元素的和: {while2_sum}\t  元素的平均值: {while2_sum / len(s)}")

    # While True : ... break
    while3_Max, while3_Min = s[0], s[0]
    while3_sum = 0
    while3_count = 0
    while True:
        if s[while3_count] > while3_Max:
            while3_Max = s[while3_count]
        if s[while3_count] < while3_Min:
            while3_Min = s[while3_count]
        while3_sum += s[while3_count]
        while3_count += 1
        if while3_count == len(s):
            break
    print(f"While True : ... break:\n\t元素的个数: {while3_count}\t  元素的最大值: {while3_Max}\t"
          f"元素的最小值: {while3_Min}\t 元素的和: {while3_sum}\t  元素的平均值: {while3_sum / while3_count}")


# 第5题
def EvenTosquare():
    s = [9, 7, 8, 3, 2, 1, 5, 6]
    print(f'变换前,s={s}')
    for i in s:
        if i % 2 == 0:
            s[s.index(i)] = i ** 2
    print(f'变换后,s={s}')


# 第6题
def StrToAscii():
    AAstr = input("请输入一个字符串:")
    AsciiList = []
    for i in AAstr:
        AsciiList.append(ord(i))
    print(AsciiList)


if __name__ == '__main__':
    # CountStr() # 第2题
    # Test = ["hello", "hello", "hello", "hello",
    #         'world', 1, 2, 3, 1, 2, '1', '2', '3', '1', '2']  # 第3题
    # ListUniq(Test)  # 第3题
    # MinMax()  # 第4题
    # EvenTosquare()  # 第5题
    StrToAscii()  # 第6题
    pass
