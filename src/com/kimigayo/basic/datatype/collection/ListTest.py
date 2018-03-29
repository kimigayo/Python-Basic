# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。
list = [1, 'python', True, 3+2j, 2.345]
typeList = ['python', True, complex(3 + 2,3)]
print(list)
print(list[1])
print(list[1:3])  # 输出第二、第三个元素
print(list[1:])
print(list[1:] * 2)
print(list + typeList)
list[0]=100
print(list)
print(list.pop(1))
list.append("python")
print(list)
