from database.mysql_connector import connector
from models.category import CategoryModel
from utils.thread import AsyncThread
import io
import random

# 异步执行
@AsyncThread
def handleInsert():
    # 执行查询
    # query = "SELECT version()"
    # result = connector.execute_query(query)
    # for row in result:
    #     print(row)

    category_model = CategoryModel(connector)
    
    # # 插入分类数据
    # category_model.create_category('科技', 1, 1001, 1001)

    # 自己造一批假数据
    dataString = getData()

    # 按行插入数据
    rows = dataString.split("\n")[1:]
    for row in rows:
        fields = row.split(",")
        if len(fields) != 4:
            print("字段数量不正确:", row)
            continue

        # 组装数据
        name       = fields[0]
        status     = fields[1]
        create_uid = fields[2]
        update_uid = fields[3]
        # 判断数据是否存在
        result = category_model.get_categories_by_conditions({"name": name})
        if len(result) == 0:
            # 然后插入数据
            category_model.create_category(name, status, create_uid, update_uid)

# 造假数据
def getData():
    # 数据字段
    field_names = ['name', 'status', 'create_uid', 'update_uid']
    # 定义要生成的数据行数
    num_rows = 10

    # 创建内存中的缓冲区
    buffer = io.StringIO()

    # 写入字段名到缓冲区
    buffer.write(','.join(field_names) + '\n')

    # 生成数据并写入缓冲区
    for _ in range(num_rows):
        row = {
            field_names[0]: random.choice(['北京', '南京', '东京', 'A' , 'B' , 'C' , 'D']),
            field_names[1]: random.choice([1,0]),
            field_names[2]: random.randint(1, 100),
            field_names[3]: random.randint(1, 100),
        }
        buffer.write(','.join(map(str, row.values())) + '\n')

    # 将缓冲区内容转换为字符串
    data_string = buffer.getvalue()

    # 关闭缓冲区
    buffer.close()

    print(data_string)
    return data_string

# name,status,create_uid,update_uid
# 南京,0,15,89
# 东京,0,43,64
# 北京,1,44,66
# 北京,0,45,55
# 南京,0,76,63
# 北京,1,29,31
# 南京,0,76,4
# 东京,1,6,21
# 东京,0,90,42
# 南京,1,33,66
