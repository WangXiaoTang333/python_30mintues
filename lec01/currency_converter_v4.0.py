"""
        作者：王糖糖
        功能：汇率兑换currency_converter_v5.0.py
        版本：4.0
        日期：26/12/2018
        新增功能：将汇率兑换功能封装在函数中
"""


def converter_com(im,er):
    out_m = im * er
    return out_m
# 汇率
USD_VS_RMB = 6.77

currency_str_value = input("请输入带单位的货币输入金额（USD or CNY，退出程序请输入Q）：")
unit=currency_str_value[-3:]

# 判断是人民币还是美元
if unit=='USD':
    exchange_rate = USD_VS_RMB
elif unit=='CNY':
    exchange_rate = 1/USD_VS_RMB
else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    # 调用函数
    out_money=converter_com(in_money,exchange_rate)
    print("转换后的货币金额为：", out_money)
else:
    print("不支持该种货币！")




