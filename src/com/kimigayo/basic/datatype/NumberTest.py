# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
a,b,c,d=10,1.1,False,4+3j
print(d.real)
print(d.imag)
print(type(a),type(b),type(c),type(d))
print(isinstance(a,int))
print(True+a)
e=10
print(a is e)
a=20
print(a is e)
f=10000
g=10000
print(f is g)
print(id(f))
print(id(g))
# Python 所谓的奇进偶弃???????
print(round(12.5))
print(round(11.5))
print(round(22.65,1))
print(round(22.85,1))
print(round(15.215,2))
print(round(16.225,2))
