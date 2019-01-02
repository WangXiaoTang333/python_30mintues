"""
	作者：王糖糖
	功能：汇率兑换
	版本：1.0
	日期：25/12/2018
"""
rmb_str_value=input("请输入人民币（CNY）金额：")
# 输入的是字符串，因此要改变类型
# 转换类型
rmb_value=eval(rmb_str_value)

usd_vs_rmb=6.77

usd_str_value=rmb_value/usd_vs_rmb

print("美元金额是：",usd_str_value)


