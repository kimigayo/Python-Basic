# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
'''注释'''
import sys; str = 'python';sys.stdout.write(str+"\n");
for i in sys.argv:
    print(i)
print("python 的路径为",sys.path)
from sys import argv,path
print('-------python import------')
print('path',path)
for i in argv:
    print(i)
print(max.__doc__)
