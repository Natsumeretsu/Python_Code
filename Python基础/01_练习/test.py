def multiple_table():
    # 九九乘法表
    row = 0
    while row < 9:
        col = 0
        while col <= row:
            print("%d * %d = %d" % (col + 1, row + 1, (row + 1 )* (col + 1)), end="\t")
            col += 1
        print("")
        row += 1
