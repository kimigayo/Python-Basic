# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。
tuple = (1000,True,'python',1.234,3+2j)
typetuple = (1000,True,'python')
print(tuple)
print(tuple[2])
print(tuple[2:4])
print(tuple[2:])
print(tuple[2:-1])
print(tuple[2:]*2)
print(tuple+typetuple)
# tuple[0]=100# 1、与字符串一样，元组的元素不能修改。
blank=()
single=(1,)#一个元素，需要在元素后添加逗号，确保single[0]不报错
print(blank)
print(single[0])
print(tuple[0] is typetuple[0])
