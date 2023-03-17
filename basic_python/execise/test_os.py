import os
import random
from openpyxl import Workbook
import pandas as pd


"""
    将一个目录下的所有不同类别的文件拼接在一起
    比如.txt的拼接在.txt下，.xlsx和.xls拼接在一起以此类推
    并将其放在一个新建的目录下的new.txt,new.xlsx
"""

def generator_txt(n):
    for con in range(n):
        os.system(f"cd e:\\转用表\\test && type nul>some{con}.txt")
        with open(f"e:\\转用表\\test\\some{con}.txt", 'w') as f:
            f.write(f"some{con}")


def generator_xlsx(n):
    for i in range(n):
        book = Workbook()
        sheet = book.active
        sheet['A1'] = random.random() * 10
        sheet['A2'] = random.random() * 10
        book.save(f"e:\\转用表\\test\\test{i}.xlsx")

def get_con(PATH):
    new1 = (PATH + "\\res\\new.txt")
    new2 = (PATH + "\\res\\new.xlsx")
    new = pd.read_excel(new2)
    for file_name in os.listdir(PATH):
        filepath = os.path.join(PATH + '\\' + file_name)
        suffix = os.path.splitext(filepath)[1]
        if suffix == '.txt':
            with open(new1, mode='a') as m:
                with open(filepath, mode='r') as f:
                    con = f.read()
                m.write(con)
                m.write('\n')
        elif suffix == '.xlsx':
            con = pd.read_excel(filepath, header=None)
            new = pd.concat([new, con], axis=0)
    new.to_excel(new2, index=None, header=None)


if __name__ == '__main__':
    # 生成复杂的文件树
    # generator_txt(5)
    # generator_xlsx(5)
    # print(os.path.abspath(PATH))
    PATH = r"E:\转用表\test"
    get_con(PATH)