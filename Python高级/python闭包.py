"""闭包定义格式"""


# 要形成三个条件
# 1.在函数嵌套(函数里面在定义函数)的前提下
# 2.内部函数使用了外部函数的变量(还包括外部函数的参数)
# 3.外部函数返回了内部函数


def outer():
    n = 1

    def inner():
        print(n)
        # 当函数没有返回值时,默认返回None
        # return None

    # 在外函数返回  内函数引用  时,不能带括号
    # 若是带括号返回 如:return inner() 则在此进行函数调用,此时inner() = None
    return inner
    # 此时返回内函数的地址,而之后有可能会调用内函数,
    # 所以外函数执行完毕后其内部环境及其变量都不能释放,以便后续再次使用


ret = outer()
print(ret)
ret()


def show():
    print('show')


# 闭包就是 内函数的引用 + 外函数的执行环境
print(show)
# func = show  # 将show的函数引用赋值给func
# func()
