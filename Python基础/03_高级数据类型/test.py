# # str = "hello"
# # # 假设：以下内容是从网络上抓取的
# # # 要求：顺序并且居中对齐输出以下内容
# # poem = ["\t\n登鹳雀楼",
# #          "王之涣",
# #          "白日依山尽\t\n",
# #          "黄河入海流",
# #          "欲穷千里目",
# #          "更上一层楼"]
# # for poem_line in poem:
# #     print("|%s|" % poem_line.strip().center(10,"　"))
#
# # 假设：以下内容是从网络上抓取的
# # 要求：
# # 1. 将字符串中的空白字符全部去掉
# # 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
# poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"
#
# print(poem_str)
# # rpoem_str = []
#
# poem_list = poem_str.split()
# print(poem_list)
# result = " ".join(poem_list)
# print(result)
#
# print("python"[0:5:2])

students = [
    {"name":"张三"},
    {"name":"李四"}
]

find_name = "小明"
students.append({"name":"王五"})
for stu_dict in students:
    if find_name == stu_dict["name"]:
        print("找到了%s！"% find_name)
        break
else:
    print("未搜索到%s！"% find_name)
