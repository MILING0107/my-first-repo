def order_milk_tea(tea_name, base_price, *args, **kwargs):
    # 加料价格表
    add_price = {
        "珍珠": 2,
        "布丁": 3,
        "椰果": 2,
        "红豆": 2,
        "芋圆": 3,
        "奶盖": 5,
        "奥利奥": 4
    }
    total = base_price
    add_list = []

    # 处理加料
    for item in args:
        if item in add_price:
            total += add_price[item]
            add_list.append((item, add_price[item]))
        else:
            print("不支持加料：", item)

    # 获取杯型，默认中杯
    cup_size = kwargs.get("大小", "中杯")
    if cup_size == "大杯":
        total += 3

    # 输出订单
    print("-" * 40)
    print(f"饮品：{tea_name}，基础价：{base_price}元")

    print("加料：")
    if add_list:
        for name, p in add_list:
            print(f"    {name} +{p}元")
    else:
        print("    默认无加料")

    print("定制设置：")
    if kwargs:
        for k, v in kwargs.items():
            print(f"    {k}：{v}")
    else:
        print("    默认配置")

    if cup_size == "大杯":
        print("大杯加价 +3元")

    print(f"订单总价：{total}元")
    print("-" * 40)


# 测试调用
order_milk_tea("珍珠奶茶",12,"珍珠","奶盖",甜度="少糖",冰度="去冰",大小="大杯")
order_milk_tea("可可奶茶",14,"奥利奥",甜度="无糖",冰度="常温",大小="中杯")
order_milk_tea("四季春清茶",9)