# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标]
print("this\n")
print(r"this\n")
print("this ""is"" string")
print("this ""is"" string!"*2)
print('------------------------------')
str ="python";
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print(input("按下回车后退出"))

