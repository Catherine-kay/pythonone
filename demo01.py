练习：获取用户输入的信息，并且储存到字典中。
个人信息包括name,age,sex.
"""
name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
userinfo = {}
userinfo.update(name=name,age=age,sex=sex)
print(userinfo)
