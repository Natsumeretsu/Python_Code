# # 1. 练习1: 定义一个整数变量 `age`，编写代码判断年龄是否正确
# #     * 要求人的年龄在 0-120 之间
age = int(input("请输入您的年龄："))
if 0 <= age <= 120:
    print("输入正确！！您的年龄是%d岁！" % age)
else:
    print("错误！")
# # 2. 练习2: 定义两个整数变量 `python_score`、`c_score`，编写代码判断成绩
# #     * 要求只要有一门成绩 > 60 分就算合格
python_score = 10
c_score = 90
if python_score > 60 or c_score > 60:
    print("合格！！！！")
# # 3. 练习3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
#     * 如果不是提示不允许入内
is_employee = True
if not is_employee != 0:
    print("不允许入内！！")
else:
    print("允许入内！！")
#在开发中，通常希望某个条件不满足时，执行一些代码，可以用not
#另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到not

