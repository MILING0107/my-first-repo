#1.列表list（注：指定索引不能超出范围）
s=[111,"A",2.5,"abc"]
print (type(s))
print (s[0])
print (s[-1])

s[0] = 222
print (s)

del s[0]
print (s[0])

for i in s:
    print (i)

print (s[:3])
print (s[2:5:2])
print (s[0: :2])#(注：s[start:end:step](起：终：步长),可不填数字)

#2.方法
b = [54,15,75,108,23,78,75]
b.append(10086) #在列表的末尾追加元素
print(b)
b.insert(0,666) #在指定的索引前插入该元素
print(b)
b.remove(75) #移除列表中第一个匹配到的值，需指明元素的值
print(b)
e = b.pop(2) #删除列表中指定索引位置的元素并返回值(此处删除了第三个元素)
print(e)
print(b)
b.pop() #默认移除最后一个值
print(b)
b.sort() #对列表进行排序（需要列表元素类型一致,默认从小到大）
print(b)
b.reverse() #反转列表元素
print(b)

#3.字符串（不可变性，有序性，可迭代性）
s = "Hallo-Python-Hallo-World   "

print(s[5:0:-1]) #可以倒着截取

ss = s.split() #去掉字符串两边的空格
print(ss)

index = s.find("-") #查找指定字符第一次出现的位置
print(index)

c = s.count("H") #记录指定字符出现的次数
print(c) 

su = s.upper() #转大写
print(su)

sl = s.lower() #转小写
print(sl)

slist = s.split("Hallo") #将字符串照指定字符串切割-列表（用于切割的字符串不会输出）
print(slist)

sr = s.replace("-","_") #后面的换前面的
print(sr)

#只返回布尔值
print(s.startswith("   Ha")) #判断是否为指定开头
print(s.endswith("lo")) #判断是否为指定结尾
#（注：每一次操作都是从原式子开始操作，操作不改变原字符串的值）
print(s)

#4.元组（tuple）（元素可重复，有序，不可修改）
t1 = (12,14,54,12,78)

print(t1.count(12)) #计数
print(t1.index(12)) #获取元素索引（第一个元素的位置）

print(t1[1:5:2]) #切片

t2 = ()
print(t2) #空元组

a,b,*c,d = t1 #解包（ * 收集所有的剩余元素）
print(*c)

t3 = *c,a,d
print(t3) #组包.

#5.集合（set）（无序，不可重复，可修改）

s = {1,2,3,4,5,6,7,8,1} #大括号（重复的元素之输出一次，可用于去重）
print(type(s))
print(s)

s.add(1200) #随机位置添加元素
s.remove(1) #移除指定元素
e = s.pop() #随机删除元素并返回
print(e)

print(s)

s1 = {"A","B","c",1,2,3}

print (s.difference(s1))
print (s - s1)
print (s1.difference(s))
print (s1 - s)             #求差集（存在于第一个集合，但不存在于第二个集合）

print (s.union(s1)) 
print (s | s1)             #求并集

print (s.intersection(s1))
print (s & s1)             #求交集

set = s|s1
list = [*s,*s1] #将s，s1全部解包再合并到列表中
print(list)
for s in set:
    print(f"{s}的个数为{list.count(s)}") #用集合循环，用列表计数

#6.字典（dict）（dict = {key ：value}）
dict = {"王琳" : 675,"韩立" : 701} #如果key重复，后值会覆盖前值
score = dict["王琳"] #中括号
print(f"王琳的分数为：{score}")
dict["徐立国"] = 688 #添加
dict["王琳"]=677 #修改
print(dict)
print(dict["王琳"]) #输出指定value

print(dict.values()) #获取所有value
print(dict.keys()) #获取所有key
print(dict.items()) #获取所有键值对（小括号里封装多个元组）

for k in dict.keys():
    print (f"{k} : {dict[k]}") #遍历1
for item in dict.items():
    print (f"{item[0]} : {item[1]}") #遍历2
for k,v in dict.items():
    print (f"{k} : {v}") #遍历3(同理可写出4)

score1 = dict.pop("王琳") 
print(score1) #删除指定键值对并返回值

del dict["徐立国"] #第二种删除方法

print(dict)











