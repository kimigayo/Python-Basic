"""
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""
dict = {1:'jack'}
print(dict[1])
dict['name']='mick'
print(dict)
print(dict.keys())
print(dict.values())
del dict
typedict=dict([(1,"jack"),(2,'jay')])
print(typedict)
typedict=dict(jack=1000,jay=200)
print(typedict)
typedict={x:x**3 for x in (1,2,3)}
print(typedict)
