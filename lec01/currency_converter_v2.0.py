"""
        作者：王糖糖
        功能：汇率兑换currency_converter_v2.0.py
        版本：2.0
        日期：25/12/2018
        新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
"""


# 汇率
USD_VS_RMB = 6.77

currency_str_value = input("请输入带单位的货币输入金额（USD or CNY）：")  # 输入的是字符串，因此要改变类型
print(currency_str_value)
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




