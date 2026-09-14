students = {}
menu = """
########### 教务管理系统 ###########
#          1.添加学生信息          #
#          2.修改学生信息          #
#          3.删除学生信息          #
#          4.查询学生信息          #
#          5.列出所有学生          #
#          6.统计班级成绩          #
#          7.退出系统              #
###################################
"""
print("欢迎使用教务系统^_^")

while True:
    print(menu)
    choice = input("请选择要执行的操作（1—7):")
    
    if choice == "1":
        student_id = input("请输入学号：")
        
        if student_id in students:
            print("该学号已存在，请重新输入！")
            continue
        name = input("请输入姓名：")
        
        try:
            chinese = float(input("请输入语文成绩:"))
            math = float(input("请输入数学成绩："))
            english = float(input("请输入英语成绩："))
            
            if chinese < 0 or chinese > 100 or math < 0 or math > 100 or english < 0 or english > 100:
                print("成绩应该在0-100之间!")
                continue
        except ValueError:
            print("成绩请输入数字!")
            continue
        
        students[student_id] = {
            "name":name,
            "chinese":chinese,
            "math":math,
            "english":english
        }
    elif choice == "2":
        student_id = input("请输入要修改的学号：")
        
        if student_id not in students:
            print("该学号不存在，请重新输入！")
            continue
        
        old_data = {
            "name":students[student_id]['name'],
            "chinese":students[student_id]['chinese'],
            "math":students[student_id]['math'],
            "english":students[student_id]['english']
        }
        
        print(f"当前信息：姓名：{students[student_id]['name']},语文{students[student_id]['chinese']},数学{students[student_id]['math']},英语{students[student_id]['english']}")
        print("如需修改某项，请直接输入新值，不修改请直接回车")
        
        modified_count = 0
        
        name = input(f"请输入新姓名（当前：{students[student_id]['name']}):")
        if name != "":
            if name == old_data['name']:
                print("姓名与原来相同，未作修改")
            else:
                students[student_id]["name"] = name
                modified_count += 1
                print("姓名修改成功！")
        else:
            print("姓名未修改")
            
        try:
            chinese_input = input(f"请输入新语文成绩（当前：{students[student_id]['chinese']}):")
            if chinese_input != "":
                chinese = float(chinese_input)
                if 0 <= chinese <= 100:
                    if chinese ==  old_data['chinese']:
                          print("语文成绩与原来相同，未作修改")
                    else:
                        students[student_id]['chinese'] = chinese
                        modified_count += 1
                        print("语文成绩修改成功！")
                else:
                    print("成绩应在0-100之间，该选项未修改")
            else:
                 print("语文成绩未修改")
                
            math_input = input(f"请输入新数学成绩（当前：{students[student_id]['math']}):")
            if math_input != "":
                math = float(math_input)
                if 0 <= math <= 100:
                    if math == old_data['math']:
                        print("数学成绩与原来相同，未作修改")
                    else:
                        students[student_id]['math'] = math
                        modified_count += 1
                        print("数学成绩修改成功！")
                else:
                    print("成绩应在0-100之间，该选项未修改")
            else:
                print("数学成绩未修改")
            
                     
            english_input = input(f"请输入新英语成绩（当前：{students[student_id]['english']}):")
            if english_input != "":
                english = float(english_input)
                if 0 <= english <= 100:
                    if english == old_data['english']:
                         print("英语成绩与原来相同，未作修改")
                    else:
                        students[student_id]['english'] = english
                        modified_count += 1
                        print("英语成绩修改成功！")
                else:
                    print("成绩应在0-100之间，该选项未修改")
            else:
                print("英语成绩未修改")
        except ValueError:
            print("成绩请输入数字！")
            continue
        if modified_count == 0:
            print("所有信息均未修改")
        else:
            print(f"共修改了{modified_count}项信息,修改完毕^_^")
    
    elif choice == "3":
        student_id = input("请输入要删除的学生学号：")
        
        if student_id not in students:
            print("该学号不存在，请重新输入！")
            continue
        else:
            del students[student_id]
            print("学生信息删除完毕！")
            
    elif choice == "4":
        # 查询学生信息
        print("请选择查询方式：")
        print("1.按学号查询")
        print("2.按姓名查询")
        search_type = input("请输入选择(1-2)：")
        
        if search_type == "1":
            student_id = input("请输入学号：")
            if student_id in students:
                info = students[student_id]
                print(f"学号：{student_id}，姓名：{info['name']}，语文：{info['chinese']}，数学：{info['math']}，英语：{info['english']}")
            else:
                print("未找到该学号的学生！")
        
        elif search_type == "2":
            name = input("请输入姓名：")
            found = False
            for student_id in students:
                if students[student_id]["name"] == name:
                    info = students[student_id]
                    print(f"学号：{student_id}，姓名：{info['name']}，语文：{info['chinese']}，数学：{info['math']}，英语：{info['english']}")
                    found = True
            if not found:
                print("未找到该姓名的学生！")
        else:
            print("输入无效！")
            
    elif choice == "5":
        if len(students) == 0:
            print("暂无学生数据！")
        else:
            print(f"共{len(students)}名学生：")
            print("-"*50)
            for student_id in students:
                info = students[student_id]
                print(f"学号:{student_id},姓名:{info['name']},语文:{info['chinese']},数学:{info['math']},英语:{info['english']}")
                print("-" * 50)
    

            
    elif choice == "6":
        if len(students) == 0:
            print("暂无学生数据！")
        else:
            print(f"班级总人数 {len(students)}：")
            print("-"*50)
        
        chinese_sum = 0
        chinese_max = -1
        chinese_min = 101
        chinese_max_students = []
        chinese_min_students = []
        count = len(students)
        
        for student_id in students:
            s = students[student_id]
            score = s["chinese"]
            chinese_sum += score
            
            if score > chinese_max:
                chinese_max = score
                chinese_max_students = [s["name"]]
            elif score == chinese_max:
                chinese_max_students.append(s["name"])
                
            if score < chinese_min:
                chinese_min = score
                chinese_min_students = [s["name"]]
            elif score == chinese_min:
                chinese_min_students.append(s["name"])
                
        chinese_avg = chinese_sum/count
        
        print("语文：")
        print(f"  最高分：{chinese_max}（学生：{'、'.join(chinese_max_students)}）")
        print(f"  最低分：{chinese_min}（学生：{'、'.join(chinese_min_students)}）")
        print(f"  平均分：{chinese_avg:.2f}")
        
      
        math_sum = 0
        math_max = -1
        math_min = 101
        math_max_students = []
        math_min_students = []
        count = len(students)

        for student_id in students:
            s = students[student_id]
            score = s["math"]
            math_sum += score

        # 更新数学最高分
            if score > math_max:
                math_max = score
                math_max_students = [s["name"]]
            elif score == math_max:
                math_max_students.append(s["name"])

        # 更新数学最低分
            if score < math_min:
                math_min = score
                math_min_students = [s["name"]]
            elif score == math_min:
                math_min_students.append(s["name"])

        math_avg = math_sum / count

        print("数学：")
        print(f"  最高分：{math_max}（学生：{'、'.join(math_max_students)}）")
        print(f"  最低分：{math_min}（学生：{'、'.join(math_min_students)}）")
        print(f"  平均分：{math_avg:.2f}")


        # ========== 统计英语 ==========
        english_sum = 0
        english_max = -1
        english_min = 101
        english_max_students = []
        english_min_students = []
        count = len(students)

        for studient_id in students:
            s = students[studient_id]
            score = s["english"]
            english_sum += score

        # 更新英语最高分
            if score > english_max:
                english_max = score
                english_max_students = [s["name"]]
            elif score == english_max:
               english_max_students.append(s["name"])

        # 更新英语最低分
            if score < english_min:
                english_min = score
                english_min_students = [s["name"]]
            elif score == english_min:
                english_min_students.append(s["name"])

        english_avg = english_sum / count

        print("英语：")
        print(f"  最高分：{english_max}（学生：{'、'.join(english_max_students)}）")
        print(f"  最低分：{english_min}（学生：{'、'.join(english_min_students)}）")
        print(f"  平均分：{english_avg:.2f}")
        
        print("-"*50)
        
    elif choice == "7":
        print("再见，欢迎再次使用！")
        break
    
    else:
        print("操作非法，请输入正确的操作！")
 
      

      
         
        
         
                       
                  

                      
               
                
              
                     
                
                
                
                
                
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
                
                   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        