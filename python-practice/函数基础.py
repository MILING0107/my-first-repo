def get_level(score):
    if score >= 90:
        return"A"
    elif score >= 75:
        return"B"
    elif score >= 60:
        return"C"
    else:
        return"D"
ming_score = get_level(99)
print(f"小明的成绩等级为:{ming_score}")


def is_palindrome(s):
    #S[::-1]反转字符串
    reverse_s = s[::-1]
    if reverse_s == s:
        return True
    else:
        return False
print(is_palindrome("level"))
print(is_palindrome("abc"))


def turn_time(s):
    H = round(s / 3600)
    M = round((s % 3600) / 60)
    S = round(s % 60)
    return (f"{H}小时{M}分钟{S}秒")
print(f"3661秒是{turn_time(3661)}")


def sec_to_time(total_sec):
    hour = total_sec // 3600
    remain = total_sec % 3600 
    minute = remain // 60
    sec = remain % 60
    return hour,minute,sec
H,M,S = sec_to_time(3661)
print(f"3661秒是{H}小时{M}分钟{S}秒")


def triangle_type(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return"等边三角形"
        elif a == b or a == c or b == c:
            return"等腰三角形"
        else:
            return"普通三角形"
    else:
        return"不能构成三角形"
print(triangle_type(3,3,4))
print(triangle_type(9,3,4))
        
        
    



    
    
    
        
    
