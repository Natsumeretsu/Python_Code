'''
装饰器的使用
'''

import time


#
# def show():
#     for i in range(10000000):
#         print('Show - ', i)


# # 方式一
# def show():
#     start = time.time()  # 获取当前的时间
#     n = 0
#     for i in range(10000000):
#         n += i
#     print(n)
#     end = time.time()
#     print(f'共用时 {end-start} 秒')
#
#
# show()

# 方式二
#
# def show():
#     n = 0
#     for i in range(10000000):
#         n += i
#     print('Show - ', n)
#
#
# def count_time(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'共用时 {end-start} 秒')
#
#
# show()
# count_time(show)

#
# # 方式三
# def show():
#     n = 0
#     for i in range(10000000):
#         n += i
#     print('Show - ', n)
#
#
# def count_time(func):
#     def inner():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'共用时 {end-start} 秒')
#     return inner
#
# # 装饰器在装饰函数时的原理
# show = count_time(show) # --> show = inner
#
# # 下面的代码是使用者写的,并没有改变原有的调用方式
#
# show()


# 方式四  装饰器的标准使用格式


def count_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'共用时 {end - start} 秒')

    return inner


@count_time  # -> show = count_time(show)
def show():
    n = 0
    for i in range(10000000):
        n += i
    print('Show - ', n)


@count_time  # display = count_time(display)
def display():
    print('Display')


@count_time
def func(a):
    print(a)


# 下面的代码是使用者写的,并没有改变原有的调用方式

show()
display()
func()
