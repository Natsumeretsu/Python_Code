# 1. 定义字符串变量 `name`，输出 **我的名字叫 小明，请多多关照！**
name = "小明"
print("我的名字叫%s" % name)
# 2. 定义整数变量 `student_no`，输出 **我的学号是 000001**
student_no = 1
print("我的学号是%06d" % student_no)
# 3. 定义小数 `price`、`weight`、`money`，
# 输出 **苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元**
price = 9
weight = 5
money = price * weight
print("苹果单价 %.2f 元／斤，购买了 %.2f 斤，需要支付 %.2f 元" % (price, weight, money))
# 4. 定义一个小数 `scale`，输出 **数据比例是 10.00%**
scale = 10
print("数据比例是 %0.2f%%" % scale)

