# 1.1 数据读取
## 1. 读取 Excel 文件
## - 读取当前目录下面 某招聘网站数据.csv 文件
## - 读取当前目录下 TOP250.xlsx 文件

from pathlib import Path
import pandas as pd
import numpy as np

file = Path(r"C:\Users\Administrator\Desktop\pandas进阶修炼")

data1 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8')
# print(data.head(10))

data2 = pd.read_excel(file.joinpath('TOP250.xlsx'))
# print(data2.head(10))

## 2. 读取 Excel 文件 | 指定位置

## 3. 读取 Excel 文件 | 指定行（顺序）
## 读取当前目录下 某招聘网站数据.csv文件前20行
data3 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', nrows=20)
# print(data3)


## 4. 读取 Excel 文件 | 指定行（跳过）
data4 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', skiprows=[i for i in range(1, 21)])
# print(data4)

## 5. 读取 Excel 文件 | 指定行（条件）
## 读取偶数行
data5 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', skiprows=lambda x: (x != 0) and not x % 2)
# print(data4)

## 6. 读取 Excel 文件 | 指定列（列号）
data6 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', usecols=[0, 2, 4])
# print(data6)

## 7. 读取 Excel 文件 | 指定列（列名）
data7 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', usecols=["positionId", "positionName", "salary"])
# print(data7)

## 8. 读取 Excel 文件 | 指定列（匹配）
usecols = ['positionId', 'test', 'positionName', 'test1', 'salary']
data8 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', usecols=lambda x: x in usecols)
# print(data8)

## 9. 读取 Excel 文件｜指定索引
data9 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', usecols=lambda x: x in usecols, index_col='positionId')
# print(data9)

## 10. 读取 Excel 文件｜指定标题
##  读取当前目录下 某招聘网站数据.csv 文件的 positionId、positionName、salary 列，并将标题设置为 ID、岗位名称、薪资
data10 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', 
                     usecols=[0, 1, 17],
                     header=None,
                     names=['ID', '岗位名称', '薪资'])
# print(data10.head())

## 11. 读取 Excel 文件｜缺失值转换
data11 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), encoding='utf-8', 
                     usecols=[0, 1, 17], keep_default_na=False)
print(data11.isna().any())

## 12. 读取 Excel 文件｜缺失值标记
data12 = pd.read_csv(file.joinpath('某招聘网站数据.csv'),
                     keep_default_na=True, na_values=['[]'])
# print(data12.to_excel(file.joinpath('t.xlsx')))

## 13. 读取 Excel 文件｜忽略缺失值
## 读取当前目录下 某招聘网站数据.csv 文件，但不处理缺失值
data13 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), na_filter=False)
# print(data13.head())

## 14. 读取 Excel 文件｜指定格式
data14 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), na_filter=False, dtype={"positionId": str,"companyId": str})

## 15. 读取 Excel 文件｜指定格式（时间）
data15 = pd.read_csv(file.joinpath('某招聘网站数据.csv'), parse_dates=["createTime"])
print(data15.head(5))

## 16 读取 Excel 文件｜分块读取
data = pd.read_csv("某招聘网站数据.csv",chunksize=10) 

## 17 读取 txt 文件｜常规
data = pd.read_csv("Titanic.txt") 

## 18 读取 txt 文件｜含中文
data = pd.read_table("TOP250.txt",encoding='gb18030')
# data = pd.read_csv("TOP250.txt",encoding='gb18030',sep = '\t') # 使用 read_csv 也可

## 19 读取 JSON 文件
data = pd.read_json("某基金数据.json")

## 20 读取 HDF5 文件
data = pd.read_hdf("store_tl.h5", "table")

## 21 从剪贴板读取数据
data = pd.read_clipboard()

## 22 从 SQL 读取数据
# conn = 1
# pd.read_sql('SELECT int_column, date_column FROM test_data', conn)

## 23 从网页读取数据
data = pd.read_html("https://olympics.com/tokyo-2020/olympic-games/zh/results/all-sports/medal-standings.htm")[0]

## 24 循环读取数据
import os
path = 'demodata/'
filesnames = os.listdir(path)
filesnames = [f for f in filesnames if f.lower().endswith(".xlsx")]
df_list = []
for filename in filesnames:
    df_list.append(pd.read_excel(path + filename))

df = pd.concat(df_list)

# 1.2 数据创建
## 25 从列表创建
l = [1,2,3,4,5]
df = pd.DataFrame(l, columns=["早起Python"])
# print(df)

## 26 从列表创建｜嵌套列表
l = [[1,2,3],[4,5,6]]
df = pd.DataFrame(l, index=["公众号","早起Python"])

## 27 从字典创建
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]) }
df = pd.DataFrame(d, )

## 28 从字典创建｜指定索引
df = pd.DataFrame(d, index=['d', 'b', 'a'])

## 29 从字典创建｜指定列名
data = pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])

## 30 从字典创建｜字典列表
d = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
data = pd.DataFrame(data2)

## 31 从集合创建
t =((1,0,0,0,),(2,3,0,0,),(4,5,6,0,),(7,8,9,10,))
data = pd.DataFrame(t, columns=[1,2,3,4], index=[1,2,3,4])

## 32 保存为 CSV

## 33 保存为 CSV｜指定列
data.to_csv("out.csv",encoding = 'utf_8_sig',columns=['positionName','salary'])

## 34 保存为 CSV｜取消索引
data.to_csv("out.csv",encoding = 'utf_8_sig',index=None)

## 35 保存为 CSV｜标记缺失值
data.to_csv("out.csv",encoding = 'utf_8_sig',index=None, na_rep='数据缺失')

## 36 保存为CSV｜压缩
compression_opts = dict(method='zip',
                        archive_name='out.csv')  
data.to_csv('out.zip', index=False,
          compression=compression_opts)  

## 37 保存为 Excel
data.to_excel("test.xlsx")

## 38 保存为 JSON
data.to_json("out.json")

## 39 保存为 Markdown
data.head().to_markdown(index = None)

## 40 保存为 Html
data.to_html("out.html", col_space=100,index = None,justify = 'center',border = 1)