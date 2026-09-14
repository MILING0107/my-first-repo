def calc_order_cost(*args,coupon = 0,score = 0,express = 0):
    
    total_price = [ goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    
    if total_cost >= 5000 and coupon < total_cost:
        total_cost -= coupon
    
    if total_cost >= 5000 and score // 100 < total_cost:
        total_cost -= score // 100
    
    total_cost += express
    
    return total_cost

print(calc_order_cost(("鼠标",188,2),("键盘",388,1), ("手机",8999,1),coupon = 3000, score = 400)) 
        
    
        