def sum_2_number(num1, num2):
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    return result
    '''加法程序'''


def print_line(char,times):
    print(char * times)
    '''分割线程序'''


print_line("*",50)
ABC = sum_2_number(3, 2)
print("ABC = %d" % ABC)
print_line("=",50)
i = 0
while i < 5:
    print_line("-",50)
    i += 1
