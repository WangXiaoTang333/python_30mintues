"""
        作者：王糖糖
        功能：汇率兑换currency_converter_v3.0.py
        版本：3.0
        日期：26/12/2018
        新增功能：使程序一直执行，直到用户想退出
"""

# 汇率
USD_VS_RMB = 6.77

currency_str_value = input("请输入带单位的货币输入金额（USD or CNY，退出程序请输入Q）：")
i = 0
while currency_str_value != "Q":
    i = i+1
    print("循环次数：", i)
    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        # pass:python中的占位符，在还没有想好语句时可以使用此
        rmb_value = eval(currency_str_value[:-3])
        usd_value = rmb_value/USD_VS_RMB
        print('美元（USD）的金额是：', usd_value)
    elif unit == 'USD':
        usd_value = eval(currency_str_value[:-3])
        rmb_value = usd_value*USD_VS_RMB
        print('人民币（RMB）的金额是：', rmb_value)
    else:
        print('目前版本尚不支持该种货币')
    print('****************************************')
    currency_str_value = input("请输入带单位的货币输入金额（USD or CNY，退出程序请输入Q）：")
print("程序退出！")



