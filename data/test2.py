import pandas as pd
import sqlite3
# import mysql.connector

# 读取Excel文件
excel_file = 'biaojiegou.xlsx'
df = pd.read_excel(excel_file)
print(df)
# 将第一行作为列名
new_header = df.iloc[0] # 将第一行作为新的列名
df = df[1:] # 删除第一行
df.columns = new_header # 将列名设置为新的列名
print(df)


# 创建表
table_name = 'example_table'
create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for index, row in df.iterrows():
    field_name = row['name']
    # chinese_name = row['chineseName']
    field_type = row['type']
    field_length = row['long']
    key_value = row['key']
    is_null = row['isNull']
    # beizhu = row['beizhu']

    if field_type == 'int':
        field_type = 'INTEGER'
    elif field_type == 'float':
        field_type = 'REAL'
    elif field_type == 'str':
        field_type = 'TEXT'


    if field_length:
        field_type += f"({field_length})"

    if key_value == 'Y':
        key_value = f"PRIMARY KEY"
    else: key_value = ' '

    if is_null == 'N':
        is_null = "NOT NULL"
    else:
        is_null = ""

    create_table_sql += f"{field_name} {field_type} {key_value} {is_null}, " +'\n'
#     todo : 将拼接的数据库保存到txt文本中，结果输出命令行看着难受

create_table_sql = create_table_sql[:-2] + ")"
print(create_table_sql)
with open('example.txt', 'w') as f:
    f.write(create_table_sql)
