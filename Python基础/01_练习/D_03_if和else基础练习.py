# 1. 输入用户年龄
age = int(input("请输入你的年龄，并以回车结束："))
if age >= 18:  # 2. 判断是否满 18 岁 （**>=**）
    print("你的年龄符合规定大于18岁，欢迎进网吧嗨皮!!!")  # 3. 如果满 18 岁，允许进网吧嗨皮
else:
    print("你的年龄未满18岁，回家写作业去吧！")  # 4. 如果未满 18 岁，提示回家写作业
