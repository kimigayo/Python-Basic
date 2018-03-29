'''
int(x [,base])将x转换为一个整数
float(x)将x转换到一个浮点数
complex(real [,imag])创建一个复数
str(x)将对象 x 转换为字符串
repr(x)将对象 x 转换为表达式字符串
eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)将序列 s 转换为一个元组
list(s)将序列 s 转换为一个列表
set(s)转换为可变集合
dict(d)创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)转换为不可变集合
chr(x)将一个整数转换为一个字符
ord(x)将一个字符转换为它的整数值
hex(x)将一个整数转换为一个十六进制字符串
oct(x)将一个整数转换为一个八进制字符串
'''
print(int(1.2))
print(float(100))
print(complex(1+2,3))
print(str(100)+'test')
print(repr({1,True,'jack'}))
print(eval('2+3'))
print(tuple('jack'))
print(list('jackjack'))
print(set('jackjack'))
print(dict())
print(chr(10000))
print(ord('j'))
print(hex(19))
print(oct(19))
print(bin(200))
