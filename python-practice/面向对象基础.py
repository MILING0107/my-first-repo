#定义类
class Car:
    
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        
    print("Car类型的对象初始化完毕，对象属性已添加完毕。")
    
# 创建对象

c1 = Car("red","BAM","X7",800000)

print(c1.__dict__)
print(c1.color)
    
    
    
    
    
    