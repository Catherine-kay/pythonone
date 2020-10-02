# a = 1
# b = 2
# if a > b:
#     print("a大于b")
# else:
#     print("a小于b")
"""
grade = float(input("请输入您的成绩："))
if grade == 60:
    print("及格")
elif grade > 60 and grade < 80:
    print("中")
elif grade >= 80 and grade < 90:
    print("良")
elif grade >=0 and grade < 60:
    print("差")
else:
    print("优")
"""
# a = "您好"
# if a in "您好，欢迎来到江苏师范大学":
#     print("谢谢")
# else:
#     print("pelase say hello")

# age = input("请输入年龄：")
# if age in "0123456789":
#     age = int(age)
# else:
#     print("请输入正确的年龄")

# a = 2.444
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

"""
练习：
将10个同学的成绩录入到系统中。要求：
1.名字和成绩需要一一对应；
2.成绩大于60和小于60的分开存放。
"""
# highgrade = {}
# lowgrade = {}
# studentlist = ["张三","李四","王麻子","二狗子","陈皮子","希希","流云","温习","胡曦","贾克","柯宇"]
# a = 0
# while a < len(studentlist):
#     grade = int(input("请输入"+studentlist[a]+"的成绩:"))
#     if grade >= 60:
#         highgrade[studentlist[a]] = grade
#     else:
#         lowgrade[studentlist[a]] = grade
#     a = a + 1
# print("成绩大于60的同学：",highgrade)
# print("成绩小于60的同学：",lowgrade)

# highgrade = {}
# lowgrade = {}
# studentlist = ["张三","李四","王麻子","二狗子","陈皮子","希希","流云","温习","胡曦","贾克","柯宇"]
# for i in studentlist:
#     grade = int(input("请输入"+i+"的成绩:"))
#     if grade >= 60:
#         highgrade[i] = grade
#     else:
#         lowgrade[i] = grade
# print("成绩大于60的同学：",highgrade)
# print("成绩小于60的同学：",lowgrade)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",i*j,end="  ")
#     print()

"""
练习1：
通过print打印，模拟一个红路灯的功能，注意：红灯30次，绿灯30次，黄灯30次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储存到字典中，{username,password}
"""