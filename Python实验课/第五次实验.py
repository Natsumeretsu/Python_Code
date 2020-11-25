# 第九章
# 第二题
class MyMath(object):
    def __init__(self):
        self.pi = 3.1415926
        self.r = int(input("请输入半径: "))
        print("圆的周长 =  {:.2f}".format(2 * self.r * self.pi))
        print("圆的面积 =  {:.2f}".format(self.pi * (self.r ** 2)))
        print("球的表面积 = {:.2f}".format(4 * self.pi * (self.r ** 2)))
        print("球的体积 =  {:.2f}".format((4 / 3) * self.pi * (self.r ** 3)))


# 第三题
class Temperature(object):
    def __init__(self):
        self.degree = int(input("请输入摄氏温度："))
        self.ToFahrenheit()
        self.degree1 = int(input("请输入华氏温度："))
        self.ToCelsius()

    def ToFahrenheit(self):
        # 摄氏温度转换为华氏温度
        print(f"摄氏温度 = {self.degree}, 华氏温度 = {(9 / 5) * self.degree + 32}")

    def ToCelsius(self):
        # 华氏温度转换为摄氏温度
        print(f"华氏温度 = {self.degree1}, 摄氏温度 = {(5 / 9) * (self.degree1 - 32)}")


if __name__ == '__main__':
    # MyMath()  # 第二题
    Temperature()  # 第三题
    pass
