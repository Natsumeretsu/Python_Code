# 火车站安检
#
# **需求**
#
# 1. 定义布尔型变量 `has_ticket` 表示是否有车票
has_ticket = True
# 2. 定义整型变量 `knife_length` 表示刀的长度，单位：厘米
knife_length = 40
# 3. 首先检查是否有车票，如果有，才允许进行 **安检**
if has_ticket:
    print("车票检测通过，准备开始安检！！")
    if knife_length > 20:
        print("发现管制刀具有%dcm超过20cm！！！禁止上车！！" % knife_length)
    else:
        print("安检通过，准许上车！！")
else:
    print("没有车票，请先购票！！")
    # 4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
    #     * 如果超过 20 厘米，提示刀的长度，不允许上车
    #     * 如果不超过 20 厘米，安检通过
    # 5. 如果没有车票，不允许进门
