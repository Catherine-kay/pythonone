"""
print("你好呀！")
print(2333)
print(2.333)
print(True) #布尔值
print({})
print(())
print("哈哈",2333)
print(((23+25)*8)/2)
print(2>3)

a = input("请输入内容：")
b = input("请输入内容：")
print("input获取的值:",a+b)
"""

# print(type("你好"))
# print(type(2333))
# print(type(2.33))
# print(type(()))
# print(type([]))
# print(type({}))
# a = int(2333)
# print(type(a))

# a =input("请输入内容：")
# b = input("请输入内容：")
# print("input获取的值:",len(a+b))

"""
练习：获取用户输入的信息，并且储存到字典中。
个人信息包括name,age,sex.
"""
name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
userinfo = {}
userinfo.update(name=name,age=age,sex=sex)
print(userinfo)
