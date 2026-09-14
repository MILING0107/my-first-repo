# main.py —— 调用自定义模块 my_fun

# 方式1：import 整个模块，用 模块名.函数名() 调用
import my_fun

print("方式1：import my_fun")
print("10 + 3 =", my_fun.add(10, 3))
print("10 - 3 =", my_fun.sub(10, 3))
print("17 是质数吗？", my_fun.is_prime(17))
print()

# 方式2：from 模块 import 函数，直接用函数名调用
from my_fun import bmi

v, level = bmi(175, 68)
print("方式2：from my_fun import bmi")
print(f"身高175cm、体重68kg → BMI={v}，属于【{level}】")
