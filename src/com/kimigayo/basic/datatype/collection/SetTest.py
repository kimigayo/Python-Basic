set ={1,"jack",True,False,3+2j}
print(set)# 输出集合，重复的元素被自动去掉
if 'jack' in set:
    print('jack 在集合中')
else:
    print('jack不在集合中')
del set
a=set('abacddaydfghi')
b=set('adlpyt')
print(a)
print(a - b) # a和b的差集
print(a | b) # a和b的并集
print(a & b) # a和b的交集
print(a ^ b) # a和b中不同时存在的元素
