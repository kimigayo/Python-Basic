# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。
a="python"
print(a)
print(a[2:-1])
print(a[2:5])
print(a[2:])
print(a[2:]*2)
print(a+"test")
print("py\nthon")
print("py\\nthon")
print(r"py\nthon")
# a[0]="P"#Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
