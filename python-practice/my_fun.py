# my_fun.py —— 自定义模块（一堆函数放在一起就是一个模块）

def add(a, b):
    """加法"""
    return a + b

def sub(a, b):
    """减法"""
    return a - b

def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def bmi(height_cm, weight_kg):
    """计算 BMI 并给出评价"""
    m = height_cm / 100
    value = weight_kg / (m * m)
    if value < 18.5:
        level = "偏瘦"
    elif value < 24:
        level = "正常"
    elif value < 28:
        level = "偏胖"
    else:
        level = "肥胖"
    return round(value, 1), level


# ---------- 模块自测代码 ----------
# 只有直接运行 my_fun.py 时才会执行；被 import 时不会执行
if __name__ == "__main__":
    print("模块自测：add(1, 2) =", add(1, 2))
