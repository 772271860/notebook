import os
from pathlib import *

a = Path(r"C:\Users\Administrator\Desktop\test2")
b = Path(r"C:\Users\Administrator\Desktop\test")


# 在这里是实现了将一个文件夹的所有结构复制到另一个文件夹，包括内容
# 也可以指定哪些类型文件是可以复制的
def copy(source_path: Path, destination_path: Path, file_type: list=None):
    for p in list(source_path.rglob("*")):
        if p.is_dir():
            if Path(str(p).replace(str(source_path), str(destination_path))).exists():
                pass
            else:
                Path.mkdir(Path(str(p).replace(str(source_path), str(destination_path))))
        if p.is_file():
            if file_type and p.suffix in file_type:
                with open(p, 'rb') as sor:
                    con = sor.read()
                    with open(Path(str(p).replace(str(source_path), str(destination_path))), 'wb') as des:
                        des.write(con)

copy(a, b, ['.txt'])


# with open(a, 'rb') as a:
#     con = a.read()
#     with open(b, 'wb') as b:
#         b.write(con)
# if not b.parent.exists():
#     Path.mkdir(b.parent)
# else:
#     pass
# with open(b, 'rb') as b:
#     con = b.read()
#     with open(a, 'wb') as a:    
#         a.write(con)


# 对象之间会共享默认值
# 当我们设置一个默认参数是可变对象时，函数调用时，默认值只会在函数定义时创建一次。
# 如果后续调用该函数，将会引用这个改动的对象。
def add(value, l=[]):
    l.append(value)
    return l

print(add(1))
print(add(2))
print(add(3))

def updates(value, mydict=set([])):
    print(id(mydict))
    mydict.add(value)
    return mydict
print(updates(1))
print(updates(2))
print(updates(3))

def new(dict, mydict={}):
    mydict.update(dict)
    return mydict
print(new({"a": 2}))
print(new({"b": 2}))
print(new({"c": 2}))

def expensive(arg1, arg2, *, _cache={}):
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]
    
    result = 1 + 2
    _cache[(arg1, arg2)] = result
    return _cache

print(expensive(1, 2))
print(expensive(2, 3))
print(expensive(2, 4))

